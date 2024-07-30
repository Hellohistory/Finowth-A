import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-期权波动率指数-50ETF 期权波动率指数
@router.get("/index_option_50etf_qvix",
            operation_id="get_index_option_50etf_qvix")
def get_index_option_50etf_qvix():
    """
    指数数据-期权波动率指数-50ETF 期权波动率指数

    接口: index_option_50etf_qvix

    目标地址: http://1.optbbs.com/s/vix.shtml?50ETF

    描述: 50ETF 期权波动率指数 QVIX; 又称中国版的恐慌指数

    限量: 单次返回所有数据
    """
    try:
        index_option_50etf_qvix = ak.index_option_50etf_qvix()
        data = index_option_50etf_qvix.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-期权波动率指数-50ETF 期权波动率指数-分时
@router.get("/index_option_50etf_min_qvix",
            operation_id="get_index_option_50etf_min_qvix")
def get_index_option_50etf_min_qvix():
    """
    指数数据-期权波动率指数-50ETF 期权波动率指数-分时

    接口: index_option_50etf_min_qvix

    目标地址: http://1.optbbs.com/s/vix.shtml?50ETF

    描述: 50ETF 期权波动率指数-分时

    限量: 单次返回最近交易日的分时数据
    """
    try:
        index_option_50etf_min_qvix = ak.index_option_50etf_min_qvix()
        data = index_option_50etf_min_qvix.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-期权波动率指数-300ETF 期权波动率指数
@router.get("/index_option_300etf_qvix",
            operation_id="get_index_option_300etf_qvix")
def get_index_option_300etf_qvix():
    """
    指数数据-期权波动率指数-300ETF 期权波动率指数

    接口: index_option_300etf_qvix

    目标地址: https://1.optbbs.com/s/vix.shtml?300ETF

    描述: 300ETF 期权波动率指数 QVIX

    限量: 单次返回所有数据
    """
    try:
        index_option_300etf_qvix = ak.index_option_300etf_qvix()
        data = index_option_300etf_qvix.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-期权波动率指数-300ETF 期权波动率指数-分时
@router.get("/index_option_300etf_min_qvix",
            operation_id="get_index_option_300etf_min_qvix")
def get_index_option_300etf_min_qvix():
    """
    指数数据-期权波动率指数-300ETF 期权波动率指数-分时

    接口: index_option_300etf_min_qvix

    目标地址: https://1.optbbs.com/s/vix.shtml?300ETF

    描述: 300ETF 期权波动率指数-分时

    限量: 单次返回最近交易日的分时数据
    """
    try:
        index_option_300etf_min_qvix = ak.index_option_300etf_min_qvix()
        data = index_option_300etf_min_qvix.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
