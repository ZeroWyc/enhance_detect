import argparse
from ultralytics import YOLO, YOLOv10
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', default='runs/train/exp27/weights/best.pt', help='Weights path')
    parser.add_argument('--data', default='widerface.yaml', help='Path to data file')
    parser.add_argument('--device', default='0', help='CUDA device, i.e. 0 or 0,1,2,3 or cpu')
    opt = parser.parse_args()

    model = YOLO(opt.weights)
    #model = YOLOv10(opt.weights)
    # Start timing
    start_time = time.time()

    # Validate the model
    metrics = model.val(data=opt.data, device=opt.device)

    # End timing
    end_time = time.time()

    # Calculate validation duration
    total_time = end_time - start_time

    avg_time_per_image = total_time / 3221

    # Output results
    print('map50-95: ' + str(metrics.box.map))
    print('Total validation time: {:.2f} seconds'.format(total_time))
    print('Average time per image: {:.4f} seconds'.format(avg_time_per_image))