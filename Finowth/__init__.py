__version__ = "1.14.58"
__author__ = "AKFamily"

import sys
import warnings

import pandas as pd

pd_main_version = int(pd.__version__.split('.')[0])

if pd_main_version < 2:
    warnings.warn(
        "为了支持更多特性，请将 Pandas 升级到 2.2.0 及以上版本！"
    )

if sys.version_info < (3, 9):
    warnings.warn(
        "为了支持更多特性，请将 Python 升级到 3.9.0 及以上版本！"
    )

del sys

"""
新闻-新闻联播
"""
from Finowth.finowth_data.news.xinwenlianbo import news_xinwenlianbo_text
