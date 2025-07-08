import os
import cv2
from PIL import Image
import time
from ascii_render_core.render import image_to_ascii_from_obj

def play_video_as_ascii(video_path, width=100, fps_limit=30):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("[ERROR] No se pudo abrir el archivo de video.")
        return

    frame_delay = 1 / fps_limit
    # 1 = 30 FPS :)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Convertimos el frame (BGR) a RGB para que lo entienda PIL
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame_rgb)
            
            ascii_frame = image_to_ascii_from_obj(image, width=width)
            print("\033c", end="")  # Limpiar la consola
            print(ascii_frame)
            time.sleep(frame_delay)

    except KeyboardInterrupt:
        print("\n[INFO] Reproducción interrumpida por el usuario.")

    finally:
        cap.release()
