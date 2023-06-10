import cv2
import os
import torch
from PIL import Image
from ultralytics import YOLO

def main():

    # Get current working directory
    HOME = os.getcwd()

    # Get the path of the data
    DATA = os.path.join(HOME, 'Data')
    IMAGES = os.path.join(DATA, 'Bottles', 'Images')

    # image_path
    image_path = os.path.join(IMAGES, 'Bottle (1).png')

    # select device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # set threshold
    threshold = 0.1

    # load a pretrained model (recommended for best training results)
    model = YOLO('yolov8n.pt')
    model.to(device)

    # predict on an image
    results = model.predict(image_path)   

    # read image
    image = cv2.imread(image_path)

    # loop through results
    for result in results[0].cpu().numpy():
        x1, y1, x2, y2 = map(int, result.boxes[0].xyxy[0])

        # if score is greater than threshold
        if True:

            # draw bounding box
            color = (255, 0, 0)
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
    
    # plot image
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # print results
    print(results)
    

if __name__ == '__main__':
    main()
