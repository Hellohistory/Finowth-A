import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-行业指数-超灵便型船运价指数
@router.get("/macro_china_bsi_index",
            operation_id="get_macro_china_bsi_index")
async def get_macro_china_bsi_index():
    """
    国民经济运行状况-行业指数-超灵便型船运价指数

    接口: macro_china_bsi_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00107667.html

    描述: 超灵便型船运价指数数据, 数据区间从 20060103-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_bsi_index = ak.macro_china_bsi_index()
        macro_china_bsi_index_df = sanitize_data_pandas(macro_china_bsi_index)
        return macro_china_bsi_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-超灵便型船运价指数
@router.get("/macro_china_bsi_index",
            operation_id="get_macro_china_bsi_index")
async def get_macro_china_bsi_index():
    """
    国民经济运行状况-行业指数-超灵便型船运价指数

    接口: macro_china_bsi_index

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00107667.html

    描述: 超灵便型船运价指数数据, 数据区间从 20060103-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_bsi_index = ak.macro_china_bsi_index()
        macro_china_bsi_index_df = sanitize_data_pandas(macro_china_bsi_index)
        return macro_china_bsi_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-波罗的海干散货指数
@router.get("/macro_shipping_bdi",
            operation_id="get_macro_shipping_bdi")
async def get_macro_shipping_bdi():
    """
    国民经济运行状况-行业指数-波罗的海干散货指数

    接口: macro_shipping_bdi

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00107664.html

    描述: 波罗的海干散货指数, 数据区间从 19881019-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_shipping_bdi = ak.macro_shipping_bdi()
        macro_shipping_bdi_df = sanitize_data_pandas(macro_shipping_bdi)
        return macro_shipping_bdi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-行业指数-巴拿马型运费指数
@router.get("/macro_shipping_bpi",
            operation_id="get_macro_shipping_bpi")
async def get_macro_shipping_bpi():
    """
    国民经济运行状况-行业指数-巴拿马型运费指数

    接口: macro_shipping_bpi

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI00107665.html

    描述: 巴拿马型运费指数, 数据区间从 19981231-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_shipping_bpi = ak.macro_shipping_bpi()
        macro_shipping_bpi_df = sanitize_data_pandas(macro_shipping_bpi)
        return macro_shipping_bpi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
