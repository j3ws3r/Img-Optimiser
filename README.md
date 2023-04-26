# Img-Optimiser

The script uses the INTER_CUBIC interpolation method for resizing, which provides better quality than INTER_AREA. The default image quality is set to 95, which balances file size and image quality. Run the script with the new quality parameter:

python resize.py input_image.jpg output_image.jpg 50 95

This will resize input_image.jpg to 50% of its original size and save the result as output_image.jpg with a high-quality setting.
