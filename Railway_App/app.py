#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REVISOR DE PRODUCTOS 3D - APLICACIÓN WEB CORREGIDA
Versión para Railway - Acceso mediante enlace web
"""

from flask import Flask, render_template, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
import io
import os
import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def tiene_modelo_3d(producto_html):
    """Detecta si un producto tiene modelo 3D"""
    if isinstance(producto_html, str):
        soup = BeautifulSoup(producto_html, 'html.parser')
    else:
        soup = producto_html
    
    if soup.find('model-viewer'):
        src = soup.find('model-viewer').get('src', '')
        if '.glb' in src.lower():
            return True, "Modelo 3D (.glb)"
        return True, "Model viewer"
    
    if soup.find(class_='modelViewerBlock'):
        return True, "modelViewerBlock"
    
    if '.glb' in str(soup).lower():
        return True, "Archivo .glb"
    
    if re.search(r'id="model\d+"', str(soup)):
        return True, "ID modelo"
    
    if soup.find(class_=re.compile(r'b3dviewer')):
        return True, "b3dviewer"
    
    return False, "Solo foto estática"

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/revisar', methods=['POST'])
def revisar():
    """Procesar revisión de productos"""
    try:
        data = request.get_json()
        base_url = data.get('url', '').strip()
        total_paginas = int(data.get('paginas', 10))
        
        if not base_url or not base_url.startswith('http'):
            return jsonify({'error': 'URL inválida'}), 400
        
        productos_sin_3d = []
        todos_productos = []
        errores = []
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        for num_pagina in range(1, total_paginas + 1):
            try:
                # Construir URL
                if num_pagina == 1:
                    url = base_url
                else:
                    if '?' in base_url:
                        url = f"{base_url}&product-page={num_pagina}"
                    else:
                        url = f"{base_url}?product-page={num_pagina}"
                
                # Hacer petición
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()
                
                # Parsear HTML
                soup = BeautifulSoup(response.content, 'html.parser')
                productos = soup.find_all('li', class_='product')
                
                if not productos:
                    errores.append({
                        'pagina': num_pagina,
                        'error': 'No se encontraron productos'
                    })
                    continue
                
                # Analizar productos
                for producto in productos:
                    nombre_tag = producto.find('h2', class_='woocommerce-loop-product__title')
                    nombre = nombre_tag.text.strip() if nombre_tag else "Sin nombre"
                    
                    enlace_tag = producto.find('a', class_='woocommerce-LoopProduct-link')
                    url_producto = enlace_tag['href'] if enlace_tag and 'href' in enlace_tag.attrs else ""
                    
                    tiene_3d, detalle = tiene_modelo_3d(producto)
                    
                    info = {
                        'numero': len(todos_productos) + 1,
                        'nombre': nombre,
                        'url': url_producto,
                        'pagina': num_pagina,
                        'tiene_modelo_3d': tiene_3d,
                        'detalle': detalle
                    }
                    todos_productos.append(info)
                    
                    if not tiene_3d:
                        productos_sin_3d.append(info)
                
                # Pequeña pausa entre peticiones
                time.sleep(0.3)
                
            except Exception as e:
                errores.append({
                    'pagina': num_pagina,
                    'error': str(e)
                })
        
        # Retornar resultados
        resultado = {
            'completado': True,
            'total_productos': len(todos_productos),
            'sin_3d': len(productos_sin_3d),
            'con_3d': len(todos_productos) - len(productos_sin_3d),
            'errores': len(errores),
            'datos': {
                'todos': todos_productos,
                'sin_3d': productos_sin_3d,
                'errores': errores
            }
        }
        
        return jsonify(resultado)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/descargar', methods=['POST'])
def descargar():
    """Generar y descargar Excel"""
    try:
        data = request.get_json()
        todos_productos = data.get('todos', [])
        productos_sin_3d = data.get('sin_3d', [])
        url_revisada = data.get('url', '')
        
        # Crear Excel en memoria
        output = io.BytesIO()
        
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Resumen
            df_resumen = pd.DataFrame({
                'Métrica': [
                    'Total productos',
                    'Sin modelo 3D',
                    'Con modelo 3D',
                    'Porcentaje sin 3D',
                    'URL revisada',
                    'Fecha'
                ],
                'Valor': [
                    len(todos_productos),
                    len(productos_sin_3d),
                    len(todos_productos) - len(productos_sin_3d),
                    f"{(len(productos_sin_3d)/len(todos_productos)*100):.2f}%" if todos_productos else "0%",
                    url_revisada,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ]
            })
            df_resumen.to_excel(writer, sheet_name='Resumen', index=False)
            
            # Productos sin 3D
            if productos_sin_3d:
                df_sin_3d = pd.DataFrame(productos_sin_3d)
                df_sin_3d = df_sin_3d[['numero', 'nombre', 'pagina', 'url', 'detalle']]
                df_sin_3d.columns = ['#', 'Nombre', 'Página', 'URL', 'Motivo']
                df_sin_3d.to_excel(writer, sheet_name='Sin Modelo 3D', index=False)
            
            # Todos los productos
            df_todos = pd.DataFrame(todos_productos)
            df_todos = df_todos[['numero', 'nombre', 'pagina', 'tiene_modelo_3d', 'url']]
            df_todos.columns = ['#', 'Nombre', 'Página', 'Tiene 3D', 'URL']
            df_todos.to_excel(writer, sheet_name='Todos', index=False)
        
        output.seek(0)
        
        fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"Reporte_Productos_3D_{fecha_hora}.xlsx"
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=nombre_archivo
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check para Railway"""
    return jsonify({'status': 'ok', 'version': '1.0.1'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
