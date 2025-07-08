import sys
import os
from src.ascii_render_core.render import image_to_ascii_from_obj
from src.ascii_render_core.input.input_image import load_image
from src.ascii_render_core.input.input_video import play_video_as_ascii
from src.ascii_render_core.output.output import print_ascii, save_ascii


def is_video_file(path):
    video_exts = [".mp4", ".mov", ".avi", ".mkv", ".webm"]
    return os.path.splitext(path)[1].lower() in video_exts


def main():
    if len(sys.argv) < 4:
        print("Uso: python -m core.app <path_imagen|video> <ancho> <modo>")
        sys.exit(1)

    input_path = sys.argv[1]
    width = int(sys.argv[2])
    mode = int(sys.argv[3])  # 0 = guardar en archivo, 1 = imprimir en consola
    

    if is_video_file(input_path):
        play_video_as_ascii(input_path, width)
    else:
        image = load_image(input_path)
        if not image:
            print("No se pudo cargar la imagen.")
            return

        ascii_art = image_to_ascii_from_obj(image, width)

        if mode == 1:
            print_ascii(ascii_art)
        else:
            output_dir = "outputs/ascii"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            image_name = os.path.basename(input_path).split(".")[0]
            filename = f"{image_name}_ascii_{width}.txt"
            full_path = os.path.join(output_dir, filename)
            save_ascii(ascii_art, filename=full_path)


if __name__ == "__main__":
    main()
