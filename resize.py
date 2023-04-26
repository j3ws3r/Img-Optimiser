import sys
import cv2
import os
from PIL import Image

def optimize_image(image_path, output_path, scale_percent, quality):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not read image: {image_path}")
        return

    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)

    resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_CUBIC)

    pil_image = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

    pil_image.save(output_path, quality=quality)
    print(f"Optimized image saved at {output_path}")




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python image_resizer.py <image_path> [output_path] [scale_percent] [quality]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "optimized_" + os.path.basename(image_path)
    scale_percent = float(sys.argv[3]) if len(sys.argv) > 3 else 50.0
    quality = int(sys.argv[4]) if len(sys.argv) > 4 else 95

    optimize_image(image_path, output_path, scale_percent, quality)

