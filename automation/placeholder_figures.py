#!/usr/bin/env python3
import argparse
import os
import sys
import yaml
from PIL import Image, ImageDraw, ImageFont


def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Create placeholder figures")
    parser.add_argument(
        "--config", help="Specify YAML file containing results config", required=True
    )
    return parser.parse_args()


def load_config(filename: str) -> dict:
    with open(filename, "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config


def list_non_existent_images(paths: list, ext: list) -> list:
    # Check paths that end in one of the extensions in ext
    to_create = []
    for path in paths:
        if any(path.endswith(e) for e in ext):
            if not os.path.exists(path):
                to_create.append(path)
    return to_create


def create_placeholder_image(path):
    # Create a new image with light grey background
    img = Image.new("RGB", (668, 486), color="grey")

    # Write 'Placeholder' in the center of the image
    try:
        fnt = ImageFont.truetype("paper/config/latinmodern-math.otf", 40)
        d = ImageDraw.Draw(img)
        d.text((230, 200), "Placeholder", font=fnt, fill=(0, 0, 0))
    except:
        pass

    # Output
    img.save(path)
    print(f"Created placeholder image {path}")


def main() -> int:
    args = parse_args()
    config = load_config(args.config)

    if config.get("results_created_files"):
        to_create = list_non_existent_images(
            paths=config["results_created_files"], ext=[".png"]
        )

        for path in to_create:
            create_placeholder_image(path)
    else:
        print("No placeholder figures to create.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
