import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 89018174 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    mean_x = np.mean(x)
    std_x = np.std(x, ddof=1)
    t_alpha = t.ppf(1 - (1 - p) / 2, n - 1)
    left_bound = mean_x - t_alpha * std_x / np.sqrt(n)
    right_bound = mean_x + t_alpha * std_x / np.sqrt(n)
    return (left_bound, right_bound)


