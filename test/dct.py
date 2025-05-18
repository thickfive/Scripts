# https://www.isc.meiji.ac.jp/~kikn/CDN/CDN3-JPEGb.pdf
# https://www.jianshu.com/p/b923cd47ac4a
# https://zhuanlan.zhihu.com/p/85299446

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
from datetime import datetime

# F(u, v) = C(u)C(v) * Σx Σy f(x, y) * cos[(2x+1)uπ / (2N)] * cos[(2y+1)vπ / (2N)]
# 系数的计算: x 和 y 的取值范围为 0 到 N-1, Σx Σy (C(u)C(v) * cos[(2x+1)uπ / (2N)] * cos[(2y+1)vπ / (2N)]) ^ 2 = 1
# dct
def discrete_cosine_transform(f):
    F = np.full((8, 8), 0, dtype=np.float64)
    for u in range(8):
        for v in range(8):
            cu = np.sqrt(1 / 8) if u == 0 else np.sqrt(2 / 8)
            cv = np.sqrt(1 / 8) if v == 0 else np.sqrt(2 / 8)
            sum = 0
            for x in range(8):
                for y in range(8):
                    sum += f[x, y] * cu * cv * np.cos((x + 0.5) * u * np.pi / 8) * np.cos((y + 0.5) * v * np.pi / 8)
            F[u, v] = sum
    return F

# 简写
def dct(f):
    return discrete_cosine_transform(f)

# f(x, y) = Σu Σv C(u)C(v) * F(u, v) * cos[(2x+1)uπ / (2N)] * cos[(2y+1)vπ / (2N)]
# 不同之处在于循环时 x, y 与 u, v 的顺序调换, 其他参数计算方式不变
# idct
def inverse_discrete_cosine_transform(F):
    f = np.full((8, 8), 0, dtype=np.float64)
    for x in range(8):
        for y in range(8):
            sum = 0
            for u in range(8):
                for v in range(8):
                    cu = np.sqrt(1 / 8) if u == 0 else np.sqrt(2 / 8)
                    cv = np.sqrt(1 / 8) if v == 0 else np.sqrt(2 / 8)
                    sum += F[u, v] * cu * cv * np.cos((x + 0.5) * u * np.pi / 8) * np.cos((y + 0.5) * v * np.pi / 8)
            f[x, y] = sum
    return f

# 简写
def idct(f):
    return inverse_discrete_cosine_transform(f)

# 量化表, 根据压缩程度选择不同的量化表
# https://www.researchgate.net/figure/JPEG-standard-quantization-table_fig1_331969197
quantization_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61], 
    [12, 12, 14, 19, 26, 58, 60, 55], 
    [14, 13, 16, 24, 40, 57, 69, 56], 
    [14, 17, 22, 29, 51, 87, 80, 62], 
    [18, 22, 37, 56, 68, 109, 103, 77], 
    [24, 35, 55, 64, 81, 104, 113, 92], 
    [49, 64, 78, 87, 103, 121, 120, 101], 
    [72, 92, 95, 98, 112, 100, 103, 99]
])

def quantization(F):
    return np.round(F / quantization_table)

def inverse_quantization(F):
    return np.round(F * quantization_table)

# 像素值假设已经减去 128
origin_image_8x8 = np.array([
    [11, 10, 10, 10, 10, 10, 10, 10,],
    [10, 22, 10, 10, 10, 10, 10, 10,],
    [10, 10, 33, 10, 10, 10, 10, 10,],
    [10, 10, 10, 44, 10, 10, 10, 10,],
    [10, 10, 10, 10, 10, 10, 10, 97,],
    [10, 10, 10, 10, 10, 10, 97, 98,],
    [10, 10, 10, 10, 10, 97, 98, 99,],
    [10, 10, 10, 10, 97, 98, 99, 100,]
])

# 随机数值量化之后压缩效果不好
# origin_image_8x8 = np.round(np.random.rand(8, 8) * 255) - 128

print("🟩 =====>>>>> origin image 8x8")
print(origin_image_8x8)
print("🟨 =====>>>>> dct image")
print(dct(origin_image_8x8))
print("🟩 =====>>>>> idct image 8x8")
print(idct(dct(origin_image_8x8)))
print("🟦 =====>>>>> encoded image: dct + quantization")
print(quantization(dct(origin_image_8x8)))
print("🟨 =====>>>>> inverse quantization")
print(inverse_quantization(quantization(dct(origin_image_8x8))))
print("🟩 =====>>>>> decoded image: inverse_quantization + idct")
print(idct(inverse_quantization(quantization(dct(origin_image_8x8)))))

# 模拟 jpeg 压缩/解压图片, 512x512 的图片大约需要 40s
def encode_and_decode_jpeg_image():
    image = np.array(Image.open('image.png'))
    gary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # red_gary_image = image[:, :, 0]

    image_w, image_h = gary_image.shape
    new_image = np.zeros((image_w, image_h)) # np.random.rand(image_w, image_h)

    block_size = 8
    block_h = np.split(gary_image, image_w / block_size, axis=0)
    
    print(datetime.now(), "creating new image ...")
    for i in range(len(block_h)):
        block_v = np.split(block_h[i], image_h / block_size, axis=1)
        for j in range(len(block_v)):
            block = block_v[j]
            new_block = idct(inverse_quantization(quantization(dct(block - 128.0)))) + 128.0 # 不能用整数 128, 溢出导致无法还原 
            for x in range(8):
                for y in range(8):
                    row = i * 8 + x
                    col = j * 8 + y
                    new_image[row, col] = new_block[x, y]
    print(datetime.now(), "done!")

    plt.imshow(new_image, cmap='gray')
    plt.show()

encode_and_decode_jpeg_image()

