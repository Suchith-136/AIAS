from PIL import Image

def compress_image(input_path, output_path, quality=20):
    """
    Compresses the image at input_path and saves it as a JPEG to output_path.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image.
        quality (int): JPEG compression quality (1-95), higher is better quality.

    This function uses the Pillow library:
    https://github.com/python-pillow/Pillow (PIL Fork, BSD License)
    """
    try:
        with Image.open(input_path) as img:
            img = img.convert('RGB')  # JPEG doesn't support transparency
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            print(f"Compressed image saved to {output_path} with quality={quality}")
    except Exception as e:
        print(f"Error compressing image: {e}")

if __name__ == "__main__":
    inp_path = input("Enter path to input image: ")
    out_path = input("Enter path to save compressed image: ")
    try:
        qual = int(input("Enter compression quality (1-95, default 20): ") or "20")
    except ValueError:
        qual = 20
    compress_image(inp_path, out_path, quality=qual)



