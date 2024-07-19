"""
Date: 2024/6/5 15:00
Desc: 清洗数据解决"ValueError: Out of range float values are not JSON compliant"
"""

import numpy as np
import pandas as pd


def sanitize_data(data):
    """
    递归处理数据，替换所有无效的浮点值（例如无穷大和 NaN）为 0
    """
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    elif isinstance(data, float):
        if data == float('inf') or data == float('-inf') or data != data:
            return 0.0
        return data
    else:
        return data


def sanitize_data_numpy(data):
    """
    递归处理数据，替换所有无效的浮点值（例如无穷大和 NaN）为 0
    """
    if isinstance(data, dict):
        return {k: sanitize_data_numpy(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data_numpy(item) for item in data]
    elif isinstance(data, float) or isinstance(data, np.float64):
        if data == float('inf') or data == float('-inf') or np.isnan(data):
            return 0.0
        return data
    else:
        return data


def sanitize_data_pandas(data):
    """
    递归处理数据，替换所有无效的浮点值（例如无穷大和 NaN）为 0
    """
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    elif isinstance(data, pd.DataFrame):
        data.replace([np.inf, -np.inf], np.nan, inplace=True)
        return data.fillna(0)
    elif isinstance(data, pd.Series):
        data.replace([np.inf, -np.inf], np.nan, inplace=True)
        return data.fillna(0)
    elif isinstance(data, float) or isinstance(data, np.float64):
        if np.isinf(data) or np.isnan(data):
            return 0.0
        return data
    else:
        return data
