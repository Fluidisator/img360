import glob
import os
import argparse

from img360_transformer.batch_process import process_image
from img360_transformer.gui import launch_ui


def main():
    parser = argparse.ArgumentParser(description="Horizon correcter")

    parser.add_argument('--pitch', '-p', type=float, help="Pitch correction to apply to the picture")
    parser.add_argument('--roll', '-r', type=float, help="Roll correction to apply to the picture")
    parser.add_argument('--yaw', '-y', type=float, help="Yaw correction to apply to the picture")    
    parser.add_argument('--quality', '-q', type=int, choices=range(0,101), default=95, help="Quality value to save a jpeg picture, integer from 0 to 100")
    parser.add_argument('--compression', '-c', type=int, choices=range(0,11), default=1, help="Compression value to save a png picture, integer from 0 to 10")
    parser.add_argument('--list_of_pictures', '-l', type=str, nargs='+', help="Path to the picture or list of path")
    
    args=parser.parse_args()
    
    GUI = False  #Variable to either use the GUI or not

    pitch = args.pitch
    if pitch is None:
        GUI = True
    roll = args.roll
    if roll is None:
        GUI = True
    yaw = args.yaw
    if yaw is None:
        GUI = True
    quality = args.quality
    compression = args.compression
    image_patterns = args.list_of_pictures

    image_paths = []
    for pattern in image_patterns:
        image_paths.extend(glob.glob(pattern))
    
    #Check if there is any picture to open
    if len(image_paths)>0:
        if GUI:
            print("Will open the GUI on the first picture")
            launch_ui(image_paths[0])
        else:
            for image_path in image_paths:
                process_image(image_path, pitch, yaw, roll, quality, compression)
    else:
        print("No picture found!")

if __name__ == "__main__":
    main()
