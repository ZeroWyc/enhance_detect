
import os
import shutil

# 设置输入和输出文件夹路径
input_folder = '/root/autodl-tmp/datasets/data/lowlfw'
output_folder = '/root/autodl-tmp/datasets/data/combine' # 合并后的文件夹

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的每个子文件夹
for person_folder in os.listdir(input_folder):
    person_path = os.path.join(input_folder, person_folder)

    # 确保只处理文件夹
    if os.path.isdir(person_path):
        # 遍历每个文件夹中的图片
        for filename in os.listdir(person_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # 构建新的文件名：person1_image1.jpg, person2_image2.jpg
                new_filename = f"{filename}"
                new_file_path = os.path.join(output_folder, new_filename)

                # 复制文件到输出文件夹
                shutil.copy(os.path.join(person_path, filename), new_file_path)

                print(f"已复制 {filename} 到 {new_file_path}")

print(f"所有文件已成功合并到 {output_folder}")

