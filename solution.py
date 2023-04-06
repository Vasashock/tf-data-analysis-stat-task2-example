import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 89018174 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    mean = x.mean()
    s = x.std(ddof=1)
    t_alpha = norm.ppf((1+p)/2, n-1)
    left = mean - t_alpha * s / np.sqrt(n)
    right = mean + t_alpha * s / np.sqrt(n)
    return left, right




