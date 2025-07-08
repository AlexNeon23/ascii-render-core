from PIL import Image, ExifTags

def load_image(image_path):
    try:
        image = Image.open(image_path)

        # Corregir orientación basada en metadatos EXIF
        try:
            # Buscar el código del tag 'Orientation'
            for tag in ExifTags.TAGS:
                if ExifTags.TAGS[tag] == 'Orientation':
                    orientation_tag = tag
                    break

            exif = image._getexif()

            if exif is not None:
                orientation = exif.get(orientation_tag)

                if orientation == 3:
                    image = image.rotate(180, expand=True)
                elif orientation == 6:
                    image = image.rotate(270, expand=True)
                elif orientation == 8:
                    image = image.rotate(90, expand=True)

        except Exception as e:
            print(f"[WARN] No se pudo corregir la orientación EXIF: {e}")

        return image

    except Exception as e:
        print(f"[ERROR] No se pudo cargar la imagen: {e}")
        return None
