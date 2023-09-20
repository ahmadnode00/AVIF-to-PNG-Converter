import av
import os

def convert_avif_to_png(input_avif, output_png):
    try:
        container = av.open(input_avif)
        for frame in container.decode(video=0):
            frame.to_image().save(output_png, 'PNG')
            print(f"Conversion successful: {input_avif} -> {output_png}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input directory for AVIF files
    input_directory = r"C:\Users\my pc\Desktop\avif_to_png"  # Use raw string literal

    # Output directory for PNG files
    output_directory = r"C:\Users\my pc\Desktop\png"  # Use raw string literal

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # List all AVIF files in the input directory
    avif_files = [f for f in os.listdir(input_directory) if f.endswith(".avif")]

    for avif_file in avif_files:
        # Generate the full path for input and output files
        input_avif_file = os.path.join(input_directory, avif_file)
        output_png_file = os.path.join(output_directory, os.path.splitext(avif_file)[0] + ".png")

        convert_avif_to_png(input_avif_file, output_png_file)

    print("All conversions completed.")


