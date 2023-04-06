import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 89018174 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    s = np.std(x, ddof=1) #выборочное стандартное отклонение
    mu = np.mean(x) # выборочное среднее
    alpha = 1 - p # уровень значимости
    t = norm.ppf(1 - alpha/2) # квантиль для нормального распределения
    left = mu - t * s / np.sqrt(n)
    right = mu + t * s / np.sqrt(n)
    return (left, right)



