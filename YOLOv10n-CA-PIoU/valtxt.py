import os

def delete_jpg_files(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以 .jpg 结尾
        if filename.endswith(".jpg"):
            # 构建完整的文件路径
            file_path = os.path.join(directory, filename)
            try:
                # 删除文件
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

# 使用示例
directory_path = '/root/autodl-tmp/yolov10/datasets/widerface/lowVal2'  # 替换为你想要删除 .jpg 文件的目录
delete_jpg_files(directory_path)
