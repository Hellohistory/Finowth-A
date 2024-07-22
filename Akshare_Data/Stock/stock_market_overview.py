# 市场全貌获取模块


import akshare as ak
from fastapi import HTTPException, APIRouter
from datetime import date as dt_date

from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


@router.get("/stock_sse_summary", operation_id="get_stock_sse_summary")
async def get_stock_sse_summary():
    """
    接口: stock_sse_summary

    目标地址: http://www.sse.com.cn/market/stockdata/statistic/

    描述: 上海证券交易所-股票数据总貌

    限量: 单次返回最近交易日的股票数据总貌(当前交易日的数据需要交易所收盘后统计)
    """
    stock_sse_summary_df = ak.stock_sse_summary()
    stock_sse_summary_list = stock_sse_summary_df.to_dict(orient="records")
    return stock_sse_summary_list


def get_stock_szse_summary(date):
    """
    深圳证券交易所
    证券类别统计
    描述: 深圳证券交易所-市场总貌-证券类别统计
    限量: 单次返回指定 symbol 的市场总貌数据-证券类别统计(当前交易日的数据需要交易所收盘后统计)
    """
    stock_szse_summary_df = ak.stock_szse_summary(date=date.strftime('%Y%m%d'))
    return stock_szse_summary_df


class AreaSummaryRequest(BaseModel):
    ym_date: str = Field(..., title="指定交易日", description="例如202406")


@router.post("/stock_szse_area_summary", operation_id="post_stock_szse_area_summary")
async def post_stock_szse_area_summary(request: AreaSummaryRequest):
    """
    接口: stock_szse_area_summary

    目标地址: http://www.szse.cn/market/overview/index.html

    描述: 深圳证券交易所-市场总貌-地区交易排序

    限量: 单次返回指定日期的市场总貌数据-地区交易排序数据
    """
    try:
        data_df = ak.stock_szse_area_summary(date=request.ym_date)
        return data_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_stock_szse_sector_summary(symbol, ym_date):
    """
    接口: stock_szse_sector_summary

    目标地址: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html

    描述: 深圳证券交易所-统计资料-股票行业成交数据

    限量: 单次返回指定个股和 date 的统计资料-股票行业成交数据
    """
    stock_szse_sector_summary_df = ak.stock_szse_sector_summary(symbol=symbol, date=ym_date)
    return stock_szse_sector_summary_df


def get_stock_sse_deal_daily(date):
    """
    接口: stock_sse_deal_daily

    目标地址: http://www.sse.com.cn/market/stockdata/overview/day/

    描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况

    限量: 单次返回指定日期的每日概况数据, 当前交易日数据需要在收盘后获取; 注意在 20211227（包含）之后输出格式变化
    """
    stock_sse_deal_daily_df = ak.stock_sse_deal_daily(date=date.strftime('%Y%m%d'))
    return stock_sse_deal_daily_df


class DtDateRequest(BaseModel):
    date: dt_date = Field(..., title="指定交易日", description="例如2024-07-12; 当前交易日的数据需要交易所收盘后统计")


@router.post("/stock_szse_summary", operation_id="post_stock_szse_summary")
async def post_stock_szse_summary(request: DtDateRequest):
    """
    接口: stock_szse_summary

    目标地址: http://www.szse.cn/market/overview/index.html

    描述: 深圳证券交易所-市场总貌-证券类别统计

    限量: 单次返回指定时间的市场总貌数据-证券类别统计(当前交易日的数据需要交易所收盘后统计)
    """
    try:
        stock_szse_summary_df = get_stock_szse_summary(date=request.date)
        sanitized_data = sanitize_data(stock_szse_summary_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SZSE summary: {str(e)}")


class SectorSummaryRequest(BaseModel):
    symbol: str = Field(..., title="指定时间段", description="例如当月; 可选择当月与当年两个时间段")
    ym_date: str = Field(..., title="指定年月", description="例如202203")


@router.post("/stock_szse_sector_summary", operation_id="post_stock_szse_sector_summary")
async def post_stock_szse_sector_summary(request: SectorSummaryRequest):
    """
    接口: stock_szse_sector_summary

    目标地址: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html

    描述: 深圳证券交易所-统计资料-股票行业成交数据

    限量: 单次返回指定个股和 date 的统计资料-股票行业成交数据
    """
    try:
        stock_szse_sector_summary_df = get_stock_szse_sector_summary(symbol=request.symbol, ym_date=request.ym_date)
        sanitized_data = sanitize_data(stock_szse_sector_summary_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SZSE sector summary: {str(e)}")


@router.post("/stock_sse_deal_daily", operation_id="post_stock_sse_deal_daily")
async def post_stock_sse_deal_daily(request: DtDateRequest):
    """
    接口: stock_sse_deal_daily

    目标地址: http://www.sse.com.cn/market/stockdata/overview/day/

    描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况

    限量: 单次返回指定日期的每日概况数据, 当前交易日数据需要在收盘后获取; 注意在 20211227（包含）之后输出格式变化
    """
    try:
        stock_sse_deal_daily_df = get_stock_sse_deal_daily(date=request.date)
        sanitized_data = sanitize_data(stock_sse_deal_daily_df.to_dict(orient="records"))
        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SSE daily deal: {str(e)}")
