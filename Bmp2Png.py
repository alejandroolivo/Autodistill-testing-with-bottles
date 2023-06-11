# load every .bmp image in a folder and save it to .png woth the same name
import cv2
import os
import glob

def main():

    # Get current working directory
    HOME = os.getcwd()

    # Get the path of the data
    DATA = os.path.join(HOME, 'Data')
    IMAGES = os.path.join(DATA, 'Carne', 'Images')

    # loop through images and rename it to png
    for image_path in glob.glob(os.path.join(IMAGES, '*.jpg')):
        image = cv2.imread(image_path)
        cv2.imwrite(image_path.replace('.jpg', '.png'), image)
        # remove old image
        os.remove(image_path)

if __name__ == '__main__':
    main()

