import argparse
from ultralytics import YOLO
from ultralytics import YOLOv10
import time
import os
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='./runs/train/exp24/weights/best.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='./ultralytics/assets/h.jpg', help='source')
    parser.add_argument('--img-size', nargs='+', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.6, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--save-img', action='store_true', help='save results')
    parser.add_argument('--save-txt', action='store_true', help='save txt results')  # 添加保存txt文件的参数
    parser.add_argument('--save-dir', type=str, default='./runs/val/exp/', help='directory to save results')  # 添加保存路径参数
    opt = parser.parse_args()

    # 如果 save_dir 不存在，则创建
    if not os.path.exists(opt.save_dir):
        os.makedirs(opt.save_dir)

    model = YOLOv10(opt.weights)
    # 记录推理开始时间
    start_time = time.time()
    model.predict(
        source=opt.source,
        imgsz=opt.img_size,
        conf=opt.conf_thres,
        iou=opt.iou_thres,
        device=opt.device,
        save=opt.save_img,
        save_txt=opt.save_txt,  # 启用保存txt
        save_dir=opt.save_dir  # 指定保存路径
    )

    # 记录推理结束时间
    end_time = time.time()

    # 计算推理时间
    inference_time = end_time - start_time
    print(f"Inference Time: {inference_time * 1000:.2f} ms")