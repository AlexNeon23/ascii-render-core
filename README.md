# 🎨 ascii-render-core

Convierte imágenes en arte ASCII directamente desde la terminal.  
El objetivo es construir un motor modular que eventualmente pueda manejar imágenes, video, webcam y exportar resultados tanto en consola como en archivos `.txt` o una web visual.

---

## 📁 Estructura del Proyecto

ascii-render-core/
├── src/
│ └── ascii_render_core/
│ ├── **init**.py
│ ├── app.py
│ ├── render.py
│ ├── input/
│ └── output/
├── inputs/
├── outputs/
├── README.md
├── pyproject.toml
└── .gitignore

```

---

## ⚙️ Requisitos

- Python 3.10+
- Librerías:
  - `Pillow` para manipulación de imágenes
  - 'OpenCV' para CV en tiempo real.

Instala las dependencias con:

pip install pillow

---

## 🚀 Cómo Ejecutar

Desde la raíz del proyecto, ejecuta el archivo `app.py` como módulo:


python -m core.app <ruta_imagen> <ancho> <modo>

### Ejemplo:


antes: python -m core.app ./inputs/image/molly.jpg 500 1

ahora: python -m ascii_render_core.app  inputs/image/portal.png 500 0


- `./inputs/image/molly.jpg` → Ruta de la imagen
- `500` → Ancho del arte ASCII
- `0` → Guardar el resultado en un `.txt` (1 para no guardar e imprimir en consola)

---

## 📦 Salidas

- El arte ASCII se guarda como .txt o .avi mode == 0.
- El arte ASCII se imprime en consola mode == 1

---

## 🛠️ Próximamente

- ✅ Soporte para cámara web
- 🌐 Visualización en navegador (web UI)
- 🎚️ Panel de ajustes interactivo

---

## 🧠 Autor

**Alex Encinia** aka **N3ON**
```
