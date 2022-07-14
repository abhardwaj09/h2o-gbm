import random
import os
from PIL import Image
import numpy as np

path = './images_copy/nine'


for filename in os.listdir(path):
    if filename.endswith('.png'):
        current_im = path + f'/{filename}'
        im = np.array(Image.open(current_im).convert('L'))
        row, col = im.shape # 28, 28
        random_num = random.randint(0, 78) 
        new_im = im.copy()
        for i in range(random_num): # randoml
            y_bl = random.randint(0, row -1) 
            x_bl = random.randint(0, col -1)
            y_wh = random.randint(0, row -1) 
            x_wh = random.randint(0, col -1)
            new_im[y_wh][x_wh] = 255
            new_im[y_bl][x_bl] = 0

        new_im = Image.fromarray(new_im)

        new_im.save(os.path.join(path, f"{filename}_new.png"))

print("exec...")
