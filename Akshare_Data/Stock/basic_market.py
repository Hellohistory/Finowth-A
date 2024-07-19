import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_numpy

router = APIRouter()


class StockSymbolRequest(BaseModel):
    symbol: str


# 同花顺-主营介绍
@router.post("/stock_zyjs_ths")
def get_stock_zyjs_ths(request: StockSymbolRequest):
    """
    描述: 同花顺-主营介绍
    限量: 单次返回所有数据
    """
    try:
        stock_zyjs_ths_df = ak.stock_zyjs_ths(symbol=request.symbol)
        return stock_zyjs_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-个股-主营构成
@router.post("/stock_zygc_em")
def get_stock_zygc_em(request: StockSymbolRequest):
    """
    描述: 东方财富网-个股-主营构成
    限量: 单次返回所有历史数据
    """
    try:
        stock_zygc_em_df = ak.stock_zygc_em(symbol=request.symbol)
        sanitized_data = stock_zygc_em_df.applymap(sanitize_data_numpy)

        return sanitized_data.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 益盟-F10-主营构成
@router.post("/stock_zygc_ym")
def get_stock_zygc_ym(request: StockSymbolRequest):
    """
    描述: 益盟-F10-主营构成
    限量: 单次返回所有历史数据
    """
    try:
        stock_zygc_ym_df = ak.stock_zygc_ym(symbol=request.symbol)
        return stock_zygc_ym_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 益盟-F10-管理层讨论与分析
@router.post("/stock_mda_ym")
def get_stock_mda_ym(request: StockSymbolRequest):
    """
    描述: 益盟-F10-管理层讨论与分析
    限量: 单次返回所有历史数据
    """
    try:
        stock_mda_ym_df = ak.stock_mda_ym(symbol=request.symbol)
        return stock_mda_ym_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolRequest(BaseModel):
    symbol: str


# 巨潮资讯-个股-公司概况
@router.post("/stock_profile_cninfo")
def get_stock_profile_cninfo(request: SymbolRequest):
    """
    描述: 巨潮资讯-个股-公司概况
    限量: 单次获取指定 symbol 的公司概况
    """
    try:
        stock_profile_cninfo_df = ak.stock_profile_cninfo(symbol=request.symbol)
        return stock_profile_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-个股-上市相关
@router.post("/stock_ipo_summary_cninfo")
def get_stock_ipo_summary_cninfo(request: SymbolRequest):
    """
    描述: 巨潮资讯-个股-上市相关
    限量: 单次获取指定 symbol 的上市相关数据
    """
    try:
        stock_ipo_summary_cninfo_df = ak.stock_ipo_summary_cninfo(symbol=request.symbol)
        return stock_ipo_summary_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
