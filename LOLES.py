import numpy as np
import glob
from PIL import Image
img = Image.open(filename)
new_image = img.resize((1920, 1080), Image.ANTIALIAS)
new_image.save(file, 'JPEG', quality=95)
cv2_img = np.array(new_image)
img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
out.write(img)
count += 1
