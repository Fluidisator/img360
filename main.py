import glob
import argparse

from img360_transformer.batch_process import process_image
from img360_transformer.gui import launch_ui


def _get_parser():
    parser = argparse.ArgumentParser(description="Horizon correcter")

    parser.add_argument(
        "--pitch", "-p", type=float, help="Pitch correction to apply to the picture"
    )
    parser.add_argument(
        "--roll", "-r", type=float, help="Roll correction to apply to the picture"
    )
    parser.add_argument(
        "--yaw", "-y", type=float, help="Yaw correction to apply to the picture"
    )
    parser.add_argument(
        "--quality",
        "-q",
        type=int,
        choices=range(0, 101),
        default=95,
        help="Quality value to save a jpeg picture, integer from 0 to 100",
    )
    parser.add_argument(
        "--compression",
        "-c",
        type=int,
        choices=range(0, 11),
        default=1,
        help="Compression value to save a png picture, integer from 0 to 10",
    )
    parser.add_argument(
        "--pictures",
        "-i",
        type=str,
        nargs="+",
        help="Path to the picture or list of path",
    )
    return parser


def main():
    args = _get_parser().parse_args()

    if not args.pictures:
        print("No picture provided!")
        return

    should_display_gui = None in (args.pitch, args.roll, args.yaw)

    image_paths = []
    for pattern in args.pictures:
        image_paths.extend(glob.glob(pattern))

    # Check if there is any picture to open
    if len(image_paths) > 0:
        if should_display_gui:
            print("Will open the GUI on the first picture")
            launch_ui(image_paths[0])
        else:
            for image_path in image_paths:
                process_image(
                    image_path,
                    args.pitch,
                    args.yaw,
                    args.roll,
                    args.quality,
                    args.compression,
                )
    else:
        print("No picture found!")


if __name__ == "__main__":
    main()
