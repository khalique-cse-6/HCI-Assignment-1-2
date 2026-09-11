
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def main():
    # Load image and convert to NumPy array
    img = Image.open("sample.jpeg").convert("RGB")
    img_arr = np.array(img)

    # Extract 2D intensity grids for each channel (Axis 2 slicing)
    red_channel = img_arr[:, :, 0]
    green_channel = img_arr[:, :, 1]
    blue_channel = img_arr[:, :, 2]

    # Build single-channel color images (other channels zeroed out)
    red_only = np.zeros_like(img_arr)
    red_only[:, :, 0] = red_channel

    green_only = np.zeros_like(img_arr)
    green_only[:, :, 1] = green_channel

    blue_only = np.zeros_like(img_arr)
    blue_only[:, :, 2] = blue_channel

    print("--- CHANNEL EXTRACTION SUMMARY ---")
    print(f"Original Image Shape  : {img_arr.shape}")
    print(f"Red Channel 2D Shape  : {red_channel.shape} | Mean Intensity: {red_channel.mean():.2f}")
    print(f"Green Channel 2D Shape: {green_channel.shape} | Mean Intensity: {green_channel.mean():.2f}")
    print(f"Blue Channel 2D Shape : {blue_channel.shape} | Mean Intensity: {blue_channel.mean():.2f}")

    # 2x3 subplot layout
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))

    axes[0, 0].imshow(red_only)
    axes[0, 0].set_title("Red-Only")
    axes[0, 0].axis("off")

    axes[0, 1].imshow(green_only)
    axes[0, 1].set_title("Green-Only")
    axes[0, 1].axis("off")

    axes[0, 2].imshow(blue_only)
    axes[0, 2].set_title("Blue-Only")
    axes[0, 2].axis("off")

    axes[1, 0].imshow(red_channel, cmap="gray")
    axes[1, 0].set_title("Red Grayscale")
    axes[1, 0].axis("off")

    axes[1, 1].imshow(green_channel, cmap="gray")
    axes[1, 1].set_title("Green Grayscale")
    axes[1, 1].axis("off")

    axes[1, 2].imshow(blue_channel, cmap="gray")
    axes[1, 2].set_title("Blue Grayscale")
    axes[1, 2].axis("off")

    plt.tight_layout()
    print("\nDisplay Window : Matplotlib 2x3 Subplot Grid Rendered.")
    plt.show()


if __name__ == "__main__":
    main()
