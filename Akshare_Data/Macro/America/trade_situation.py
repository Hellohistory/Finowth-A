import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-贸易状况-美国贸易帐报告
@router.get("/macro_usa_trade_balance",
            operation_id="macro_usa_trade_balance")
async def macro_usa_trade_balance():
    """
    美国-贸易状况-美国贸易帐报告

    接口: macro_usa_trade_balance

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_trade_balance

    描述: 美国贸易帐报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_trade_balance = ak.macro_usa_trade_balance()
        macro_usa_trade_balance_df = sanitize_data_pandas(macro_usa_trade_balance)
        return macro_usa_trade_balance_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-贸易状况-美国经常帐报告
@router.get("/macro_usa_current_account",
            operation_id="macro_usa_current_account")
async def macro_usa_current_account():
    """
    美国-贸易状况-美国贸易帐报告

    接口: macro_usa_current_account

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_current_account

    描述: 美国经常帐报告, 数据区间从 20080317-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_current_account = ak.macro_usa_current_account()
        macro_usa_current_account_df = sanitize_data_pandas(macro_usa_current_account)
        return macro_usa_current_account_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
