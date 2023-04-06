import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 89018174 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    sample_mean = np.mean(x)
    sample_std = np.std(x)/(n**0.5)
    z_alpha_2 = norm.ppf(1 - (1 - p)/2)
    left_bound = sample_mean - z_alpha_2 * sample_std
    right_bound = sample_mean + z_alpha_2 * sample_std
    return (left_bound, right_bound)

