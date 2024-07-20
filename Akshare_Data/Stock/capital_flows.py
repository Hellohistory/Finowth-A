import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, SymbolMarketRequest, IndicatorRequest, SectorRequest
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 同花顺-数据中心-资金流向-个股资金流
@router.post("/stock_fund_flow_individual", operation_id="post_stock_fund_flow_individual")
async def post_stock_fund_flow_individual(request: SymbolRequest):
    """
    接口: stock_fund_flow_individual
    描述: 同花顺-数据中心-资金流向-个股资金流
    限量: 单次获取指定 symbol 的概念资金流数据
    """
    try:
        stock_fund_flow_individual_df = ak.stock_fund_flow_individual(symbol=request.symbol)
        return stock_fund_flow_individual_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-数据中心-资金流向-概念资金流
@router.post("/stock_fund_flow_concept", operation_id="post_stock_fund_flow_concept")
async def post_stock_fund_flow_concept(request: SymbolRequest):
    """
    接口: stock_fund_flow_concept
    描述: 同花顺-数据中心-资金流向-概念资金流
    限量: 单次获取指定 symbol 的概念资金流数据
    """
    try:
        stock_fund_flow_concept_df = ak.stock_fund_flow_concept(symbol=request.symbol)
        return stock_fund_flow_concept_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-数据中心-资金流向-行业资金流
@router.post("/stock_fund_flow_industry", operation_id="post_stock_fund_flow_industry")
async def post_stock_fund_flow_industry(request: SymbolRequest):
    """
    接口: stock_fund_flow_industry
    描述: 同花顺-数据中心-资金流向-行业资金流
    限量: 单次获取指定 symbol 的行业资金流数据
    """
    try:
        stock_fund_flow_industry_df = ak.stock_fund_flow_industry(symbol=request.symbol)
        return stock_fund_flow_industry_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-数据中心-资金流向-大单追踪
@router.get("/stock_fund_flow_big_deal", operation_id="get_stock_fund_flow_big_deal")
def get_stock_fund_flow_big_deal():
    """
    接口: stock_fund_flow_big_deal
    描述: 同花顺-数据中心-资金流向-大单追踪
    限量: 单次获取当前时点的所有大单追踪数据
    """
    try:
        stock_fund_flow_big_deal_df = ak.stock_fund_flow_big_deal()
        return stock_fund_flow_big_deal_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-个股资金流向
@router.post("/stock_individual_fund_flow", operation_id="post_stock_individual_fund_flow")
async def post_stock_individual_fund_flow(request: SymbolMarketRequest):
    """
    接口: stock_individual_fund_flow
    描述: 东方财富网-数据中心-个股资金流向
    限量: 单次获取指定市场和股票的近 100 个交易日的资金流数据
    """
    try:
        stock_individual_fund_flow_df = ak.stock_individual_fund_flow(stock=request.stock, market=request.market)
        return stock_individual_fund_flow_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-排名
@router.post("/stock_individual_fund_flow_rank", operation_id="post_stock_individual_fund_flow_rank")
async def post_stock_individual_fund_flow_rank(request: IndicatorRequest):
    """
    接口: stock_individual_fund_flow_rank
    描述: 东方财富网-数据中心-资金流向-排名
    限量: 单次获取指定类型的个股资金流排名数据
    """
    try:
        stock_individual_fund_flow_rank_df = ak.stock_individual_fund_flow_rank(indicator=request.indicator)
        return stock_individual_fund_flow_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-大盘
@router.get("/stock_market_fund_flow", operation_id="get_stock_market_fund_flow")
def get_stock_market_fund_flow():
    """
    接口: stock_market_fund_flow
    描述: 东方财富网-数据中心-资金流向-大盘
    限量: 单次获取大盘资金流向历史数据
    """
    try:
        stock_market_fund_flow_df = ak.stock_market_fund_flow()
        return stock_market_fund_flow_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-板块资金流-排名
@router.post("/stock_sector_fund_flow_rank", operation_id="post_stock_sector_fund_flow_rank")
async def post_stock_sector_fund_flow_rank(request: SectorRequest):
    """
    接口: stock_sector_fund_flow_rank
    描述: 东方财富网-数据中心-资金流向-板块资金流-排名
    限量: 单次获取指定板块的指定期限的资金流排名数据
    """
    try:
        stock_sector_fund_flow_rank_df = ak.stock_sector_fund_flow_rank(indicator=request.indicator,
                                                                        sector_type=request.sector_type)
        return stock_sector_fund_flow_rank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-主力净流入排名


# 主力净流入排名
@router.post("/stock_main_fund_flow", operation_id="post_stock_main_fund_flow")
async def post_stock_main_fund_flow(request: SymbolRequest):
    """
    接口: stock_main_fund_flow
    描述: 东方财富网-数据中心-资金流向-主力净流入排名
    限量: 单次获取指定板块的主力净流入排名数据
    """
    try:
        stock_main_fund_flow_df = ak.stock_main_fund_flow(symbol=request.symbol)
        stock_main_fund_flow_df = sanitize_data_pandas(stock_main_fund_flow_df)

        return stock_main_fund_flow_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-行业资金流-xx行业个股资金流
@router.post("/stock_sector_fund_flow_summary", operation_id="post_stock_sector_fund_flow_summary")
async def post_stock_sector_fund_flow_summary(request: SymbolRequest):
    """
    接口: stock_sector_fund_flow_summary
    描述: 东方财富网-数据中心-资金流向-行业资金流-xx行业个股资金流
    限量: 单次获取指定行业的个股资金流
    """
    try:
        stock_sector_fund_flow_summary_df = ak.stock_sector_fund_flow_summary(symbol=request.symbol, indicator="今日")
        stock_sector_fund_flow_summary_df = sanitize_data_pandas(stock_sector_fund_flow_summary_df)

        return stock_sector_fund_flow_summary_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-行业资金流-行业历史资金流
@router.post("/stock_sector_fund_flow_hist", operation_id="post_stock_sector_fund_flow_hist")
async def post_stock_sector_fund_flow_hist(request: SymbolRequest):
    """
    接口: stock_sector_fund_flow_hist
    描述: 东方财富网-数据中心-资金流向-行业资金流-行业历史资金流
    限量: 单次获取指定行业的行业历史资金流数据
    """
    try:
        stock_sector_fund_flow_hist_df = ak.stock_sector_fund_flow_hist(symbol=request.symbol)
        return stock_sector_fund_flow_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-数据中心-资金流向-概念资金流-概念历史资金流
@router.post("/stock_concept_fund_flow_hist", operation_id="post_stock_concept_fund_flow_hist")
async def post_stock_concept_fund_flow_hist(request: SymbolRequest):
    """
    接口: stock_concept_fund_flow_hist
    描述: 东方财富网-数据中心-资金流向-概念资金流-概念历史资金流
    限量: 单次获取指定 symbol 的近期概念历史资金流数据
    """
    try:
        stock_concept_fund_flow_hist_df = ak.stock_concept_fund_flow_hist(symbol=request.symbol)
        return stock_concept_fund_flow_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
