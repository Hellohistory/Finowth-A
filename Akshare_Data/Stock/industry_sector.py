import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class IndustryIndexRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str


class IndustryConsRequest(BaseModel):
    symbol: str


class IndustryHistRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    period: str
    adjust: str


class IndustryHistMinRequest(BaseModel):
    symbol: str
    period: str


@router.get("/stock_board_industry_name_em")
def get_stock_board_industry_name_em():
    """
    东方财富-沪深京板块-行业板块
    """
    try:
        stock_board_industry_name_em_df = ak.stock_board_industry_name_em()
        return stock_board_industry_name_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_board_industry_summary_ths")
def get_stock_board_industry_summary_ths():
    """
    同花顺-同花顺行业一览表
    """
    try:
        stock_board_industry_summary_ths_df = ak.stock_board_industry_summary_ths()
        return stock_board_industry_summary_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-板块-行业板块-指数日频率数据
@router.post("/stock_board_industry_index_ths")
def get_stock_board_industry_index_ths(request: IndustryIndexRequest):
    try:
        stock_board_industry_index_ths_df = ak.stock_board_industry_index_ths(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )
        return stock_board_industry_index_ths_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-行业板块-板块成份
@router.post("/stock_board_industry_cons_em")
def get_stock_board_industry_cons_em(request: IndustryConsRequest):
    try:
        stock_board_industry_cons_em_df = ak.stock_board_industry_cons_em(symbol=request.symbol)
        return stock_board_industry_cons_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-行业板块-历史行情数据
@router.post("/stock_board_industry_hist_em")
def get_stock_board_industry_hist_em(request: IndustryHistRequest):
    try:
        stock_board_industry_hist_em_df = ak.stock_board_industry_hist_em(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
            period=request.period,
            adjust=request.adjust
        )
        return stock_board_industry_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-行业板块-分时历史行情数据
@router.post("/stock_board_industry_hist_min_em")
def get_stock_board_industry_hist_min_em(request: IndustryHistMinRequest):
    try:
        stock_board_industry_hist_min_em_df = ak.stock_board_industry_hist_min_em(
            symbol=request.symbol,
            period=request.period
        )
        return stock_board_industry_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
