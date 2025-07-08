import sys
from core.render import image_to_ascii_from_obj  # Importamos image_to_ascii_from_obj desde render.py
from input.input_image import load_image  # Importamos load_image desde input.py
from output.output import print_ascii, save_ascii  # Importamos las funciones desde output.py
from input.input_video import play_video_as_ascii

def image_to_ascii(image_path, width=100):
    """Convierte la imagen a arte ASCII."""
    image = load_image(image_path)  # Cargar la imagen
    if not image:  # Si no se puede cargar la imagen
        return ""
    
    ascii_art = image_to_ascii_from_obj(image, width)  # Procesar la imagen cargada
    return ascii_art

def main():
    if len(sys.argv) < 2:
        print("Uso: python app.py <ruta_imagen> [ancho] [guardar=1]")
        return

    path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) >= 3 else 100
    save_option = int(sys.argv[3]) if len(sys.argv) >= 4 else 0  # Si el tercer parámetro es '1', guarda el archivo

    image = load_image(path)  # Cargar la imagen
    if not image:  # Si no se pudo cargar la imagen
        return

    ascii_art = image_to_ascii_from_obj(image, width)  # Procesar la imagen
    print_ascii(ascii_art)  # Imprimir el resultado en consola

    if save_option == 1:  # Si el usuario quiere guardar el archivo
        import os

        output_dir = "outputs/ascii"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generar nombre de archivo limpio
        image_name = os.path.basename(path).split(".")[0]  # Extrae solo el nombre sin extensión
        filename = f"{image_name}_ascii_{width}.txt"

        # Ruta final combinando carpeta y nombre
        full_path = os.path.join(output_dir, filename)

        # Guardar el archivo
        save_ascii(ascii_art, filename=full_path)


if __name__ == "__main__":
    main()
