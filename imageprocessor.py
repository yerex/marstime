from PIL import Image
import numpy as np

image = np.asarray(Image.open('EK_rover_path002.png'))
height, width, channels = image.shape

heightMap = []
for i in range(0,width):
    column = image[:, i, 3]
    foundAlpha = 0;
    for j in range(0,height):
        if (column[j] > 100):
            foundAlpha = j
            break

    heightMap.append (foundAlpha);
  
print(heightMap);
