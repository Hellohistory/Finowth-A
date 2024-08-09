import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-贸易状况-以美元计算出口年率
@router.get("/macro_china_exports_yoy", operation_id="macro_china_exports_yoy")
async def macro_china_exports_yoy():
    """
    国民经济运行状况-贸易状况-以美元计算出口年率

    接口: macro_china_exports_yoy

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_exports_yoy

    描述: 中国以美元计算出口年率报告, 数据区间从 19820201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_exports_yoy = ak.macro_china_exports_yoy()
        macro_china_exports_yoy_df = sanitize_data_pandas(macro_china_exports_yoy)
        return macro_china_exports_yoy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-贸易状况-以美元计算进口年率
@router.get("/macro_china_imports_yoy", operation_id="macro_china_imports_yoy")
async def macro_china_imports_yoy():
    """
    国民经济运行状况-贸易状况-以美元计算进口年率

    接口: macro_china_imports_yoy

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_imports_yoy

    描述: 中国以美元计算进口年率报告, 数据区间从 19960201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_imports_yoy = ak.macro_china_imports_yoy()
        macro_china_imports_yoy_df = sanitize_data_pandas(macro_china_imports_yoy)
        return macro_china_imports_yoy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-贸易状况-以美元计算贸易帐(亿美元)
@router.get("/macro_china_trade_balance", operation_id="macro_china_trade_balance")
async def macro_china_trade_balance():
    """
    国民经济运行状况-贸易状况-以美元计算贸易帐(亿美元)

    接口: macro_china_trade_balance

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_trade_balance

    描述: 中国以美元计算贸易帐报告, 数据区间从19810201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_trade_balance = ak.macro_china_trade_balance()
        macro_china_trade_balance_df = sanitize_data_pandas(macro_china_trade_balance)
        return macro_china_trade_balance_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
