# output.py
def print_ascii(ascii_str):
    """Imprime el arte ASCII en consola."""
    print(ascii_str)

def save_ascii(ascii_str, filename="output.txt"):
    """Guarda el arte ASCII en un archivo de texto."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(ascii_str)
        print(f"[INFO] ASCII guardado en {filename}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")
