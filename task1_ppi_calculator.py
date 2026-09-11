

import math


def main():
    w_px = int(input("Enter horizontal resolution (pixels) : "))
    h_px = int(input("Enter vertical resolution (pixels) : "))
    d_inches = float(input("Enter physical diagonal size (inches) : "))

    # Total pixel count
    total_pixels = w_px * h_px

    # Simplified aspect ratio using GCD
    divisor = math.gcd(w_px, h_px)
    aspect_w = w_px // divisor
    aspect_h = h_px // divisor

    # Diagonal pixel count and DPI/PPI
    diagonal_px = math.sqrt(w_px ** 2 + h_px ** 2)
    dpi = diagonal_px / d_inches

    # Classify density
    if dpi < 100:
        category = "Low Density (Standard Monitor)"
    elif dpi <= 200:
        category = "Medium Density (HD Display)"
    else:
        category = "High Density (Retina / Mobile)"

    print("\n--- DISPLAY METRICS ANALYSIS ---")
    print(f"Total Pixel Count  : {total_pixels:,} pixels")
    print(f"Aspect Ratio       : {aspect_w}:{aspect_h}")
    print(f"Calculated DPI     : {dpi:.2f} DPI")
    print(f"Density Category   : {category}")


if __name__ == "__main__":
    main()
