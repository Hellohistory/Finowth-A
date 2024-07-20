import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.request_model import SymbolRequest

router = APIRouter()


@router.post("/stock_irm_cninfo", operation_id="post_stock_irm_cninfo")
async def post_stock_irm_cninfo(request: SymbolRequest):
    """
    接口: stock_irm_cninfo

    目标地址: https://irm.cninfo.com.cn/

    描述: 互动易-提问

    限量: 单次返回近期 10000 条提问数据

    请求类型: `POST`
    """
    try:
        stock_irm_cninfo_df = ak.stock_irm_cninfo(symbol=request.symbol)
        return stock_irm_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_irm_ans_cninfo", operation_id="post_stock_irm_ans_cninfo")
async def post_stock_irm_ans_cninfo(request: SymbolRequest):
    """
    接口: stock_irm_ans_cninfo

    目标地址: https://irm.cninfo.com.cn/

    描述: 互动易-回答

    限量: 单次返回指定个股的回答数据

    请求类型: `POST`
    """
    try:
        stock_irm_ans_cninfo_df = ak.stock_irm_ans_cninfo(symbol=request.symbol)
        return stock_irm_ans_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_sns_sseinfo", operation_id="post_stock_sns_sseinfo")
async def post_stock_sns_sseinfo(request: SymbolRequest):
    """
    接口: stock_sns_sseinfo

    目标地址: https://sns.sseinfo.com/company.do?uid=65

    描述: 上证e互动-提问与回答

    限量: 单次返回指定个股的提问与回答数据

    请求类型: `POST`
    """
    try:
        stock_sns_sseinfo_df = ak.stock_sns_sseinfo(symbol=request.symbol)
        return stock_sns_sseinfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
