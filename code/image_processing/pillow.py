#!//Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image  # strangely, pillows is imported as `PIL'

# example data is generated from a beta distribution
example_data = np.random.beta(a=1, b=1, size=(100, 100, 3))
plt.imshow(example_data)
plt.show("hold")

# use PIL.Image to open and manipulate images
img = Image.open("path_to_image")  # opens .jpg, .gif, .png, .tif
img_size = img.size
print("image size: {}".format(img_size))
