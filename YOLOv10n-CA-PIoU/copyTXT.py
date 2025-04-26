import os
import shutil

source_folder = '../yolov10/datasets/widerface/val/'  # 源文件夹路径
destination_folder = '../yolov10/datasets/widerface/highVal2'  # 目标文件夹路径

# 创建目标文件夹（如果不存在）
os.makedirs(destination_folder, exist_ok=True)

# 遍历源文件夹中的文件
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        # 复制文件
        shutil.copy(os.path.join(source_folder, filename), destination_folder)

print("所有txt文件已复制。")
