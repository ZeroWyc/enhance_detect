import cv2
import os
import numpy as np

# 设置输入和输出文件夹路径
input_folder = '/root/autodl-tmp/facenet-retinaface-pytorch/img'
output_folder = '/root/autodl-tmp/facenet-retinaface-pytorch/lowimg'

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 降低亮度的因子 (0 到 1 之间)
factor = np.random.uniform(0.15, 0.3)
# 设置 JPEG 压缩质量 (0 到 100)
# compression_quality = np.random.randint(70, 80)
compression_quality = 90

# 遍历文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.jpg'):
        # 读取图像
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"无法读取图像: {image_path}")
            continue

        print(f"正在处理图像: {image_path}")

        # 添加高斯噪声
        mean = 0
        var = 10  # 方差值，越大噪声越强
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, image.shape).astype(np.int16)
        noisy_image = cv2.add(image.astype(np.int16), gauss)
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

        # 降低亮度
        darker_image = cv2.convertScaleAbs(noisy_image, alpha=factor, beta=0)

        # 保存图像到输出文件夹
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, darker_image, [cv2.IMWRITE_JPEG_QUALITY, compression_quality])
        print(f"图像已保存为 {output_path}")
