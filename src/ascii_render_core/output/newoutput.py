import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from core.render import image_to_ascii_from_obj


def ascii_to_image(ascii_str, font_size=10, bg_color="black", fg_color="white"):
    """Convierte arte ASCII a una imagen PIL."""
    lines = ascii_str.split("\n")
    font = ImageFont.load_default()

    width = max([len(line) for line in lines]) * font_size // 2
    height = len(lines) * font_size

    image = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)

    y = 0
    for line in lines:
        draw.text((0, y), line, font=font, fill=fg_color)
        y += font_size

    return image


def save_ascii_video(video_path, output_path="ascii_video.avi", width=120):
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] No se pudo leer el video.")
        return

    # Procesamos el primer frame para definir tamaño del frame de salida
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    ascii_str = image_to_ascii_from_obj(pil_image, width)
    ascii_img = ascii_to_image(ascii_str)

    frame_size = ascii_img.size[::-1]  # PIL usa (width, height), OpenCV usa (height, width)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    frame_count = 0
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Volvemos al primer frame

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        ascii_str = image_to_ascii_from_obj(pil_image, width)
        ascii_img = ascii_to_image(ascii_str)

        # Convertimos la imagen PIL a formato que OpenCV entiende
        frame_bgr = cv2.cvtColor(np.array(ascii_img), cv2.COLOR_RGB2BGR)
        out.write(frame_bgr)

        frame_count += 1
        print(f"\rProcesando frame {frame_count}...", end="")

    cap.release()
    out.release()
    print(f"\n[INFO] Video guardado como '{output_path}'")
