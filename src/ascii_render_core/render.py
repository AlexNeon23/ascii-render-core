from PIL import Image

# Mapa de caracteres ASCII, del más claro al más oscuro
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
# ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '█'] 11 indices de 0 a 11
def scale_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    correction_factor = get_correction_factor(width, height)
    new_height = int(new_width * aspect_ratio * correction_factor)
    return image.resize((new_width, new_height))

def get_correction_factor(width, height):
    """
    Calcula un factor de corrección dinámico basado en la forma de la imagen.
    """
    aspect_ratio = height / width
 
    # Casos extremos: si es muy horizontal o muy vertical
    if aspect_ratio < 0.5:     # Muy apaisada
        return 0.45
    elif aspect_ratio > 2.0:   # Muy vertical
        return 0.65
    else:
        # En rango común, ajustar linealmente entre 0.5 y 0.6
        return 0.5 + (aspect_ratio - 0.5) * (0.6 - 0.5) / (2.0 - 0.5)

def convert_to_grayscale(image):
    """Convierte la imagen a escala de grises."""
    return image.convert("L")

def map_pixels_to_ascii(image):
    """Convierte cada píxel a un carácter ASCII."""
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_char = ASCII_CHARS[min(pixel_value // 25, len(ASCII_CHARS) - 1)]#correxion para evitar desbordamiento con 11vo indice
        #ascii_char = ASCII_CHARS[pixel_value // 25]  # 0-255 dividido entre 10 niveles(original)
        #ascii_char = ASCII_CHARS[pixel_value * len(ASCII_CHARS) // 256]
        #se añade precision despues de ajustar un 11 indice, haciendo un rango de 0-10
        ascii_str += ascii_char
    return ascii_str

def image_to_ascii_from_obj(image, width=100):
    """Convierte la imagen cargada en arte ASCII."""
    image = scale_image(image, new_width=width)  # Escalar la imagen
    image = convert_to_grayscale(image)  # Convertir a escala de grises
    ascii_str = map_pixels_to_ascii(image)  # Mapear a caracteres ASCII

    # Romper la cadena ASCII en líneas del ancho deseado
    pixel_count = len(ascii_str)
    ascii_image = "\n".join(ascii_str[i:i+width] for i in range(0, pixel_count, width))
    
    return ascii_image
