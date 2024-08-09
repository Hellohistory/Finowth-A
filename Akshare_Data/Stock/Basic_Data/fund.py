import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 新浪财经-股本股东-基金持股
@router.post("/stock_fund_stock_holder", operation_id="stock_fund_stock_holder")
async def stock_fund_stock_holder(request: SymbolRequest):
    """
    新浪财经-基金持股

    接口: stock_fund_stock_holder

    目标地址: https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_FundStockHolder/stockid/600004.phtml

    描述: 新浪财经-股本股东-基金持股

    限量: 新浪财经-股本股东-基金持股所有历史数据
    """
    try:
        stock_fund_stock_holder = ak.stock_fund_stock_holder(symbol=request.symbol)
        stock_fund_stock_holder_df = sanitize_data_pandas(stock_fund_stock_holder)
        return stock_fund_stock_holder_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="数据类型",
                        description="可选择'基金持仓', 'QFII持仓', '社保持仓', '券商持仓', '保险持仓', '信托持仓'")
    date: str = Field(..., title="财报发布日期",
                      description="可选择'xxxx-03-31', 'xxxx-06-30', 'xxxx-09-30', 'xxxx-12-31'")


# 东方财富-数据中心-主力数据-基金持仓
@router.post("/stock_report_fund_hold", operation_id="stock_report_fund_hold")
async def stock_report_fund_hold(request: DongCaiSymbolDateRequest):
    """
    东方财富-主力数据-基金持仓

    接口: stock_report_fund_hold

    目标地址: http://data.eastmoney.com/zlsj/2020-06-30-1-2.html

    描述: 东方财富-数据中心-主力数据-基金持仓

    限量: 单次返回指定数据类型和财报发布日期的所有历史数据
    """
    try:
        stock_report_fund_hold = ak.stock_report_fund_hold(symbol=request.symbol, date=request.date)
        stock_report_fund_hold_df = sanitize_data_pandas(stock_report_fund_hold)
        return stock_report_fund_hold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiChiCangSymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="基金代码", description="例：005827")
    date: str = Field(..., title="财报发布日期",
                      description="可选择'xxxx-03-31', 'xxxx-06-30', 'xxxx-09-30', 'xxxx-12-31'")


# 东方财富-数据中心-主力数据-基金持仓-基金持仓明细表
@router.post("/stock_report_fund_hold_detail", operation_id="stock_report_fund_hold_detail")
async def stock_report_fund_hold_detail(request: DongCaiChiCangSymbolDateRequest):
    """
    东方财富-基金持仓-基金持仓明细表

    接口: stock_report_fund_hold_detail

    目标地址: http://data.eastmoney.com/zlsj/ccjj/2020-12-31-008286.html

    描述: 东方财富-数据中心-主力数据-基金持仓-基金持仓明细表

    限量: 单次返回指定个股和指定财报发布日期的所有历史数据
    """
    try:
        stock_report_fund_hold_detail = ak.stock_report_fund_hold_detail(symbol=request.symbol, date=request.date)
        stock_report_fund_hold_detail_df = sanitize_data_pandas(stock_report_fund_hold_detail)
        return stock_report_fund_hold_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
