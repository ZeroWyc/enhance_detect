import os
import shutil

# 源文件夹路径
source_folder = 'datasets/widerface/train'  # 替换为你的文件夹路径

# 目标文件夹路径
txt_folder = os.path.join('datasets/widerface/images/train')
jpg_folder = os.path.join('datasets/widerface/labels/train')

# 创建目标文件夹
os.makedirs(txt_folder, exist_ok=True)
os.makedirs(jpg_folder, exist_ok=True)

# 遍历源文件夹中的文件
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        # 移动 .txt 文件
        shutil.move(os.path.join(source_folder, filename), os.path.join(txt_folder, filename))
    elif filename.endswith('.jpg'):
        # 移动 .jpg 文件
        shutil.move(os.path.join(source_folder, filename), os.path.join(jpg_folder, filename))

print("文件分类完成！")
