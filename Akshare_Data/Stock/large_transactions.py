# 大宗交易

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 市场统计
@router.get("/stock_dzjy_sctj", operation_id="get_stock_dzjy_sctj")
def get_stock_dzjy_sctj():
    """
    东方财富-大宗交易-市场统计

    接口: stock_dzjy_sctj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_sctj.aspx

    描述: 东方财富-数据中心-大宗交易-市场统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_sctj = ak.stock_dzjy_sctj()
        stock_dzjy_sctj_df = sanitize_data_pandas(stock_dzjy_sctj)
        return stock_dzjy_sctj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="市场类型", description="可选择 A股 , B股 , 基金 , 债券")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# 东方财富-数据中心-大宗交易-每日明细
@router.post("/stock_dzjy_mrmx", operation_id="post_stock_dzjy_mrmx")
async def post_stock_dzjy_mrmx(request: SymbolDateRequest):
    """
    东方财富-大宗交易-每日明细

    接口: stock_dzjy_mrmx

    目标地址: http://data.eastmoney.com/dzjy/dzjy_mrmxa.aspx

    描述: 东方财富-数据中心-大宗交易-每日明细

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_mrmx = ak.stock_dzjy_mrmx(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date)
        stock_dzjy_mrmx_df = sanitize_data_pandas(stock_dzjy_mrmx)
        return stock_dzjy_mrmx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


@router.post("/stock_dzjy_mrtj", operation_id="post_stock_dzjy_mrtj")
async def post_stock_dzjy_mrtj(request: DateRangeRequest):
    """
    东方财富-大宗交易-每日统计

    接口: stock_dzjy_mrtj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_mrtj.aspx

    描述: 东方财富-数据中心-大宗交易-每日统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_mrtj = ak.stock_dzjy_mrtj(start_date=request.start_date, end_date=request.end_date)
        stock_dzjy_mrtj_df = sanitize_data_pandas(stock_dzjy_mrtj)
        return stock_dzjy_mrtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiASymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期", description="可选择 近一月 , 近三月 , 近六月 , 近一年 ")


# 东方财富-数据中心-大宗交易-活跃 A 股统计
@router.post("/stock_dzjy_hygtj", operation_id="post_stock_dzjy_hygtj")
async def post_stock_dzjy_hygtj(request: DongCaiASymbolRequest):
    """
    东方财富-大宗交易-活跃 A 股统计

    接口: stock_dzjy_hygtj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_hygtj.aspx

    描述: 东方财富-数据中心-大宗交易-活跃 A 股统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_hygtj = ak.stock_dzjy_hygtj(symbol=request.symbol)
        stock_dzjy_hygtj_df = sanitize_data_pandas(stock_dzjy_hygtj)
        return stock_dzjy_hygtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiYingSymbolRequest(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择 当前交易日 , 近3日 , 近5日 , 近10日 , 近30日 ")


# 东方财富-数据中心-大宗交易-活跃营业部统计
@router.post("/stock_dzjy_hyyybtj", operation_id="post_stock_dzjy_hyyybtj")
async def post_stock_dzjy_hyyybtj(request: DongCaiYingSymbolRequest):
    """
    东方财富-大宗交易-活跃营业部统计

    接口: stock_dzjy_hyyybtj

    目标地址: http://data.eastmoney.com/dzjy/dzjy_hyyybtj.aspx

    描述: 东方财富-数据中心-大宗交易-活跃营业部统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_hyyybtj = ak.stock_dzjy_hyyybtj(symbol=request.symbol)
        stock_dzjy_hyyybtj_df = sanitize_data_pandas(stock_dzjy_hyyybtj)
        return stock_dzjy_hyyybtj_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_dzjy_yybph", operation_id="post_stock_dzjy_yybph")
async def post_stock_dzjy_yybph(request: DongCaiASymbolRequest):
    """
    东方财富-大宗交易-活跃营业部统计

    接口: stock_dzjy_yybph

    目标地址: http://data.eastmoney.com/dzjy/dzjy_yybph.aspx

    描述: 东方财富-数据中心-大宗交易-营业部排行

    限量: 单次返回所有历史数据
    """
    try:
        stock_dzjy_yybph = ak.stock_dzjy_yybph(symbol=request.symbol)
        stock_dzjy_yybph_df = sanitize_data_pandas(stock_dzjy_yybph)
        return stock_dzjy_yybph_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
