# 市场全貌获取模块

from datetime import date as dt_date
import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


class DateRequest(BaseModel):
    date: dt_date


class SectorSummaryRequest(BaseModel):
    symbol: str
    ym_date: str


class AreaSummaryRequest(BaseModel):
    ym_date: str


def get_stock_sse_summary():
    """
    上海证券交易所
    描述: 上海证券交易所-股票数据总貌
    限量: 单次返回最近交易日的股票数据总貌(当前交易日的数据需要交易所收盘后统计)
    """
    stock_sse_summary_df = ak.stock_sse_summary()
    return stock_sse_summary_df


def get_stock_szse_summary(date):
    """
    深圳证券交易所
    证券类别统计
    描述: 深圳证券交易所-市场总貌-证券类别统计
    限量: 单次返回指定 symbol 的市场总貌数据-证券类别统计(当前交易日的数据需要交易所收盘后统计)
    """
    stock_szse_summary_df = ak.stock_szse_summary(date=date.strftime('%Y%m%d'))
    return stock_szse_summary_df


def get_stock_szse_area_summary(ym_date):
    """
    地区交易排序
    描述: 深圳证券交易所-市场总貌-地区交易排序
    限量: 单次返回指定 ym_date 的市场总貌数据-地区交易排序数据
    """
    stock_szse_area_summary_df = ak.stock_szse_area_summary(date=ym_date)
    return stock_szse_area_summary_df


def get_stock_szse_sector_summary(symbol, ym_date):
    """
    股票行业成交
    描述: 深圳证券交易所-统计资料-股票行业成交数据
    限量: 单次返回指定 symbol 和 ym_date 的统计资料-股票行业成交数据
    """
    stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol=symbol, date=ym_date)
    return stock_szse_sector_summary_df


def get_stock_sse_deal_daily(date):
    """
    上海证券交易所-每日概况
    描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况
    限量: 单次返回指定日期的每日概况数据, 当前交易日数据需要在收盘后获取; 注意在 20211227（包含）之后输出格式变化
    """
    stock_sse_deal_daily_df = ak.stock_sse_deal_daily(date=date.strftime('%Y%m%d'))
    return stock_sse_deal_daily_df


@router.get("/stock_sse_summary", operation_id="get_stock_sse_summary")
def get_stock_sse_summary():
    """
    获取上海证券交易所的股票数据总貌
    """
    try:
        stock_sse_summary_df = get_stock_sse_summary()
        sanitized_data = sanitize_data(stock_sse_summary_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SSE summary: {str(e)}")


@router.post("/stock_szse_summary", operation_id="post_stock_szse_summary")
async def post_stock_szse_summary(request: DateRequest):
    """
    获取深圳证券交易所的证券类别统计
    """
    try:
        stock_szse_summary_df = get_stock_szse_summary(date=request.date)
        sanitized_data = sanitize_data(stock_szse_summary_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SZSE summary: {str(e)}")


@router.post("/stock_szse_sector_summary", operation_id="post_stock_szse_sector_summary")
async def post_stock_szse_sector_summary(request: SectorSummaryRequest):
    """
    获取深圳证券交易所的股票行业成交数据
    """
    try:
        stock_szse_sector_summary_df = get_stock_szse_sector_summary(symbol=request.symbol, ym_date=request.ym_date)
        sanitized_data = sanitize_data(stock_szse_sector_summary_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SZSE sector summary: {str(e)}")


@router.post("/stock_sse_deal_daily", operation_id="post_stock_sse_deal_daily")
async def post_stock_sse_deal_daily(request: DateRequest):
    """
    获取上海证券交易所的每日概况
    """
    try:
        stock_sse_deal_daily_df = get_stock_sse_deal_daily(date=request.date)
        sanitized_data = sanitize_data(stock_sse_deal_daily_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SSE daily deal: {str(e)}")
