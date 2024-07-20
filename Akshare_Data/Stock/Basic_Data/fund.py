import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


class SymbolDateRequest(BaseModel):
    symbol: str
    date: str


# 新浪财经-股本股东-基金持股
@router.post("/stock_fund_stock_holder", operation_id="post_stock_fund_stock_holder")
def get_stock_fund_stock_holder(request: SymbolRequest):
    """
    描述: 新浪财经-股本股东-基金持股
    限量: 新浪财经-股本股东-基金持股所有历史数据
    """
    try:
        stock_fund_stock_holder_df = ak.stock_fund_stock_holder(symbol=request.symbol)
        return stock_fund_stock_holder_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-主力数据-基金持仓
@router.post("/stock_report_fund_hold", operation_id="post_stock_report_fund_hold")
def get_stock_report_fund_hold(request: SymbolDateRequest):
    """
    描述: 东方财富网-数据中心-主力数据-基金持仓
    限量: 单次返回指定 symbol 和 symbol 的所有历史数据
    """
    try:
        stock_report_fund_hold_df = ak.stock_report_fund_hold(symbol=request.symbol, date=request.date)
        return stock_report_fund_hold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-主力数据-基金持仓-基金持仓明细表
@router.post("/stock_report_fund_hold_detail", operation_id="post_stock_report_fund_hold_detail")
def get_stock_report_fund_hold_detail(request: SymbolDateRequest):
    """
    描述: 东方财富网-数据中心-主力数据-基金持仓-基金持仓明细表
    限量: 单次返回指定 symbol 和 symbol 的所有历史数据
    """
    try:
        stock_report_fund_hold_detail_df = ak.stock_report_fund_hold_detail(symbol=request.symbol, date=request.date)
        stock_report_fund_hold_detail_df = sanitize_data_pandas(stock_report_fund_hold_detail_df)

        return stock_report_fund_hold_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
