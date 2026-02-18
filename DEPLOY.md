# 📋 Instrucciones de Publicación en GitHub

## Paso 1: Preparar los archivos

Los archivos ya están listos en tu workspace:
- ✅ `streamlit_app.py` - Aplicación principal
- ✅ `requirements.txt` - Dependencias (Streamlit + Plotly)
- ✅ `README.md` - Documentación completa
- ✅ `QUICKSTART.md` - Guía rápida de uso
- ✅ `.streamlit/config.toml` - Configuración de tema
- ✅ `.gitignore` - Archivos a ignorar

## Paso 2: Publicar en GitHub

Abre tu terminal en la carpeta `/workspaces/cuantocuesta` y ejecuta:

```bash
# 1. Inicializar git (si no lo has hecho)
git init

# 2. Agregar todos los archivos
git add .

# 3. Hacer commit
git commit -m "feat: Agregar calculadora de costos reales con visualizaciones Plotly

- Cálculo automático de precio final según régimen fiscal SAT
- 3 regímenes fiscales actualizados (RESICO, General, Personas Físicas)
- Gráficos interactivos de desglose de costos
- Tabla detallada de componentes
- Documentación completa para GitHub"

# 4. Empujar a GitHub (reemplaza con tu rama)
git push -u origin main
```

## Paso 3: Desplegar en Streamlit Cloud

1. **Ve a [Streamlit Cloud](https://streamlit.io/cloud)**
2. **Inicia sesión con GitHub**
3. **Haz clic en "New app"**
4. **Completa:**
   - Repository: `waltgarcia/cuantocuesta`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. **Haz clic en "Deploy"**

¡Listo! Tu app estará disponible en una URL pública.

## Paso 4: Compartir tu App

Tu aplicación estará disponible en:
```
https://cuantocuesta.streamlit.app
```

Puedes compartir este link con:
- 👥 Tus clientes
- 📱 En redes sociales
- 📧 Por email
- 💼 En tu sitio web

## 🎯 Qué Obtiene el Usuario

Cuando acceden a tu link, los usuarios pueden:
1. Seleccionar su régimen fiscal
2. Ingresar costo base y % de utilidad
3. Ver automáticamente:
   - Desglose paso a paso
   - Gráfico de pastel (composición)
   - Gráfico de barras (costos en dinero)
   - Tabla detallada
4. Todo sin instalar nada, directamente en el navegador

## 📊 Actualizaciones Futuras

Si haces cambios al código en GitHub:
1. Git push automáticamente despliega en Streamlit Cloud
2. No necesitas hacer nada más
3. Los cambios estarán en vivo en segundos

## 🔧 Configuración Adicional (Opcional)

### Cambiar dominio personalizado
En Streamlit Cloud, puedes configurar un dominio personalizado (requiere plan pagado).

### Variables de entorno
Si necesitas secretos o variables, crea `.streamlit/secrets.toml`:
```toml
[example]
secret_key = "tu_clave_secreta"
```

### Límites y cuotas
- ✅ Gratuito para proyectos públicos
- ✅ 1 GB RAM
- ✅ 3 aplicaciones gratuitas
- ✅ Tráfico ilimitado

## 💡 Tips Importantes

1. **Mantén el README actualizado** - Los usuarios lo leen primero
2. **Agrega ejemplos** - Que muestren cómo usar
3. **Documenta cambios** - En los commits
4. **Responde issues** - En GitHub
5. **Dale mantenimiento** - Actualiza SAT cuando haya cambios

## 🎉 ¡Felicidades!

Tu calculadora está lista para que la uses y la compartas. Es una herramienta valiosa para emprendedores mexicanos. 🚀

---

**Notas finales:**
- La app funciona offline una vez cargada
- Es completamente gratuita usar Streamlit Cloud
- Los datos no se guardan (cada sesión es independiente)
- Puedes hacer cambios y ver actualizados al instante
