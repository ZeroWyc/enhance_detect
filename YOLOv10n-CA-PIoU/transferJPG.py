from PIL import Image
import os


# Function to convert .webp files to .jpg
def convert_webp_to_jpg(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            webp_path = os.path.join(input_folder, filename)
            jpg_filename = filename.replace('.webp', '.jpg')
            jpg_path = os.path.join(output_folder, jpg_filename)

            # Open and convert the image
            with Image.open(webp_path) as img:
                img = img.convert("RGB")
                img.save(jpg_path, "JPEG")
                print(f"Converted {filename} to {jpg_filename}")


# Set your folder paths
input_folder = "/root/autodl-tmp/yolov10/datasets/newdataset/TEST"  # Replace with your actual input folder path
output_folder = "/root/autodl-tmp/yolov10/datasets/newdataset/TEST"  # Replace with your actual output folder path

# Run the conversion function
convert_webp_to_jpg(input_folder, output_folder)

