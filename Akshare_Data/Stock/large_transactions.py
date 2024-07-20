# 大宗交易

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


# 市场统计
@router.get("/stock_dzjy_sctj", operation_id="get_stock_dzjy_sctj")
def get_stock_dzjy_sctj():
    """
    东方财富网-数据中心-大宗交易-市场统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_sctj_df = ak.stock_dzjy_sctj()
        return stock_dzjy_sctj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolDateRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class DateRangeRequest(BaseModel):
    start_date: str
    end_date: str


class SymbolRequest(BaseModel):
    symbol: str


@router.post("/stock_dzjy_mrmx", operation_id="post_stock_dzjy_mrmx")
async def post_stock_dzjy_mrmx(request: SymbolDateRequest):
    """
    东方财富网-数据中心-大宗交易-每日明细
    单次返回所有历史数据
    """
    try:
        stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol=request.symbol, start_date=request.start_date,
                                                end_date=request.end_date)
        return stock_dzjy_mrmx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_mrtj", operation_id="post_stock_dzjy_mrtj")
async def post_stock_dzjy_mrtj(request: DateRangeRequest):
    """
    东方财富网-数据中心-大宗交易-每日统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_mrtj_df = ak.stock_dzjy_mrtj(start_date=request.start_date, end_date=request.end_date)
        return stock_dzjy_mrtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_hygtj", operation_id="post_stock_dzjy_hygtj")
async def post_stock_dzjy_hygtj(request: SymbolRequest):
    """
    东方财富网-数据中心-大宗交易-活跃 A 股统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_hygtj_df = ak.stock_dzjy_hygtj(symbol=request.symbol)
        return stock_dzjy_hygtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_hyyybtj", operation_id="post_stock_dzjy_hyyybtj")
async def post_stock_dzjy_hyyybtj(request: SymbolRequest):
    """
    东方财富网-数据中心-大宗交易-活跃营业部统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_hyyybtj_df = ak.stock_dzjy_hyyybtj(symbol=request.symbol)
        return stock_dzjy_hyyybtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_yybph", operation_id="post_stock_dzjy_yybph")
async def post_stock_dzjy_yybph(request: SymbolRequest):
    """
    东方财富网-数据中心-大宗交易-营业部排行
    单次返回所有历史数据
    """
    try:
        stock_dzjy_yybph_df = ak.stock_dzjy_yybph(symbol=request.symbol)
        return stock_dzjy_yybph_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
