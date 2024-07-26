import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 中国香港-GDP指数-GDP
@router.get("/macro_china_hk_gbp",
            operation_id="get_macro_china_hk_gbp")
async def get_macro_china_hk_gbp():
    """
    中国香港-GDP指数-GDP

    接口: macro_china_hk_gbp

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_3.html

    描述: 东方财富-经济数据一览-中国香港-香港 GDP

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_gbp = ak.macro_china_hk_gbp()
        macro_china_hk_gbp_df = sanitize_data_pandas(macro_china_hk_gbp)
        return macro_china_hk_gbp_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 中国香港-GDP指数-GDP 同比
@router.get("/macro_china_hk_gbp_ratio",
            operation_id="get_macro_china_hk_gbp_ratio")
async def get_macro_china_hk_gbp_ratio():
    """
    中国香港-GDP指数-GDP 同比

    接口: macro_china_hk_gbp_ratio

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_4.html

    描述: 东方财富-经济数据一览-中国香港-香港 GDP 同比

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_gbp_ratio = ak.macro_china_hk_gbp_ratio()
        macro_china_hk_gbp_ratio_df = sanitize_data_pandas(macro_china_hk_gbp_ratio)
        return macro_china_hk_gbp_ratio_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
