
import numpy as np
import matplotlib.pyplot as plt


def main():
    height, width, channels = 300, 400, 3

    # Create a blank (black) image array
    img = np.zeros((height, width, channels), dtype=np.uint8)

    mid_h = height // 2
    mid_w = width // 2

    # Top-Left: Red
    img[0:mid_h, 0:mid_w] = [255, 0, 0]
    # Top-Right: Green
    img[0:mid_h, mid_w:width] = [0, 255, 0]
    # Bottom-Left: Blue
    img[mid_h:height, 0:mid_w] = [0, 0, 255]
    # Bottom-Right: White
    img[mid_h:height, mid_w:width] = [255, 255, 255]

    print("--- SYNTHETIC MATRIX METRICS ---")
    print(f"Array Shape (H, W, C) : {img.shape}")
    print(f"Data Type             : {img.dtype}")
    print(f"Total Elements        : {img.size:,} values")
    print(f"Memory Footprint      : {img.nbytes:,} bytes ({img.nbytes / 1024:.2f} KB)")

    plt.imshow(img)
    plt.title("Synthetic Quadrant Image (300x400x3)")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
