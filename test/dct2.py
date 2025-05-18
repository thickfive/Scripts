import numpy as np

def dct(x):
    """
    Compute 1D Discrete Cosine Transform (DCT-II) with scaled coefficients.
    """
    N = len(x)
    X = np.zeros(N)
    a = 2.0  # 缩放因子
    for k in range(N):
        sum_result = 0.0
        for n in range(N):
            sum_result += x[n] * np.cos(np.pi * (2 * n + 1) * k / (2 * N))
        coeff = a * np.sqrt(1 / N) if k == 0 else a * np.sqrt(2 / N)
        X[k] = sum_result * coeff
    return X

def idct(X):
    """
    Compute 1D Inverse Discrete Cosine Transform (IDCT-II) with scaled coefficients.
    """
    N = len(X)
    x = np.zeros(N)
    a = 2.0  # DCT 使用的缩放因子. 也就是说系数可以调整, 保证和 DCT 使用的缩放因子相乘之后不变即可
    for n in range(N):
        sum_result = 0.0
        for k in range(N):
            coeff = (1/a) * np.sqrt(1 / N) if k == 0 else (1/a) * np.sqrt(2 / N)
            sum_result += coeff * X[k] * np.cos(np.pi * (2 * n + 1) * k / (2 * N))
        x[n] = sum_result
    return x

# 测试可逆性
x = np.array([1.0, 2.0, 3.0, 4.0])
X = dct(x)
x_reconstructed = idct(X)
print("原始信号:", x)
print("重构信号:", x_reconstructed)
print("是否可逆:", np.allclose(x, x_reconstructed))