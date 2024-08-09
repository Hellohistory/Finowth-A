import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-金融指标-上海银行业同业拆借报告
@router.get("/macro_china_shibor_all",
            operation_id="macro_china_shibor_all")
async def macro_china_shibor_all():
    """
    国民经济运行状况-金融指标-上海银行业同业拆借报告

    接口: macro_china_shibor_all

    目标地址: https://datacenter.jin10.com/reportType/dc_shibor

    描述: 上海银行业同业拆借报告, 数据区间从 20170317-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_shibor_all = ak.macro_china_shibor_all()
        macro_china_shibor_all_df = sanitize_data_pandas(macro_china_shibor_all)
        return macro_china_shibor_all_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-人民币香港银行同业拆息
@router.get("/macro_china_hk_market_info",
            operation_id="macro_china_hk_market_info")
async def macro_china_hk_market_info():
    """
    国民经济运行状况-金融指标-人民币香港银行同业拆息

    接口: macro_china_hk_market_info

    目标地址: https://datacenter.jin10.com/reportType/dc_hk_market_info

    描述: 香港同业拆借报告, 数据区间从 20170320-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_market_info = ak.macro_china_hk_market_info()
        macro_china_hk_market_info_df = sanitize_data_pandas(macro_china_hk_market_info)
        return macro_china_hk_market_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
