# 💰 Calculadora de Costo Real del Producto

Una aplicación web interactiva para calcular el precio final de productos considerando costos reales, utilidad deseada, ISR (Impuesto Sobre la Renta) e IVA (Impuesto al Valor Agregado) según las regulaciones fiscales del SAT en México.

## 🎯 Propósito

Esta calculadora resuelve un problema común entre emprendedores y pequeños negocios: **¿Cuál debe ser el precio real de venta de un producto para obtener la ganancia deseada después de pagar impuestos?**

Muchos vendedores cometen el error de sumar únicamente su ganancia deseada al costo del producto, sin considerar que esa ganancia debe pagar ISR. Esta herramienta calcula automáticamente el precio correcto utilizando la fórmula adecuada.

## 📺 Inspiración

La inspiración de esta calculadora surge posterior a ver el video:
**[¿Cuánto Cuesta Realmente Vender? - Costos Verdaderos](https://www.youtube.com/watch?v=5_G0b3IVeXM)**

En este vídeo se explica de manera clara por qué es importante calcular correctamente los costos reales de los productos, considerando todos los impuestos involucrados.

## ✨ Características

- ✅ **Cálculo automático** de precio final según régimen fiscal
- ✅ **3 regímenes fiscales** actualizados al SAT 2026:
  - RESICO (Régimen Simplificado de Contribuyentes)
  - Régimen General de Ley (Personas Morales)
  - Personas Físicas con Actividad Empresarial
- ✅ **Información detallada** sobre cada régimen fiscal
- ✅ **Desglose paso a paso** de cada cálculo
- ✅ **Resumen de ganancias** con montos de ISR e IVA
- ✅ **Interfaz intuitiva** y fácil de usar
- ✅ **Cálculos en tiempo real** mientras cambias los valores

## 📋 Pasos de Cálculo

La calculadora implementa los siguientes pasos:

### Paso 1: Costo Base
El costo base de producción del producto.

### Paso 2: Utilidad y Ajuste por ISR
Calcula la utilidad deseada, luego la ajusta usando la fórmula:
```
Utilidad Ajustada = Utilidad Deseada / (1 - Tasa ISR)
```
Esto garantiza que después de pagar el ISR, te queden los pesos de ganancia que planeaste.

### Paso 3: Subtotal (Precio sin IVA)
```
Subtotal = Costo Base + Utilidad Ajustada
```

### Paso 4: Cálculo de IVA
```
IVA = Subtotal × 16%
```
El IVA es del 16% según la tasa general del SAT en México.

### Paso 5: Precio Final al Público
```
Precio Final = Subtotal + IVA
```

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos

1. **Clonar el repositorio:**
```bash
git clone https://github.com/waltgarcia/cuantocuesta.git
cd cuantocuesta
```

2. **Crear un ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar las dependencias:**
```bash
pip install -r requirements.txt
```

## 🚀 Uso Online (Recomendado)

**Accesa la aplicación desplegada en Streamlit Cloud sin necesidad de instalar nada:**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cuantocuesta.streamlit.app)

Simplemente haz clic en el botón de arriba para usar la calculadora en línea.

## 🎮 Uso Local

Para ejecutar la aplicación en tu máquina:
```bash
streamlit run streamlit_app.py
```

La aplicación se abrirá en tu navegador predeterminado (generalmente en `http://localhost:8501`).

### Pasos para usar:

1. **Selecciona tu régimen fiscal** en las opciones disponibles
2. **Ingresa el costo base** de producción de tu producto
3. **Define el porcentaje de utilidad** que deseas obtener
4. **Automáticamente verás:**
   - Desglose detallado de cada paso
   - Precio final al público
   - Resumen de ganancias netas
   - Monto de ISR e IVA

## 🌐 Despliegue en Streamlit Cloud

Para desplegar esta aplicación en **Streamlit Cloud** (servicio gratuito):

### Pasos para desplegar:

1. **Despecha push de tus cambios a GitHub:**
```bash
git add .
git commit -m "Agregar calculadora de costos con Plotly"
git push origin main
```

2. **Ve a [Streamlit Community Cloud](https://streamlit.io/cloud)**

3. **Crea una cuenta (gratuita)** o inicia sesión con tu cuenta de GitHub

4. **Haz clic en "New app"** y selecciona:
   - **Repository:** `waltgarcia/cuantocuesta`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`

5. **¡Listo!** El app se desplegará automáticamente en una URL pública como:
   ```
   https://cuantocuesta.streamlit.app
   ```

### Compartir tu app:
Una vez desplegada, puedes compartir el link directamente con tus clientes y usuarios para que usen la calculadora sin necesidad de instalar nada.

**Ventajas de Streamlit Cloud:**
- ✅ Hosting gratuito
- ✅ Actualizaciones automáticas (cada push a GitHub se deploya automáticamente)
- ✅ Compatible con todos tus compañeros
- ✅ No requiere servidor propio
- ✅ Fácil de mantener

---

## 📊 Ejemplo

**Datos de entrada:**
- Régimen: RESICO
- Costo base: $700
- Porcentaje de utilidad: 30%

**Resultados:**
- Utilidad deseada: $210
- Utilidad ajustada por ISR (2.7%): $215.82
- Subtotal (sin IVA): $915.82
- IVA (16%): $146.53
- **Precio final al público: $1,062.35**
- Ganancia neta después de ISR: ~$210

## ⚠️ Disclaimer

Esta calculadora es una **herramienta orientativa**. Los resultados pueden variar según:
- Tu situación fiscal específica
- Deducciones permitidas según tu régimen
- Cambios en las tasas del SAT
- Otros impuestos o contribuciones locales

**Se recomienda ampliamente consultar con un contador o asesor fiscal profesional** para validar estos cálculos según tu situación particular.

## 🏛️ Regulaciones del SAT

La información tributaria incluida en esta calculadora está basada en:
- **Régimen Fiscal:** SAT 2026
- **IVA:** 16% (tasa general)
- **ISR:** Según régimen seleccionado

Para información oficial, visita: [Servicio de Administración Tributaria (SAT)](https://www.gob.mx/sat)

## 📱 Tecnología

- **Frontend/Backend:** [Streamlit](https://streamlit.io/) - Framework para aplicaciones web en Python
- **Lenguaje:** Python 3
- **Hospedaje:** Compatible con cualquier plataforma que soporte Streamlit

## 📦 Dependencias

Ver archivo `requirements.txt`:
```
streamlit
plotly
```

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo `LICENSE` para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 💬 Preguntas y Soporte

Si tienes preguntas o encuentras problemas, por favor abre un issue en el repositorio.

## 👨‍💻 Autor

Desarrollado por: **Walt García**

---

**Nota:** Esta herramienta es para fines educativos y de referencia. Siempre valida con profesionales en tributación antes de tomar decisiones fiscales importantes.

⭐ Si esta calculadora te fue útil, ¡considera darle una estrella en GitHub!
