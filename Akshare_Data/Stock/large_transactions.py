# 大宗交易

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


# 市场统计
@router.get("/stock_dzjy_sctj", operation_id="get_stock_dzjy_sctj")
def get_stock_dzjy_sctj():
    """
    接口: stock_dzjy_sctj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_sctj.aspx

    描述: 东方财富网-数据中心-大宗交易-市场统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_sctj_df = ak.stock_dzjy_sctj()
        return stock_dzjy_sctj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_mrmx", operation_id="post_stock_dzjy_mrmx")
async def post_stock_dzjy_mrmx(request: SymbolDateRequest):
    """
    接口: stock_dzjy_mrmx

    目标地址: http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx

    描述: 东方财富网-数据中心-大宗交易-每日明细

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_mrmx_df = ak.stock_dzjy_mrmx(symbol=request.symbol, start_date=request.start_date,
                                                end_date=request.end_date)
        return stock_dzjy_mrmx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例如20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例如20240716")


@router.post("/stock_dzjy_mrtj", operation_id="post_stock_dzjy_mrtj")
async def post_stock_dzjy_mrtj(request: DateRangeRequest):
    """
    接口: stock_dzjy_mrtj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_mrtj.aspx

    描述: 东方财富网-数据中心-大宗交易-每日统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_mrtj_df = ak.stock_dzjy_mrtj(start_date=request.start_date, end_date=request.end_date)
        return stock_dzjy_mrtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiASymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期", description="可选择'近一月', '近三月', '近六月', '近一年'")


# 东方财富网-数据中心-大宗交易-活跃 A 股统计
@router.post("/stock_dzjy_hygtj", operation_id="post_stock_dzjy_hygtj")
async def post_stock_dzjy_hygtj(request: DongCaiASymbolRequest):
    """
    接口: stock_dzjy_hygtj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_hygtj.aspx

    描述: 东方财富网-数据中心-大宗交易-活跃 A 股统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_hygtj_df = ak.stock_dzjy_hygtj(symbol=request.symbol)
        return stock_dzjy_hygtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiYingSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择'当前交易日', '近3日', '近5日', '近10日', '近30日'")


# 东方财富网-数据中心-大宗交易-活跃营业部统计
@router.post("/stock_dzjy_hyyybtj", operation_id="post_stock_dzjy_hyyybtj")
async def post_stock_dzjy_hyyybtj(request: DongCaiYingSymbolRequest):
    """
    接口: stock_dzjy_hyyybtj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_hyyybtj.aspx

    描述: 东方财富网-数据中心-大宗交易-活跃营业部统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_hyyybtj_df = ak.stock_dzjy_hyyybtj(symbol=request.symbol)
        return stock_dzjy_hyyybtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_yybph", operation_id="post_stock_dzjy_yybph")
async def post_stock_dzjy_yybph(request: DongCaiASymbolRequest):
    """
    接口: stock_dzjy_yybph

    目标地址: http://data.eastmoney.com/dzjy/dzjy_yybph.aspx

    描述: 东方财富网-数据中心-大宗交易-营业部排行

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_yybph_df = ak.stock_dzjy_yybph(symbol=request.symbol)
        return stock_dzjy_yybph_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
