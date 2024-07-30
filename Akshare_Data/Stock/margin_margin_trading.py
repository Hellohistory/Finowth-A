import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


class SingleDateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20231013")


@router.post("/stock_margin_ratio_pa", operation_id="post_stock_margin_ratio_pa")
async def post_stock_margin_ratio_pa(request: SingleDateRequest):
    """
    融资融券-标的证券名单及保证金比例查询

    接口: stock_margin_ratio_pa

    目标地址: https://stock.pingan.com/static/webinfo/margin/business.html?businessType=0

    描述: 融资融券-标的证券名单及保证金比例查询

    限量: 单次返回指定交易日的所有历史数据
    """
    try:
        stock_margin_ratio_pa_df = ak.stock_margin_ratio_pa(date=request.date)
        return stock_margin_ratio_pa_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_margin_account_info", operation_id="get_stock_margin_account_info")
def get_stock_margin_account_info():
    """
    东方财富-融资融券-融资融券账户统计-两融账户信息

    接口: stock_margin_account_info

    目标地址: https://data.eastmoney.com/rzrq/zhtjday.html

    描述: 东方财富-数据中心-融资融券-融资融券账户统计-两融账户信息

    限量: 单次返回所有历史数据
    """
    try:
        stock_margin_account_info_df = ak.stock_margin_account_info()
        return stock_margin_account_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


@router.post("/stock_margin_sse", operation_id="post_stock_margin_sse")
async def post_stock_margin_sse(request: DateRangeRequest):
    """
    上海证券交易所-融资融券数据-融资融券汇总数据

    接口: stock_margin_sse

    目标地址: http://www.sse.com.cn/market/othersdata/margin/sum/

    描述: 上海证券交易所-融资融券数据-融资融券汇总数据

    限量: 单次返回指定时间段内的所有历史数据
    """
    try:
        stock_margin_sse_df = ak.stock_margin_sse(start_date=request.start_date, end_date=request.end_date)
        return stock_margin_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_margin_detail_sse", operation_id="post_stock_margin_detail_sse")
async def post_stock_margin_detail_sse(request: SingleDateRequest):
    """
    上海证券交易所-融资融券数据-融资融券明细数据

    接口: stock_margin_detail_sse

    目标地址: http://www.sse.com.cn/market/othersdata/margin/detail/

    描述: 上海证券交易所-融资融券数据-融资融券明细数据

    限量: 单次返回交易日的所有历史数据
    """
    try:
        stock_margin_detail_sse_df = ak.stock_margin_detail_sse(date=request.date)
        return stock_margin_detail_sse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_margin_szse", operation_id="post_stock_margin_szse")
async def post_stock_margin_szse(request: SingleDateRequest):
    """
    深圳证券交易所-融资融券数据-融资融券汇总数据

    接口: stock_margin_szse

    目标地址: https://www.szse.cn/disclosure/margin/margin/index.html

    描述: 深圳证券交易所-融资融券数据-融资融券汇总数据

    限量: 单次返回指定时间内的所有历史数据
    """
    try:
        stock_margin_szse_df = ak.stock_margin_szse(date=request.date)
        return stock_margin_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_margin_detail_szse", operation_id="post_stock_margin_detail_szse")
async def post_stock_margin_detail_szse(request: SingleDateRequest):
    """
    深证证券交易所-融资融券数据-融资融券交易明细数据

    接口: stock_margin_detail_szse

    目标地址: https://www.szse.cn/disclosure/margin/margin/index.html

    描述: 深证证券交易所-融资融券数据-融资融券交易明细数据

    限量: 单次返回指定时间的所有历史数据
    """
    try:
        stock_margin_detail_szse_df = ak.stock_margin_detail_szse(date=request.date)
        return stock_margin_detail_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_margin_underlying_info_szse", operation_id="post_stock_margin_underlying_info_szse")
async def post_stock_margin_underlying_info_szse(request: SingleDateRequest):
    """
    深圳证券交易所-融资融券数据-标的证券信息

    接口: stock_margin_underlying_info_szse

    目标地址: https://www.szse.cn/disclosure/margin/object/index.html

    描述: 深圳证券交易所-融资融券数据-标的证券信息

    限量: 单次返回交易日的所有历史数据
    """
    try:
        stock_margin_underlying_info_szse_df = ak.stock_margin_underlying_info_szse(date=request.date)
        return stock_margin_underlying_info_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
