import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DateRequest(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20240717")


# 涨停股池
@router.post("/stock_zt_pool_em", operation_id="stock_zt_pool_em")
async def stock_zt_pool_em(request: DateRequest):
    """
    东方财富-涨停板行情-涨停股池

    接口: stock_zt_pool_em

    目标地址: https://quote.eastmoney.com/ztb/detail#type=ztgc

    描述: 东方财富-行情中心-涨停板行情-涨停股池

    限量: 单次返回指定时间的涨停股池数据; 该接口只能获取近期的数据
    """
    try:
        stock_zt_pool_em = ak.stock_zt_pool_em(date=request.date)
        stock_zt_pool_em_df = sanitize_data_pandas(stock_zt_pool_em)
        return stock_zt_pool_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 昨日涨停股池
@router.post("/stock_zt_pool_previous_em", operation_id="stock_zt_pool_previous_em")
async def stock_zt_pool_previous_em(request: DateRequest):
    """
    东方财富-涨停板行情-昨日涨停股池

    接口: stock_zt_pool_previous_em

    目标地址: https://quote.eastmoney.com/ztb/detail#type=zrzt

    描述: 东方财富-行情中心-涨停板行情-昨日涨停股池

    限量: 单次返回指定时间的昨日涨停股池数据; 该接口只能获取近期的数据
    """
    try:
        stock_zt_pool_previous_em = ak.stock_zt_pool_previous_em(date=request.date)
        stock_zt_pool_previous_em_df = sanitize_data_pandas(stock_zt_pool_previous_em)
        return stock_zt_pool_previous_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 强势股池
@router.post("/stock_zt_pool_strong_em", operation_id="stock_zt_pool_strong_em")
async def stock_zt_pool_strong_em(request: DateRequest):
    """
    东方财富-涨停板行情-强势股池

    接口: stock_zt_pool_strong_em

    目标地址: https://quote.eastmoney.com/ztb/detail#type=qsgc

    描述: 东方财富-行情中心-涨停板行情-强势股池

    限量: 单次返回指定时间的强势股池数据；该接口只能获取近期的数据
    """
    try:
        stock_zt_pool_strong_em = ak.stock_zt_pool_strong_em(date=request.date)
        stock_zt_pool_strong_em_df = sanitize_data_pandas(stock_zt_pool_strong_em)
        return stock_zt_pool_strong_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 次新股池
@router.post("/stock_zt_pool_sub_new_em", operation_id="stock_zt_pool_sub_new_em")
async def stock_zt_pool_sub_new_em(request: DateRequest):
    """
    东方财富-涨停板行情-次新股池

    接口: stock_zt_pool_sub_new_em

    目标地址: https://quote.eastmoney.com/ztb/detail#type=cxgc

    描述: 东方财富-行情中心-涨停板行情-次新股池

    限量: 单次返回指定时间的次新股池数据；该接口只能获取近期的数据
    """
    try:
        stock_zt_pool_sub_new_em = ak.stock_zt_pool_sub_new_em(date=request.date)
        stock_zt_pool_sub_new_em_df = sanitize_data_pandas(stock_zt_pool_sub_new_em)
        return stock_zt_pool_sub_new_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 炸板股池
@router.post("/stock_zt_pool_zbgc_em", operation_id="stock_zt_pool_zbgc_em")
async def stock_zt_pool_zbgc_em(request: DateRequest):
    """
    东方财富-涨停板行情-炸板股池

    接口: stock_zt_pool_zbgc_em

    目标地址: https://quote.eastmoney.com/ztb/detail#type=zbgc

    描述: 东方财富-行情中心-涨停板行情-炸板股池

    限量: 单次返回指定时间的炸板股池数据；该接口只能获取近期的数据
    """
    try:
        stock_zt_pool_zbgc_em = ak.stock_zt_pool_zbgc_em(date=request.date)
        stock_zt_pool_zbgc_em_df = sanitize_data_pandas(stock_zt_pool_zbgc_em)
        return stock_zt_pool_zbgc_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 跌停股池
@router.post("/stock_zt_pool_dtgc_em", operation_id="stock_zt_pool_dtgc_em")
async def stock_zt_pool_dtgc_em(request: DateRequest):
    """
    东方财富-涨停板行情-跌停股池

    接口: stock_zt_pool_dtgc_em

    目标地址: https://quote.eastmoney.com/ztb/detail#type=zbgc

    描述: 东方财富-行情中心-涨停板行情-跌停股池

    限量: 单次返回指定时间的跌停股池数据；该接口只能获取近期的数据
    """
    try:
        stock_zt_pool_dtgc_em = ak.stock_zt_pool_dtgc_em(date=request.date)
        stock_zt_pool_dtgc_em_df = sanitize_data_pandas(stock_zt_pool_dtgc_em)
        return stock_zt_pool_dtgc_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
