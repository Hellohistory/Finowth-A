import akshare as ak
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/stock_irm_cninfo")
def get_stock_irm_cninfo(symbol: str):
    """
    互动易-提问
    """
    try:
        stock_irm_cninfo_df = ak.stock_irm_cninfo(symbol=symbol)
        return stock_irm_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_irm_ans_cninfo")
def get_stock_irm_ans_cninfo(symbol: str):
    """
    互动易-回答
    """
    try:
        stock_irm_ans_cninfo_df = ak.stock_irm_ans_cninfo(symbol=symbol)
        return stock_irm_ans_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_sns_sseinfo")
def get_stock_sns_sseinfo(symbol: str):
    """
    上证e互动-提问与回答
    """
    try:
        stock_sns_sseinfo_df = ak.stock_sns_sseinfo(symbol=symbol)
        return stock_sns_sseinfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
