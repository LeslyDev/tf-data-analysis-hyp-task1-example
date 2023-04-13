import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 623406448 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    control = [x_success / x_cnt]
    test = [y_success / y_cnt]
    alpha = 0.03
    t_stat, p_value = stats.ttest_ind(control, test)
    
    if p_value < alpha:
      return True
    else:
      return False
