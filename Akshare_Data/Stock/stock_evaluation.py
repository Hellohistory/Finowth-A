import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest
from Akshare_Data.utility_function import sanitize_data

router = APIRouter()


# 东方财富网-数据中心-特色数据-千股千评
@router.get("/stock_comment_em", operation_id="get_stock_comment_em")
def get_stock_comment_em():
    """
    接口: stock_comment_em

    目标地址: https://data.eastmoney.com/stockcomment/

    描述: 东方财富网-数据中心-特色数据-千股千评

    限量: 单次获取所有数据
    """
    try:
        stock_comment_em_df = ak.stock_comment_em()
        sanitized_data = stock_comment_em_df.applymap(sanitize_data)

        return sanitized_data.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-千股千评-主力控盘-机构参与度
@router.post("/stock_comment_detail_zlkp_jgcyd_em",
             operation_id="post_stock_comment_detail_zlkp_jgcyd_em")
async def post_stock_comment_detail_zlkp_jgcyd_em(request: SymbolRequest):
    """
    接口: stock_comment_detail_zlkp_jgcyd_em

    目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

    描述: 东方财富网-数据中心-特色数据-千股千评-主力控盘-机构参与度

    限量: 单次获取所有数据
    """
    try:
        stock_comment_detail_zlkp_jgcyd_em_df = ak.stock_comment_detail_zlkp_jgcyd_em(symbol=request.symbol)
        return stock_comment_detail_zlkp_jgcyd_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-千股千评-综合评价-历史评分
@router.post("/stock_comment_detail_zhpj_lspf_em",
             operation_id="post_stock_comment_detail_zhpj_lspf_em")
async def post_stock_comment_detail_zhpj_lspf_em(request: SymbolRequest):
    """
    接口: stock_comment_detail_zhpj_lspf_em

    目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

    描述: 东方财富网-数据中心-特色数据-千股千评-综合评价-历史评分

    限量: 单次获取所有数据
    """
    try:
        stock_comment_detail_zhpj_lspf_em_df = ak.stock_comment_detail_zhpj_lspf_em(symbol=request.symbol)
        return stock_comment_detail_zhpj_lspf_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-千股千评-市场热度-用户关注指数
@router.post("/stock_comment_detail_scrd_focus_em",
             operation_id="post_stock_comment_detail_scrd_focus_em")
async def post_stock_comment_detail_scrd_focus_em(request: SymbolRequest):
    """
    接口: stock_comment_detail_scrd_focus_em

    目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

    描述: 东方财富网-数据中心-特色数据-千股千评-市场热度-用户关注指数

    限量: 单次获取所有数据
    """
    try:
        stock_comment_detail_scrd_focus_em_df = ak.stock_comment_detail_scrd_focus_em(symbol=request.symbol)
        return stock_comment_detail_scrd_focus_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-千股千评-市场热度-市场参与意愿
@router.post("/stock_comment_detail_scrd_desire_em",
             operation_id="post_stock_comment_detail_scrd_desire_em")
async def post_stock_comment_detail_scrd_desire_em(request: SymbolRequest):
    """
    接口: stock_comment_detail_scrd_desire_em

    目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

    描述: 东方财富网-数据中心-特色数据-千股千评-市场热度-市场参与意愿

    限量: 单次获取所有数据
    """
    try:
        stock_comment_detail_scrd_desire_em_df = ak.stock_comment_detail_scrd_desire_em(symbol=request.symbol)
        return stock_comment_detail_scrd_desire_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-千股千评-市场热度-日度市场参与意愿
@router.post("/stock_comment_detail_scrd_desire_daily_em",
             operation_id="post_stock_comment_detail_scrd_desire_daily_em")
async def post_stock_comment_detail_scrd_desire_daily_em(request: SymbolRequest):
    """
    接口: stock_comment_detail_scrd_desire_daily_em

    目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

    描述: 东方财富网-数据中心-特色数据-千股千评-市场热度-日度市场参与意愿

    限量: 单次获取所有数据
    """
    try:
        stock_comment_detail_scrd_desire_daily_em_df = ak.stock_comment_detail_scrd_desire_daily_em(
            symbol=request.symbol)
        return stock_comment_detail_scrd_desire_daily_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-特色数据-千股千评-市场热度-市场成本
@router.post("/stock_comment_detail_scrd_cost_em",
             operation_id="post_stock_comment_detail_scrd_cost_em")
async def post_stock_comment_detail_scrd_cost_em(request: SymbolRequest):
    """
    接口: stock_comment_detail_scrd_cost_em

    目标地址: https://data.eastmoney.com/stockcomment/stock/600000.html

    描述: 东方财富网-数据中心-特色数据-千股千评-市场热度-市场成本

    限量: 单次获取所有数据
    """
    try:
        stock_comment_detail_scrd_cost_em_df = ak.stock_comment_detail_scrd_cost_em(symbol=request.symbol)
        return stock_comment_detail_scrd_cost_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
