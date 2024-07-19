# 大宗交易

import akshare as ak
from fastapi import APIRouter, HTTPException

router = APIRouter()


# 市场统计
@router.get("/stock_dzjy_sctj")
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


# 每日明细
@router.get("/stock_dzjy_mrmx")
def get_stock_dzjy_mrmx(symbol: str, start_date: str, end_date: str):
    """
    东方财富网-数据中心-大宗交易-每日明细
    单次返回所有历史数据
    """
    try:
        stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol=symbol, start_date=start_date, end_date=end_date)
        return stock_dzjy_mrmx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 每日统计
@router.get("/stock_dzjy_mrtj")
def get_stock_dzjy_mrtj(start_date: str, end_date: str):
    """
    东方财富网-数据中心-大宗交易-每日统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_mrtj_df = ak.stock_dzjy_mrtj(start_date=start_date, end_date=end_date)
        return stock_dzjy_mrtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 活跃 A 股统计
@router.get("/stock_dzjy_hygtj")
def get_stock_dzjy_hygtj(symbol: str):
    """
    东方财富网-数据中心-大宗交易-活跃 A 股统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_hygtj_df = ak.stock_dzjy_hygtj(symbol=symbol)
        return stock_dzjy_hygtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 活跃营业部统计
@router.get("/stock_dzjy_hyyybtj")
def get_stock_dzjy_hyyybtj(symbol: str):
    """
    东方财富网-数据中心-大宗交易-活跃营业部统计
    单次返回所有历史数据
    """
    try:
        stock_dzjy_hyyybtj_df = ak.stock_dzjy_hyyybtj(symbol=symbol)
        return stock_dzjy_hyyybtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 营业部排行
@router.get("/stock_dzjy_yybph")
def get_stock_dzjy_yybph(symbol: str):
    """
    东方财富网-数据中心-大宗交易-营业部排行
    单次返回所有历史数据
    """
    try:
        stock_dzjy_yybph_df = ak.stock_dzjy_yybph(symbol=symbol)
        return stock_dzjy_yybph_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
