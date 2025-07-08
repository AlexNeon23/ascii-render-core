from PIL import Image

def image_to_ansi(image_path, width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return

    # Redimensionar
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio * 0.5)  # Ajuste vertical para caracteres
    image = image.resize((width, new_height))

    # Convertir a RGB
    image = image.convert("RGB")

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            print(f"\033[48;2;{r};{g};{b}m ", end="")  # Fondo coloreado
        print("\033[0m")  # Reset al final de la línea

if __name__ == "__main__":
    image_to_ansi("../inputs/stupid_bread.jpg", width=80)
