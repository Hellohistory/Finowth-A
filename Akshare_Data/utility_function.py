"""
Date: 2024/7/23
Desc: 清洗数据解决"ValueError: Out of range float values are not JSON compliant"
"""

import numpy as np
import pandas as pd


def sanitize_data(data):
    """
    递归处理数据，替换所有无效的浮点值（例：无穷大和 NaN）为 'null'
    """
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    elif isinstance(data, float):
        if np.isinf(data) or np.isnan(data):
            return 'null'
        return data
    else:
        return data


def sanitize_data_pandas(data):
    """
    递归处理数据，替换所有无效的浮点值（例：无穷大和 NaN）为 'null'
    """
    if isinstance(data, dict):
        return {k: sanitize_data_pandas(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data_pandas(item) for item in data]
    elif isinstance(data, pd.DataFrame):
        data.replace([np.inf, -np.inf], 'null', inplace=True)
        return data.fillna('null')
    elif isinstance(data, pd.Series):
        data.replace([np.inf, -np.inf], 'null', inplace=True)
        return data.fillna('null')
    elif isinstance(data, float) or isinstance(data, np.float64):
        if np.isinf(data) or np.isnan(data):
            return 'null'
        return data
    else:
        return data
