import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-行业指数-原油运输指数
@router.get("/macro_china_bdti_index",
            operation_id="get_macro_china_bdti_index")
async def get_macro_china_bdti_index():
    """
    国民经济运行状况-行业指数-物流景气指数

    接口: macro_china_bdti_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00107668.html

    描述: 原油运输指数数据, 数据区间从 20011227-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_bdti_index = ak.macro_china_bdti_index()
        macro_china_bdti_index_df = sanitize_data_pandas(macro_china_bdti_index)
        return macro_china_bdti_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-成品油运输指数
@router.get("/macro_shipping_bcti",
            operation_id="get_macro_shipping_bcti")
async def get_macro_shipping_bcti():
    """
    国民经济运行状况-行业指数-成品油运输指数

    接口: macro_shipping_bcti

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00107669.html

    描述: 成品油运输指数, 数据区间从 20011217-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_shipping_bcti = ak.macro_shipping_bcti()
        macro_shipping_bcti_df = sanitize_data_pandas(macro_shipping_bcti)
        return macro_shipping_bcti_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
