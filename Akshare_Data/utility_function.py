"""
Date: 2024/7/23
Desc: 清洗数据解决"ValueError: Out of range float values are not JSON compliant"
"""

import numpy as np
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)


def sanitize_data_pandas(data):
    """
    递归处理数据，替换所有无效的浮点值（无穷大和 NaN）为 'null'
    """
    if isinstance(data, dict):
        return {k: sanitize_data_pandas(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data_pandas(item) for item in data]
    elif isinstance(data, pd.DataFrame):
        # 替换无效值为 'null'，并使用 fillna 处理 NaN
        data.replace([np.inf, -np.inf], 'null', inplace=True)
        return data.fillna('null')
    elif isinstance(data, pd.Series):
        # 替换无效值为 'null'，并使用 fillna 处理 NaN
        data.replace([np.inf, -np.inf], 'null', inplace=True)
        return data.fillna('null')
    elif isinstance(data, float) or isinstance(data, np.float64):
        if np.isinf(data) or np.isnan(data):
            return 'null'
        return data
    else:
        return data
