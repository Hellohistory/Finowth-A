import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-金融市场-股票筹资
@router.get("/macro_stock_finance",
            operation_id="get_macro_stock_finance")
async def get_macro_stock_finance():
    """
    国民经济运行状况-金融市场-股票筹资

    接口: macro_stock_finance

    目标地址: https://data.10jqka.com.cn/macro/finance/

    描述: 同花顺-数据中心-宏观数据-股票筹资

    限量: 单次返回所有历史数据
    """
    try:
        macro_stock_finance = ak.macro_stock_finance()
        macro_stock_finance_df = sanitize_data_pandas(macro_stock_finance)
        return macro_stock_finance_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融市场-新增人民币贷款
@router.get("/macro_rmb_loan",
            operation_id="get_macro_rmb_loan")
async def get_macro_rmb_loan():
    """
    国民经济运行状况-金融市场-新增人民币贷款

    接口: macro_rmb_loan

    目标地址: https://data.10jqka.com.cn/macro/loan/

    描述: 同花顺-数据中心-宏观数据-新增人民币贷款

    限量: 单次返回所有历史数据
    """
    try:
        macro_rmb_loan = ak.macro_rmb_loan()
        macro_rmb_loan_df = sanitize_data_pandas(macro_rmb_loan)
        return macro_rmb_loan_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融市场-人民币存款余额
@router.get("/macro_rmb_deposit",
            operation_id="get_macro_rmb_deposit")
async def get_macro_rmb_deposit():
    """
    国民经济运行状况-金融市场-人民币存款余额

    接口: macro_rmb_deposit

    目标地址: https://data.10jqka.com.cn/macro/rmb/

    描述: 同花顺-数据中心-宏观数据-人民币存款余额

    限量: 单次返回所有历史数据
    """
    try:
        macro_rmb_deposit = ak.macro_rmb_deposit()
        macro_rmb_deposit_df = sanitize_data_pandas(macro_rmb_deposit)
        return macro_rmb_deposit_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
