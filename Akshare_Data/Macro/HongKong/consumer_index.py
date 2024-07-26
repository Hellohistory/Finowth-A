import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 中国香港-消费者指数-消费者物价指数
@router.get("/macro_china_hk_cpi",
            operation_id="get_macro_china_hk_cpi")
async def get_macro_china_hk_cpi():
    """
    中国香港-消费者指数-消费者物价指数

    接口: macro_china_hk_cpi

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_0.html

    描述: 东方财富-经济数据一览-中国香港-消费者物价指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_cpi = ak.macro_china_hk_cpi()
        macro_china_hk_cpi_df = sanitize_data_pandas(macro_china_hk_cpi)
        return macro_china_hk_cpi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 中国香港-消费者指数-消费者物价指数年率
@router.get("/macro_china_hk_cpi_ratio",
            operation_id="get_macro_china_hk_cpi_ratio")
async def get_macro_china_hk_cpi_ratio():
    """
    中国香港-消费者指数-消费者物价指数年率

    接口: macro_china_hk_cpi

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_0.html

    描述: 东方财富-经济数据一览-中国香港-消费者物价指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_cpi_ratio = ak.macro_china_hk_cpi_ratio()
        macro_china_hk_cpi_ratio_df = sanitize_data_pandas(macro_china_hk_cpi_ratio)
        return macro_china_hk_cpi_ratio_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



