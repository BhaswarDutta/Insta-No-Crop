# Import necessary modules
import os  # For file system operations
from PIL import Image, ImageOps  # For image manipulation using Pillow library

# Constants
BORDER = 20  # Final border width to be added around the image
BASE_DIMENSIONS = (1080, 1350)  # Instagram's 4:5 aspect ratio dimensions
INPUT_FOLDER = "image"  # Folder containing the original images
OUTPUT_FOLDER = "exports"  # Folder where processed images will be saved
SUPPORTED_FORMATS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".bmp",
    ".tiff",
)  # Supported image formats


def is_portrait(img: Image.Image) -> bool:
    """
    Determines if an image is portrait-oriented.
    Returns True if height > width, else False.
    """
    return img.height > img.width


def process_image(image_path: str, output_path: str):
    """
    Processes a single image:
    - Resizes it to fit Instagram's 4:5 aspect ratio without cropping
    - Adds white space and borders to maintain aspect ratio
    - Saves the processed image to the output folder
    """
    print(f"Processing: {image_path}")

    # Open the image
    image = Image.open(image_path)

    # Resize while preserving aspect ratio to fit within Instagram 4:5 frame
    if is_portrait(image):
        # For portrait: fit height to 1350 - BORDER
        image_height_new = BASE_DIMENSIONS[1] - BORDER
        image_width_new = int((image_height_new / image.height) * image.width)
    else:
        # For landscape or square: fit width to 1080 - BORDER
        image_width_new = BASE_DIMENSIONS[0] - BORDER
        image_height_new = int((image_width_new / image.width) * image.height)

    # Resize the image using high-quality resampling
    resized_image = image.resize(
        (image_width_new, image_height_new), Image.Resampling.LANCZOS
    )

    # Calculate white space padding to center the resized image
    if is_portrait(image):
        # Add horizontal padding for portrait orientation
        white_space = (BASE_DIMENSIONS[0] - BORDER) - resized_image.width
        padding = (white_space // 2, 0, white_space // 2, 0)
    else:
        # Add vertical padding for landscape/square
        white_space = (BASE_DIMENSIONS[1] - BORDER) - resized_image.height
        padding = (0, white_space // 2, 0, white_space // 2)

    # Add white space to center the image
    white_space_image = ImageOps.expand(resized_image, border=padding, fill="white")

    # Add the final border around the image
    border_padding = (BORDER, BORDER, BORDER, BORDER)
    final_image = ImageOps.expand(
        white_space_image, border=border_padding, fill="white"
    )

    # Save the final image
    final_image.save(output_path)
    print(f"✅ Saved: {output_path}\n")


def main():
    """
    Main function:
    - Creates output folder if it doesn't exist
    - Loops through all supported images in the input folder
    - Processes each image and saves the output
    """
    print("📂 Starting NoCrop Instagram Processing Script")
    print(f"Input folder: {INPUT_FOLDER}")
    print(f"Output folder: {OUTPUT_FOLDER}\n")

    # Create output directory if not exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Counter for summary
    total_images = 0
    errors = 0

    # Iterate through all files in the input folder
    for filename in os.listdir(INPUT_FOLDER):
        # Check if the file has a supported image format
        if filename.lower().endswith(SUPPORTED_FORMATS):
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, f"nocrop_{filename}")
            try:
                process_image(input_path, output_path)
                total_images += 1
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}\n")
                errors += 1

    print("🎉 Processing Complete!")
    print(f"Total images processed: {total_images}")
    print(f"Errors encountered: {errors}")


# Run the script if this file is executed directly
if __name__ == "__main__":
    main()
