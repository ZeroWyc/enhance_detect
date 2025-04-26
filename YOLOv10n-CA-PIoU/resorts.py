import os
import shutil

# 合并文件夹的路径
merged_folder = '/root/autodl-tmp/datasets/combined'
# 原始文件夹路径
restored_folder = '/root/autodl-tmp/datasets/data/enhancedlfw'

# 创建恢复文件夹（如果不存在）
os.makedirs(restored_folder, exist_ok=True)

# 遍历合并文件夹中的所有文件
for filename in os.listdir(merged_folder):
    file_path = os.path.join(merged_folder, filename)

    # 解析原始文件夹名
    person_folder = filename.rsplit('_', 1)[0]  # 获取文件名前面的部分作为文件夹名

    # 生成恢复后的路径
    person_path = os.path.join(restored_folder, person_folder)
    os.makedirs(person_path, exist_ok=True)

    # 将文件移动到恢复后的路径中，保持原来的文件名
    new_file_path = os.path.join(person_path, filename)
    shutil.move(file_path, new_file_path)

    print(f"已恢复 {file_path} 到 {new_file_path}")

print(f"所有文件已成功恢复到 {restored_folder}")
