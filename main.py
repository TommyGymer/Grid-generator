from PIL import Image
import numpy as np

def safe_int_input(req):
    try:
        return int(input(req))
    except:
        return None

w, h = safe_int_input("Enter the width: ") or 1920, safe_int_input("Enter the height: ") or 1080
r, g, b = safe_int_input("Enter the background r value: ") or 255, safe_int_input("Enter the background g value: ") or 255, safe_int_input("Enter the background b value: ") or 255
data = np.full((h, w, 3), [r,g,b], dtype=np.uint8)
gap = safe_int_input("Enter the gap: ") or 64
r, g, b = safe_int_input("Enter the grid r value: ") or 0, safe_int_input("Enter the grid g value: ") or 0, safe_int_input("Enter the grid b value: ") or 0
data[::gap, 0::] = [r,g,b]
data[0::, ::gap] = [r,g,b]
img = Image.fromarray(data, 'RGB')
img.show()