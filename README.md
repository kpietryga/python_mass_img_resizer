
# Image Resizer

This Python program scales images to a specified width while maintaining their aspect ratio. It processes all images in the `input/` folder and saves the scaled images in the `output/` folder.

## Requirements

- Python 3.x
- Pillow library

You can install the necessary libraries by running:
```bash
pip install pillow
```

## How to Use

1. Place the images you want to scale in the `input/` folder.
2. Run the script.
3. When prompted, specify the width to which you want to scale the images. The program will automatically adjust the height to maintain the aspect ratio.
4. The scaled images will be saved in the `output/` folder with the specified width included in their filenames.

### Example:
```
Please specify the width to which you want to scale the images:
640
```

## Example Output

After the process completes, you will see the scaled images in the `output/` folder, with their filenames reflecting the specified width.

## Process Flow

- The script loops through all images in the `input/` folder.
- For each image, it scales the width to the user-defined value while maintaining the original aspect ratio.
- The output images are saved in the `output/` folder, with filenames that include the new width.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
