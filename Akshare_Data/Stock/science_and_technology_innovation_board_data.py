import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import StockReportRequest
from alone_test import StockDailyRequest

router = APIRouter()


# 新浪财经-科创板股票实时行情数据
@router.get("/stock_zh_kcb_spot", operation_id="get_stock_zh_kcb_spot")
async def get_stock_zh_kcb_spot():
    """
    描述: 新浪财经-科创板股票实时行情数据
    限量: 单次返回所有科创板上市公司的实时行情数据
    """
    try:
        stock_zh_kcb_spot_df = ak.stock_zh_kcb_spot()
        return stock_zh_kcb_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-科创板股票历史行情数据
@router.post("/stock_zh_kcb_daily", operation_id="post_stock_zh_kcb_daily")
async def post_stock_zh_kcb_daily(request: StockDailyRequest):
    """
    描述: 新浪财经-科创板股票历史行情数据
    限量: 单次返回指定 symbol 和 adjust 的所有历史行情数据
    """
    try:
        stock_zh_kcb_daily_df = ak.stock_zh_kcb_daily(symbol=request.symbol, adjust=request.adjust)
        return stock_zh_kcb_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-科创板报告数据
@router.post("/stock_zh_kcb_report_em", operation_id="post_stock_zh_kcb_report_em")
async def post_stock_zh_kcb_report_em(request: StockReportRequest):
    """
    描述: 东方财富-科创板报告数据
    限量: 单次返回所有科创板上市公司的报告数据
    """
    try:
        stock_zh_kcb_report_em_df = ak.stock_zh_kcb_report_em(from_page=request.from_page, to_page=request.to_page)
        return stock_zh_kcb_report_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
