import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class ConceptConsRequest(BaseModel):
    symbol: str


class ConceptHistRequest(BaseModel):
    symbol: str
    period: str
    start_date: str
    end_date: str
    adjust: str


class ConceptHistMinRequest(BaseModel):
    symbol: str
    period: str


@router.get("/stock_board_concept_name_em")
def get_stock_board_concept_name_em():
    """
    东方财富网-行情中心-沪深京板块-概念板块
    """
    try:
        stock_board_concept_name_em_df = ak.stock_board_concept_name_em()
        return stock_board_concept_name_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-概念板块-板块成份
@router.post("/stock_board_concept_cons_em")
def get_stock_board_concept_cons_em(request: ConceptConsRequest):
    """
    东方财富-沪深板块-概念板块-板块成份
    """
    try:
        stock_board_concept_cons_em_df = ak.stock_board_concept_cons_em(symbol=request.symbol)
        return stock_board_concept_cons_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-概念板块-历史行情数据
@router.post("/stock_board_concept_hist_em")
def get_stock_board_concept_hist_em(request: ConceptHistRequest):
    """
    东方财富-沪深板块-概念板块-历史行情数据
    """
    try:
        stock_board_concept_hist_em_df = ak.stock_board_concept_hist_em(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        return stock_board_concept_hist_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-概念板块-分时历史行情数据
@router.post("/stock_board_concept_hist_min_em")
def get_stock_board_concept_hist_min_em(request: ConceptHistMinRequest):
    """
    东方财富-沪深板块-概念板块-分时历史行情数据
    """
    try:
        stock_board_concept_hist_min_em_df = ak.stock_board_concept_hist_min_em(
            symbol=request.symbol,
            period=request.period
        )
        return stock_board_concept_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
