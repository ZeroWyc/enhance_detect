
import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLOv10
from ultralytics import YOLO

if __name__ == '__main__':
    # model.load('yolov8n.pt') # 加载预训练权重,改进或者做对比实验时候不建议打开，因为用预训练模型整体精度没有很明显的提升
    model = YOLO(model=r'ultralytics/cfg/models/v8/yolov8-CA200.yaml')
    model.train(data=r'widerface.yaml',
                imgsz=640,
                epochs=200,
                batch=8,
                workers=16,
                device='0',
                optimizer='SGD',
                close_mosaic=10,
                resume=False,
                project='runs/train',
                name='exp',
                single_cls=False,
                cache=False,
                )
