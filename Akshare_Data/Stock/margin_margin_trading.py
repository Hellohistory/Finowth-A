import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class SingleDateRequest(BaseModel):
    date: str


@router.post("/stock_margin_ratio_pa", operation_id="post_stock_margin_ratio_pa")
async def post_stock_margin_ratio_pa(request: SingleDateRequest):
    """
    融资融券-标的证券名单及保证金比例查询
    """
    try:
        stock_margin_ratio_pa_df = ak.stock_margin_ratio_pa(date=request.date)
        return stock_margin_ratio_pa_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 暂无法获取
# @router.get("/stock_margin_account_info")
# def get_stock_margin_account_info():
#     """
#     东方财富网-数据中心-融资融券-融资融券账户统计-两融账户信息
#     """
#     try:
#         stock_margin_account_info_df = ak.stock_margin_account_info()
#         return stock_margin_account_info_df.to_dict(orient="records")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


class DateRangeRequest(BaseModel):
    start_date: str
    end_date: str


class SingleDateRequest(BaseModel):
    date: str


@router.post("/stock_margin_sse", operation_id="post_stock_margin_sse")
async def post_stock_margin_sse(request: DateRangeRequest):
    """
    上海证券交易所-融资融券数据-融资融券汇总数据
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
    """
    try:
        stock_margin_underlying_info_szse_df = ak.stock_margin_underlying_info_szse(date=request.date)
        return stock_margin_underlying_info_szse_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
