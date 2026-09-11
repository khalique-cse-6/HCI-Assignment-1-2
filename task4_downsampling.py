
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def main():
    N = 8  # Step factor

    # Load image and convert to NumPy array
    img = Image.open("sample.jpeg").convert("RGB")
    original = np.array(img)

    # Downsample using striding: take every N-th pixel along rows/cols
    downsampled = original[::N, ::N, :]

    # Re-expand back to original dimensions using np.repeat on axes 0 and 1
    re_expanded = np.repeat(downsampled, N, axis=0)
    re_expanded = np.repeat(re_expanded, N, axis=1)

    # Trim/pad re-expanded array in case dimensions don't divide evenly
    re_expanded = re_expanded[: original.shape[0], : original.shape[1], :]

    # Metrics
    orig_shape = original.shape
    down_shape = downsampled.shape
    orig_mem = original.nbytes
    down_mem = downsampled.nbytes

    dim_reduction = (1 - (down_shape[0] * down_shape[1]) / (orig_shape[0] * orig_shape[1])) ** 0.5
    # Percentage reduction per axis (rows and cols each reduced by same factor N)
    dim_reduction_per_axis = (1 - (1 / N)) * 100
    mem_savings = (1 - down_mem / orig_mem) * 100

    print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
    print(f"Original Shape      : {orig_shape} | Memory: {orig_mem:,} bytes")
    print(f"Downsampled Shape   : {down_shape} | Memory: {down_mem:,} bytes")
    print(f"Re-expanded Shape   : {re_expanded.shape} | Visual: Blocky Pixelation")
    print(f"Dimension Reduction : {dim_reduction_per_axis:.2f}% reduction per axis")
    print(f"Memory Savings      : {mem_savings:.2f}% data reduction")

    # Show original vs pixelated result
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(re_expanded)
    axes[1].set_title(f"Pixelated (N={N})")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
