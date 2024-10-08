# 市场全貌获取模块

import akshare as ak
import pandas as pd
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


@router.get("/stock_sse_summary", operation_id="stock_sse_summary")
async def stock_sse_summary():
    """
    上海证券交易所-股票数据总貌

    接口: stock_sse_summary

    目标地址: http://www.sse.com.cn/market/stockdata/statistic/

    描述: 上海证券交易所-股票数据总貌

    限量: 单次返回最近交易日的股票数据总貌(当前交易日的数据需要交易所收盘后统计)
    """
    try:
        stock_sse_summary = ak.stock_sse_summary()
        stock_sse_summary_df = sanitize_data_pandas(stock_sse_summary)
        return stock_sse_summary_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DateRequest(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240717")


@router.post("/stock_szse_summary", operation_id="stock_szse_summary")
async def stock_szse_summary(request: DateRequest):
    """
    深圳证券交易所-证券类别统计

    接口: stock_szse_summary

    目标地址: http://www.szse.cn/market/overview/index.html

    描述: 深圳证券交易所-市场总貌-证券类别统计

    限量: 单次返回指定时间的市场总貌数据-证券类别统计(当前交易日的数据需要交易所收盘后统计)
    """
    try:
        stock_szse_summary = ak.stock_szse_summary(date=request.date)
        stock_szse_summary_df = sanitize_data_pandas(stock_szse_summary)
        return stock_szse_summary_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SZSE summary: {str(e)}")


class SseDealStockDataRequest(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240717")


def sanitize_data_sse_deal(df: pd.DataFrame) -> pd.DataFrame:
    """
    清洗数据：标准化列名等
    """
    for col in df.select_dtypes(include=['category', 'object']).columns:
        df[col] = df[col].astype(str)
    df.columns = df.columns.str.strip()
    return df


@router.post("/stock_sse_deal_daily", operation_id="stock_sse_deal_daily")
def stock_sse_deal_daily(data: SseDealStockDataRequest) -> list[dict]:
    """
    上海证券交易所-每日概况

    接口: stock_sse_deal_daily

    目标地址: http://www.sse.com.cn/market/stockdata/overview/day/

    描述: 上海证券交易所-数据-股票数据-成交概况-股票成交概况-每日股票情况

    限量: 单次返回指定日期的每日概况数据, 当前交易日数据需要在收盘后获取; 注意在 20211227（包含）之后输出格式变化
    """
    try:
        stock_sse_deal_daily = ak.stock_sse_deal_daily(date=data.date)
        stock_sse_deal_daily_df = sanitize_data_sse_deal(stock_sse_deal_daily)
        return stock_sse_deal_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SectorSummaryRequest(BaseModel):
    symbol: str = Field(..., title="指定时间类型", description="可选择'当月', '当年'")
    date: str = Field(..., title="指定年月", description="例：202203")


@router.post("/stock_szse_sector_summary", operation_id="stock_szse_sector_summary")
async def stock_szse_sector_summary(request: SectorSummaryRequest):
    """
    深圳证券交易所-股票行业成交

    接口: stock_szse_sector_summary

    目标地址: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html

    描述: 深圳证券交易所-统计资料-股票行业成交数据

    限量: 单次返回指定个股和 date 的统计资料-股票行业成交数据
    """
    try:
        stock_szse_sector_summary = ak.stock_szse_sector_summary(symbol=request.symbol, date=request.date)
        stock_szse_sector_summary_df = sanitize_data_pandas(stock_szse_sector_summary)
        return stock_szse_sector_summary_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving SZSE sector summary: {str(e)}")


class AreaSummaryRequest(BaseModel):
    date: str = Field(..., title="指定交易月", description="例：202406")


@router.post("/stock_szse_area_summary", operation_id="stock_szse_area_summary")
async def stock_szse_area_summary(request: AreaSummaryRequest):
    """
    深圳证券交易所-地区交易排序

    接口: stock_szse_area_summary

    目标地址: http://www.szse.cn/market/overview/index.html

    描述: 深圳证券交易所-市场总貌-地区交易排序

    限量: 单次返回指定日期的市场总貌数据-地区交易排序数据
    """
    try:
        stock_szse_area_summary = ak.stock_szse_area_summary(date=request.date)
        stock_szse_area_summary_df = sanitize_data_pandas(stock_szse_area_summary)
        return stock_szse_area_summary_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
