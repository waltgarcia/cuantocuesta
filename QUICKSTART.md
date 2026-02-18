# 🚀 Guía Rápida de Despliegue

## 📌 Opción 1: Usar Online (Más Fácil)

Solo haz clic aquí: [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cuantocuesta.streamlit.app)

**Listo.** No necesitas instalar nada. ✨

---

## 💻 Opción 2: Ejecutar Localmente

### Requisitos:
- Python 3.8+
- Git

### Pasos:

```bash
# 1. Clonar el repositorio
git clone https://github.com/waltgarcia/cuantocuesta.git
cd cuantocuesta

# 2. Crear ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la app
streamlit run streamlit_app.py
```

La app se abrirá en `http://localhost:8501`

---

## 🌐 Opción 3: Desplegar tu Propia Versión en Streamlit Cloud

### Requisitos:
- Cuenta de GitHub
- Cuenta de Streamlit Cloud (gratuita)

### Pasos:

1. **Fork este repositorio** en GitHub

2. **Ve a [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Haz clic en "New app"** y completa:
   - Repository: `tu-usuario/cuantocuesta`
   - Branch: `main`
   - Main file: `streamlit_app.py`

4. **Click en "Deploy"** ¡y listo! 🎉

Tu app estará disponible en:
```
https://tu-usuario-cuantocuesta.streamlit.app
```

---

## 📝 Personalización

Si despliegas tu propia versión, puedes editar:

- `streamlit_app.py` - Lógica principal
- `.streamlit/config.toml` - Tema y colores
- `README.md` - Documentación

Después de hacer cambios, solo haz push a GitHub y se desplegará automáticamente.

---

## 🆘 Problemas Comunes

**P:** No puedo instalar las dependencias
**R:** Asegúrate de tener Python 3.8+ (`python --version`)

**P:** El app no se abre en localhost
**R:** Intenta: `streamlit run streamlit_app.py --logger.level=debug`

**P:** Quiero cambiar los colores
**R:** Edita `.streamlit/config.toml`

---

## 📞 Soporte

- 📚 [Documentación de Streamlit](https://docs.streamlit.io)
- 🐛 [Abre un issue en GitHub](https://github.com/waltgarcia/cuantocuesta/issues)
- 📧 Contáctame: walt@example.com

---

**¿Te gusta la calculadora? ⭐ Dale una estrella en GitHub!**
