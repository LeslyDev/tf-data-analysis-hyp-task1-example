from statsmodels.stats.proportion import proportions_ztest
import numpy as np


chat_id = 623406448 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.03
    t_stat, p_value = proportions_ztest(np.array([x_success, y_success]), np.array([x_cnt, y_cnt]))
    
    if p_value < alpha:
      return True
    else:
      return False
