import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


class DateRangeRequest(BaseModel):
    start_date: str
    end_date: str


class SymbolDateRequest(BaseModel):
    symbol: str
    date: str


class RestrictedReleaseSummaryRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


# 新浪财经-发行分配-限售解禁
@router.post("/stock_restricted_release_queue_sina")
def get_stock_restricted_release_queue_sina(request: SymbolRequest):
    """
    描述: 新浪财经-发行分配-限售解禁
    限量: 单次获取指定 symbol 的限售解禁数据
    """
    try:
        stock_restricted_release_queue_sina_df = ak.stock_restricted_release_queue_sina(symbol=request.symbol)
        return stock_restricted_release_queue_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-限售股解禁
@router.post("/stock_restricted_release_summary_em")
def get_stock_restricted_release_summary_em(request: RestrictedReleaseSummaryRequest):
    """
    描述: 东方财富网-数据中心-特色数据-限售股解禁
    限量: 单次获取指定 symbol 在近期限售股解禁数据
    """
    try:
        stock_restricted_release_summary_em_df = ak.stock_restricted_release_summary_em(symbol=request.symbol,
                                                                                        start_date=request.start_date,
                                                                                        end_date=request.end_date)
        return stock_restricted_release_summary_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-限售股解禁-解禁详情一览
@router.post("/stock_restricted_release_detail_em")
def get_stock_restricted_release_detail_em(request: DateRangeRequest):
    """
    描述: 东方财富网-数据中心-限售股解禁-解禁详情一览
    限量: 单次获取指定时间段限售股解禁数据
    """
    try:
        stock_restricted_release_detail_em_df = ak.stock_restricted_release_detail_em(start_date=request.start_date,
                                                                                      end_date=request.end_date)
        stock_restricted_release_detail_em_df = sanitize_data_pandas(stock_restricted_release_detail_em_df)

        return stock_restricted_release_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-个股限售解禁-解禁批次
@router.post("/stock_restricted_release_queue_em")
def get_stock_restricted_release_queue_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-个股限售解禁-解禁批次
    限量: 单次获取指定 symbol 的解禁批次数据
    """
    try:
        stock_restricted_release_queue_em_df = ak.stock_restricted_release_queue_em(symbol=request.symbol)
        return stock_restricted_release_queue_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-个股限售解禁-解禁股东
@router.post("/stock_restricted_release_stockholder_em")
def get_stock_restricted_release_stockholder_em(request: SymbolDateRequest):
    """
    描述: 东方财富网-数据中心-个股限售解禁-解禁股东
    限量: 单次获取指定 symbol 的解禁批次数据
    """
    try:
        stock_restricted_release_stockholder_em_df = ak.stock_restricted_release_stockholder_em(symbol=request.symbol,
                                                                                                date=request.date)
        return stock_restricted_release_stockholder_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
