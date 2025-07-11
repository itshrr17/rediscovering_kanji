# convert svg to png
import cairosvg
import os
import shutil
import sys
import cv2
import numpy as np
from tqdm import tqdm
    

# note output width and height is hard-coded, change according to your needs
def convert_svg2png(input, output):
  if not os.path.exists(input):
    print('invalid input path')
    return

  if os.path.exists(output):
    shutil.rmtree(output)

  os.makedirs(output)

  file_names = os.listdir(input)

  print(f'\nStarting to process {input} -> {output}')

  for file_name in tqdm(file_names):
    file_name_without_extension = file_name.split('.')[0]
    full_path_input = os.path.join(input, file_name)
    full_path_output = os.path.join(output, file_name_without_extension + '.png')

    if os.path.exists(full_path_output):
      os.remove(full_path_output)
    
    png_bytes = cairosvg.svg2png(url=full_path_input, output_width=224, output_height=224)
    img_array = np.frombuffer(png_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)

    # end of conversion from svg to png

    binary = None

    # starting to grayscale
    if img.shape[2] == 4:
        alpha = img[:, :, 3]
        gray = cv2.cvtColor(img[:, :, :3], cv2.COLOR_BGR2GRAY)
        mask = (gray < 128) & (alpha > 0)
        binary = np.zeros_like(gray, dtype=np.uint8)
        binary[mask] = 255
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite(full_path_output, binary)