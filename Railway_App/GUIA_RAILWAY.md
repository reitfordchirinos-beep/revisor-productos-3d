# 🚀 GUÍA COMPLETA - DESPLIEGUE EN RAILWAY

## 📋 ÍNDICE
1. [Preparar archivos](#paso-1-preparar-archivos)
2. [Crear cuenta/acceder a Railway](#paso-2-acceder-a-railway)
3. [Crear nuevo proyecto](#paso-3-crear-proyecto)
4. [Subir archivos](#paso-4-subir-archivos)
5. [Configurar límite de gasto ($5/mes)](#paso-5-configurar-límite-de-gasto)
6. [Obtener enlace público](#paso-6-obtener-enlace)
7. [Compartir con tu equipo](#paso-7-compartir)
8. [Monitorear uso y costos](#paso-8-monitorear)

---

## ✅ PASO 1: PREPARAR ARCHIVOS

### 1.1 Descargar todos los archivos
Asegúrate de tener estos archivos en una carpeta llamada `Railway_App`:

```
Railway_App/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
└── templates/
    └── index.html
```

### 1.2 Verificar que todos estén completos
- ✅ Todos los archivos descargados
- ✅ Carpeta `templates` con `index.html` dentro
- ✅ Sin archivos faltantes

---

## ✅ PASO 2: ACCEDER A RAILWAY

### 2.1 Abrir Railway
1. Ve a: **https://railway.app**
2. Ya tienes cuenta, así que haz clic en **"Login"**

### 2.2 Iniciar sesión
1. Ingresa con tu cuenta (email o GitHub)
2. Espera a que cargue el dashboard

---

## ✅ PASO 3: CREAR NUEVO PROYECTO

### 3.1 Desde el Dashboard de Railway

![Railway Dashboard](https://i.imgur.com/ejemplo.png)

1. Haz clic en **"New Project"** (botón morado en la parte superior)

### 3.2 Seleccionar método de despliegue

Verás 3 opciones:
- Deploy from GitHub repo
- **Deploy from template** 
- Empty project

**Elige:** "**Empty project**" o "**Deploy from GitHub repo**"

---

### 🔀 OPCIÓN A: Deploy desde GitHub (RECOMENDADA)

#### 3.2.A.1 Conectar GitHub
1. Haz clic en **"Deploy from GitHub repo"**
2. Autoriza a Railway para acceder a tu GitHub
3. Haz clic en **"Configure GitHub App"**

#### 3.2.A.2 Crear repositorio en GitHub
Antes de continuar, ve a GitHub y:

1. Ve a **https://github.com**
2. Haz clic en **"New repository"** (botón verde)
3. Nombre: `revisor-productos-3d`
4. Privacidad: **Private** (recomendado)
5. Haz clic en **"Create repository"**

#### 3.2.A.3 Subir archivos a GitHub

**Opción A1: Desde la web de GitHub:**

1. En tu nuevo repositorio, haz clic en **"uploading an existing file"**
2. Arrastra TODOS los archivos de la carpeta `Railway_App`
3. **IMPORTANTE:** También arrastra la carpeta `templates`
4. Escribe un mensaje: "Initial commit - Revisor 3D"
5. Haz clic en **"Commit changes"**

**Opción A2: Desde la terminal (si sabes usar Git):**

```bash
cd Railway_App
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/revisor-productos-3d.git
git push -u origin main
```

#### 3.2.A.4 Conectar repo a Railway
1. Vuelve a Railway
2. Selecciona el repositorio `revisor-productos-3d`
3. Railway detectará automáticamente que es Python
4. Haz clic en **"Deploy Now"**

---

### 🔀 OPCIÓN B: Deploy manual (MÁS SIMPLE)

#### 3.2.B.1 Usar Railway CLI

1. Abre la terminal/CMD
2. Instala Railway CLI:

**Windows (PowerShell como Administrador):**
```powershell
npm install -g @railway/cli
```

Si no tienes npm:
- Descarga desde: https://railway.app/cli
- Sigue las instrucciones de instalación

3. Navega a tu carpeta:
```bash
cd "C:\Users\Kalstein 3D\Descargas\Railway_App"
```

4. Inicia sesión en Railway:
```bash
railway login
```

5. Inicializa proyecto:
```bash
railway init
```

6. Despliega:
```bash
railway up
```

---

## ✅ PASO 4: CONFIGURAR EL PROYECTO

### 4.1 Esperar el despliegue inicial

Railway empezará a:
1. ✅ Detectar que es Python
2. ✅ Instalar dependencias (requirements.txt)
3. ✅ Ejecutar la aplicación

**Tiempo estimado:** 2-5 minutos

Verás un log como este:
```
Installing dependencies...
✓ Python 3.11.7
✓ Installing requirements...
✓ Starting application...
✓ Deployment successful
```

### 4.2 Verificar que esté funcionando

En el dashboard de Railway verás:
- 🟢 **Status: Active** (círculo verde)
- **Deployments: 1 successful**

---

## ✅ PASO 5: CONFIGURAR LÍMITE DE GASTO ($5/mes) 🔒

**¡MUY IMPORTANTE! Esto evitará cargos inesperados**

### 5.1 Ir a la configuración del proyecto

1. Estando en tu proyecto, busca en la barra lateral izquierda
2. Haz clic en **"Settings"** (ícono de engranaje ⚙️)

### 5.2 Configurar Usage Limits

1. En el menú de Settings, busca la sección **"Usage"** o **"Billing"**
2. Haz clic en **"Usage Limits"** o **"Set Spending Limit"**

### 5.3 Establecer el límite

Verás una pantalla con opciones:

```
┌─────────────────────────────────────┐
│  Set Monthly Spending Limit         │
├─────────────────────────────────────┤
│                                     │
│  [$5.00 USD]  ◄── Escribe aquí     │
│                                     │
│  ☑ Pause services when limit        │
│     is reached                      │
│                                     │
│  [ Cancel ]  [ Save Limit ]         │
└─────────────────────────────────────┘
```

1. Escribe: **5**
2. Marca la casilla: **"Pause services when limit is reached"**
3. Haz clic en **"Save Limit"**

### 5.4 Confirmar configuración

Railway te pedirá confirmar:
- "If you reach $5.00, we will pause your services"
- Haz clic en **"Confirm"**

✅ **¡Listo! Ahora estás protegido. Railway NO te cobrará más de $5/mes**

---

## ✅ PASO 6: OBTENER ENLACE PÚBLICO

### 6.1 Generar dominio público

1. En tu proyecto de Railway, busca la sección **"Settings"**
2. Ve a la pestaña **"Domains"** o **"Networking"**
3. Haz clic en **"Generate Domain"**

Railway generará un enlace como:
```
https://revisor-productos-3d-production.up.railway.app
```

### 6.2 Probar el enlace

1. Copia el enlace completo
2. Ábrelo en tu navegador
3. Deberías ver la interfaz de la aplicación ✅

Si NO funciona:
- Espera 1-2 minutos más (puede tardar en activarse)
- Verifica que el deployment diga "Active"
- Revisa los logs en Railway

---

## ✅ PASO 7: COMPARTIR CON TU EQUIPO

### 7.1 Copiar el enlace

El enlace será algo como:
```
https://tu-app-production.up.railway.app
```

### 7.2 Compartir de forma profesional

**Opción A: Email/WhatsApp:**
```
Hola equipo,

Ya está lista la herramienta para revisar productos 3D.

🔗 Enlace: https://revisor-productos-3d.up.railway.app

📖 Cómo usar:
1. Abre el enlace
2. Introduce la URL del sitio (ej: https://kalstein.co.ve/productos/)
3. Indica las páginas a revisar
4. Haz clic en "Comenzar Revisión"
5. Espera a que termine
6. Descarga el Excel con los resultados

¡No necesitan instalar nada! Funciona directo en el navegador.

Saludos
```

**Opción B: Crear acceso directo:**
1. Abre el enlace en Chrome
2. Haz clic en los 3 puntos (⋮)
3. Más herramientas → Crear acceso directo
4. Marca "Abrir como ventana"
5. Se crea un ícono en el escritorio

---

## ✅ PASO 8: MONITOREAR USO Y COSTOS

### 8.1 Ver consumo en tiempo real

1. En Railway, ve a tu proyecto
2. Haz clic en **"Usage"** en la barra lateral
3. Verás un gráfico con:
   - 💰 **Costo actual del mes**
   - 📊 **Uso de CPU**
   - 💾 **Uso de RAM**
   - 🌐 **Tráfico de red**

### 8.2 Configurar alertas

1. Ve a **Settings → Notifications**
2. Activa alertas para:
   - ✅ **"Usage threshold reached"** (75% del límite)
   - ✅ **"Deployment failed"**
   - ✅ **"Service crashed"**

3. Introduce tu email para recibir notificaciones

### 8.3 Revisar uso mensual

Railway resetea el contador cada mes. Verifica:

```
┌─────────────────────────────────┐
│  Monthly Usage                  │
├─────────────────────────────────┤
│  Current: $1.23 / $5.00         │
│  Progress: [████░░░░░░] 24%     │
│  Days left: 18                  │
└─────────────────────────────────┘
```

### 8.4 ¿Qué hacer si te acercas al límite?

Si llegas a $4.50-$4.90:

**Opción 1:** Pausar temporalmente
- Settings → Pause service
- Espera al siguiente mes

**Opción 2:** Optimizar uso
- Reducir número de páginas por revisión
- Usar en horarios específicos

**Opción 3:** Aumentar límite (si es necesario)
- Settings → Usage Limits
- Cambiar a $10 o $15
- Solo si realmente lo necesitas

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Problema 1: "Application Error" al abrir el enlace

**Solución:**
1. Ve a Railway → Deployments
2. Haz clic en el último deployment
3. Revisa los **logs**
4. Busca errores en rojo
5. Comparte el error conmigo para ayudarte

### Problema 2: El deployment falla

**Causas comunes:**
- ❌ Falta el archivo `requirements.txt`
- ❌ Falta la carpeta `templates`
- ❌ Error en `Procfile`

**Solución:**
1. Verifica que TODOS los archivos estén subidos
2. Re-despliega: Settings → Redeploy

### Problema 3: La aplicación se "duerme"

**Esto es normal en Railway.** La app se duerme después de 15 min sin uso.

**Solución:**
- Al abrir el enlace, espera 10-15 segundos
- La app "despertará" automáticamente
- Después funcionará normal

### Problema 4: Excedí el límite de $5

**Solución:**
1. Railway pausará automáticamente el servicio
2. NO te cobrará más
3. Espera al siguiente mes
4. O aumenta el límite si es necesario

---

## 📊 RESUMEN DE COSTOS ESTIMADOS

| Uso | Revisiones/mes | Tiempo | Costo estimado |
|-----|----------------|--------|----------------|
| **Bajo** | 5-10 | ~50 min | $0.50 - $1.00 |
| **Medio** | 20-30 | ~3 hrs | $1.50 - $2.50 |
| **Alto** | 50-80 | ~8 hrs | $3.00 - $4.50 |
| **Muy Alto** | 100+ | ~15 hrs | $4.50 - $5.00 |

✅ **Con el límite de $5, NUNCA pagarás más de eso**

---

## 🎯 CHECKLIST FINAL

Antes de compartir con tu equipo, verifica:

- [ ] Proyecto desplegado en Railway
- [ ] Estado: 🟢 Active
- [ ] Enlace público funcionando
- [ ] **Límite de $5/mes configurado** ✅
- [ ] Alertas de uso activadas
- [ ] Prueba realizada con éxito
- [ ] Enlace compartido con el equipo

---

## 📞 SOPORTE

Si tienes problemas:

1. **Revisa los logs** en Railway
2. **Verifica el límite** esté configurado
3. **Contacta soporte** de Railway si es necesario
4. **O escríbeme** y te ayudo a resolver

---

## 🎉 ¡FELICIDADES!

Tu aplicación ya está en la nube y lista para usar.

**Enlace de ejemplo:**
```
https://tu-proyecto.up.railway.app
```

**Características:**
✅ Acceso 24/7 desde cualquier lugar
✅ No necesita instalación
✅ Protección de $5/mes
✅ Actualizaciones centralizadas
✅ Profesional y fácil de usar

---

## 📌 TIPS ADICIONALES

### Personalizar el dominio (opcional)

Si quieres un dominio más profesional:
1. Settings → Domains
2. Add Custom Domain
3. Introduce: `revisor.tuempresa.com`
4. Sigue las instrucciones de DNS

### Actualizar la aplicación

Si necesitas cambios:
1. Edita los archivos en GitHub
2. Haz commit de los cambios
3. Railway re-desplegará automáticamente

### Hacer backup

1. Exporta tu código de GitHub
2. Descarga los reportes Excel generados
3. Guarda configuraciones importantes

---

**¿Listo para desplegar? ¡Comienza con el PASO 1!** 🚀
