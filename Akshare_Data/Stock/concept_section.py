import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.request_model import ConceptHistRequest, ConceptHistMinRequest, SymbolRequest

router = APIRouter()


@router.get("/stock_board_concept_name_em", operation_id="get_stock_board_concept_name_em")
def get_stock_board_concept_name_em():
    """
    接口: stock_board_concept_name_em

    目标地址: https://quote.eastmoney.com/center/boardlist.html#concept_board

    描述: 东方财富网-行情中心-沪深京板块-概念板块

    限量: 单次返回当前时刻所有概念板块数据

    请求类型: `GET`
    """
    try:
        stock_board_concept_name_em_df = ak.stock_board_concept_name_em()
        return stock_board_concept_name_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-概念板块-板块成份
@router.post("/stock_board_concept_cons_em", operation_id="post_stock_board_concept_cons_em")
async def post_stock_board_concept_cons_em(request: SymbolRequest):
    """
    接口: stock_board_concept_cons_em

    目标地址: http://quote.eastmoney.com/center/boardlist.html#boards-BK06551(示例)

    描述: 东方财富-沪深板块-概念板块-板块成份

    限量: 单次返回当前时刻所有成份股

    请求类型: `POST`
    """
    try:
        stock_board_concept_cons_em_df = ak.stock_board_concept_cons_em(symbol=request.symbol)
        return stock_board_concept_cons_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-沪深板块-概念板块-历史行情数据
@router.post("/stock_board_concept_hist_em", operation_id="post_stock_board_concept_hist_em")
async def post_stock_board_concept_hist_em(request: ConceptHistRequest):
    """
    接口: stock_board_concept_hist_em

    目标地址: http://quote.eastmoney.com/bk/90.BK0715.html(示例)

    描述: 东方财富-沪深板块-概念板块-历史行情数据

    限量: 单次返回指定个股和 adjust 的历史数据

    请求类型: `POST`
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
@router.post("/stock_board_concept_hist_min_em", operation_id="post_stock_board_concept_hist_min_em")
async def post_stock_board_concept_hist_min_em(request: ConceptHistMinRequest):
    """
    接口: stock_board_concept_hist_min_em

    目标地址: http://quote.eastmoney.com/bk/90.BK0715.html

    描述: 东方财富-沪深板块-概念板块-分时历史行情数据

    限量: 单次返回指定个股和 period 的历史数据

    请求类型: `POST`
    """
    try:
        stock_board_concept_hist_min_em_df = ak.stock_board_concept_hist_min_em(
            symbol=request.symbol,
            period=request.period
        )
        return stock_board_concept_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
