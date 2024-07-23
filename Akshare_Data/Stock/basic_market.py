import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 同花顺-主营介绍
@router.post("/stock_zyjs_ths", operation_id="post_stock_zyjs_ths")
async def post_stock_zyjs_ths(request: SymbolRequest):
    """
    接口: stock_zyjs_ths

    目标地址: https://basic.10jqka.com.cn/new/000066/operate.html

    描述: 同花顺-主营介绍

    限量: 单次返回所有数据
    """
    try:
        stock_zyjs_ths_df = ak.stock_zyjs_ths(symbol=request.symbol)
        return stock_zyjs_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiSymbolRequest(BaseModel):
    symbol: str = Field(..., title="携带市场标识的股票代码", description="例：SH688041")


# 东方财富网-个股-主营构成
@router.post("/stock_zygc_em", operation_id="post_stock_zygc_em")
async def post_stock_zygc_em(request: DongCaiSymbolRequest):
    """
    接口: stock_zygc_em

    目标地址: https://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/Index?type=web&code=SH688041#

    描述: 东方财富网-个股-主营构成

    限量: 单次返回所有历史数据
    """
    try:
        stock_zygc_em_df = ak.stock_zygc_em(symbol=request.symbol)
        stock_zygc_em_df = sanitize_data_pandas(stock_zygc_em_df)

        return stock_zygc_em_df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 益盟-F10-主营构成
@router.post("/stock_zygc_ym", operation_id="post_stock_zygc_ym")
async def post_stock_zygc_ym(request: SymbolRequest):
    """
    接口: stock_zygc_ym

    目标地址: http://f10.emoney.cn/f10/zbyz/1000001

    描述: 益盟-F10-主营构成

    限量: 单次返回所有历史数据
    """
    try:
        stock_zygc_ym_df = ak.stock_zygc_ym(symbol=request.symbol)
        return stock_zygc_ym_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 益盟-F10-管理层讨论与分析
@router.post("/stock_mda_ym", operation_id="post_stock_mda_ym")
async def post_stock_mda_ym(request: SymbolRequest):
    """
    接口: stock_mda_ym

    目标地址: https://f10.emoney.cn/f10/zbyz/1000001

    描述: 益盟-F10-管理层讨论与分析

    限量: 单次返回所有历史数据
    """
    try:
        stock_mda_ym_df = ak.stock_mda_ym(symbol=request.symbol)
        return stock_mda_ym_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-个股-公司概况
@router.post("/stock_profile_cninfo", operation_id="post_stock_profile_cninfo")
async def post_stock_profile_cninfo(request: SymbolRequest):
    """
    接口: stock_profile_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/company

    描述: 巨潮资讯-个股-公司概况

    限量: 单次获取指定个股的公司概况
    """
    try:
        stock_profile_cninfo_df = ak.stock_profile_cninfo(symbol=request.symbol)
        return stock_profile_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-个股-上市相关
@router.post("/stock_ipo_summary_cninfo", operation_id="post_stock_ipo_summary_cninfo")
async def post_stock_ipo_summary_cninfo(request: SymbolRequest):
    """
    接口: stock_ipo_summary_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/company

    描述: 巨潮资讯-个股-上市相关

    限量: 单次获取指定个股的上市相关数据
    """
    try:
        stock_ipo_summary_cninfo_df = ak.stock_ipo_summary_cninfo(symbol=request.symbol)
        return stock_ipo_summary_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
