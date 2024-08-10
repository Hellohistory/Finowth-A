"""
FileName: utility_function.py
Date: 2024/7/23
Desc: 清洗数据解决"ValueError: Out of range float values are not JSON compliant"
"""
from typing import Dict, List

import numpy as np
import pandas as pd

pd.set_option('future.no_silent_downcasting', True)


def sanitize_data(data):
    """
    递归处理数据，替换所有无效的浮点值（无穷大和 NaN）为 0.0，并将字符串 'null' 替换为 0.0
    """
    if isinstance(data, pd.DataFrame):
        data = data.replace([np.inf, -np.inf, 'null'], np.nan)
        data = data.fillna(0.0)
        return data
    elif isinstance(data, pd.Series):
        data = data.replace([np.inf, -np.inf, 'null'], np.nan)
        data = data.fillna(0.0)
        return data
    elif isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    elif isinstance(data, (float, np.float64)):
        if np.isinf(data) or np.isnan(data):
            return 0.0
        return data
    elif isinstance(data, (int, np.int64)):
        return data
    elif isinstance(data, str) and data == 'null':
        return 0.0
    else:
        return data


def sanitize_data_pandas(data):
    """
    递归处理数据，替换所有无效的浮点值（无穷大、NaN 和 0.0）为 'null'
    """
    if isinstance(data, dict):
        return {k: sanitize_data_pandas(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data_pandas(item) for item in data]
    elif isinstance(data, pd.DataFrame):
        data.replace([np.inf, -np.inf, 0.0], 'null', inplace=True)
        data = data.map(lambda x: 'null' if pd.isna(x) or x == 0.0 else x)
        return data
    elif isinstance(data, pd.Series):
        data.replace([np.inf, -np.inf, 0.0], 'null', inplace=True)
        data = data.map(lambda x: 'null' if pd.isna(x) or x == 0.0 else x)
        return data
    elif isinstance(data, (float, np.float64, int, np.int64)):
        if np.isinf(data) or np.isnan(data) or data == 0.0:
            return 'null'
        return data
    else:
        return data


def common_transform(raw_data: pd.DataFrame, columns_mapping: Dict[str, str]) -> List[dict]:
    raw_data.rename(columns=columns_mapping, inplace=True)
    for col in columns_mapping.values():
        if raw_data[col].dtype == 'object':
            raw_data[col] = pd.to_datetime(raw_data[col], errors='coerce').dt.date
    return raw_data.replace({0.0: 'null'}).to_dict(orient="records")
