import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


@router.post("/stock_irm_cninfo", operation_id="post_stock_irm_cninfo")
async def post_stock_irm_cninfo(request: SymbolRequest):
    """
    互动易-提问
    """
    try:
        stock_irm_cninfo_df = ak.stock_irm_cninfo(symbol=request.symbol)
        return stock_irm_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_irm_ans_cninfo", operation_id="post_stock_irm_ans_cninfo")
async def post_stock_irm_ans_cninfo(request: SymbolRequest):
    """
    互动易-回答
    """
    try:
        stock_irm_ans_cninfo_df = ak.stock_irm_ans_cninfo(symbol=request.symbol)
        return stock_irm_ans_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_sns_sseinfo", operation_id="post_stock_sns_sseinfo")
async def post_stock_sns_sseinfo(request: SymbolRequest):
    """
    上证e互动-提问与回答
    """
    try:
        stock_sns_sseinfo_df = ak.stock_sns_sseinfo(symbol=request.symbol)
        return stock_sns_sseinfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
