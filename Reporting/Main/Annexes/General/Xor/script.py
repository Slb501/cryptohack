#!/usr/bin/python3

from PIL import Image
import sys
from io import BytesIO

def get_rgb_bytes(png_path):
    with Image.open(png_path) as img:
        img = img.convert('RGB')
        return img.tobytes()

lemur = get_rgb_bytes("lemur_ed66878c338e662d3473f0d98eedbd0d.png")
flag = get_rgb_bytes("flag_7ae18c704272532658c10b5faad06d74.png")

xored_result = []
for i, c in enumerate(lemur):
    xored_byte = c ^ flag[i % len(flag)]
    xored_result.append(xored_byte)

with Image.open("lemur_ed66878c338e662d3473f0d98eedbd0d.png") as img:
    width, height = img.size

result_img = Image.frombytes('RGB', (width, height), bytes(xored_result))
result_img.save("xored_result.png")