import os
import cv2  # OpenCV for reading image dimensions

def convert_to_yolo_format(bbox, img_width, img_height):
    x_min, y_min, x_max, y_max = bbox
    x_center = (x_min + x_max) / 2 / img_width
    y_center = (y_min + y_max) / 2 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height
    return f"0 {x_center:.4f} {y_center:.4f} {width:.4f} {height:.4f}"

def process_txt_file(input_path, image_path, output_path):
    # Read the image to get its dimensions
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Image not found at {image_path}")
        return
    img_height, img_width = image.shape[:2]  # Get the image dimensions

    with open(input_path, 'r') as file:
        lines = file.readlines()

    # The first line represents the number of faces, which we can ignore
    face_count = int(lines[0].strip())
    processed_lines = []

    for line in lines[1:]:
        bbox = list(map(int, line.strip().split()))
        yolo_format_bbox = convert_to_yolo_format(bbox, img_width, img_height)
        processed_lines.append(yolo_format_bbox)

    # Write the processed content to a new YOLO format .txt file
    with open(output_path, 'w') as file:
        for line in processed_lines:
            file.write(f"{line}\n")

def process_txt_files_in_folder(input_folder, image_folder, output_folder):
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            image_path = os.path.join(image_folder, filename.replace('.txt', '.png'))  # Match .txt and .png
            output_path = os.path.join(output_folder, filename)  # Output same .txt filename in YOLO format
            process_txt_file(input_path, image_path, output_path)
            print(f"Processed {filename}")

# Set your folder paths
input_folder = "/path/to/input/txt/folder"
image_folder = "/path/to/images/folder"
output_folder = "/path/to/output/folder"

# Run the function to process all .txt files in the folder
process_txt_files_in_folder(input_folder, image_folder, output_folder)


# import os
# import shutil
#
# # Set the source and destination folder paths
# source_folder = '/root/autodl-tmp/yolov10/datasets/DarkFace_Train_2021'  # Replace with your source folder path
# destination_folder = '/root/autodl-tmp/yolov10/datasets/darkface'  # Replace with your destination folder path
#
# # Create the destination folder if it doesn't exist
# os.makedirs(destination_folder, exist_ok=True)
#
# # Iterate over all files in the source folder
# for filename in os.listdir(source_folder):
#     if filename.endswith('.png'):  # Only process .png files
#         source_path = os.path.join(source_folder, filename)
#         destination_path = os.path.join(destination_folder, filename)
#
#         # Copy the .png file to the destination folder
#         shutil.copy(source_path, destination_path)
#         print(f"Copied {filename} to {destination_folder}")
#
# print("All .png files have been copied successfully.")
