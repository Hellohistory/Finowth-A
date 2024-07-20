import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.request_model import SymbolRequest, StockQuarterRequest, DateRequest
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 新浪财经-机构持股-机构持股一览表
@router.post("/stock_institute_hold", operation_id="post_stock_institute_hold")
async def post_stock_institute_hold(request: SymbolRequest):
    """
    描述: 新浪财经-机构持股-机构持股一览表
    限量: 单次获取所有历史数据
    """
    try:
        stock_institute_hold_df = ak.stock_institute_hold(symbol=request.symbol)
        return stock_institute_hold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-机构持股-机构持股详情
@router.post("/stock_institute_hold_detail", operation_id="post_stock_institute_hold_detail")
async def post_stock_institute_hold_detail(request: StockQuarterRequest):
    """
    描述: 新浪财经-机构持股-机构持股详情
    限量: 单次获取所有历史数据
    """
    try:
        stock_institute_hold_detail_df = ak.stock_institute_hold_detail(stock=request.stock, quarter=request.quarter)
        return stock_institute_hold_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-机构推荐池-具体指标的数据
@router.post("/stock_institute_recommend", operation_id="post_stock_institute_recommend")
async def post_stock_institute_recommend(request: SymbolRequest):
    """
    描述: 新浪财经-机构推荐池-具体指标的数据
    限量: 单次获取新浪财经-机构推荐池-具体指标的所有数据
    """
    try:
        stock_institute_recommend_df = ak.stock_institute_recommend(symbol=request.symbol)
        return stock_institute_recommend_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 新浪财经-机构推荐池-股票评级记录
@router.post("/stock_institute_recommend_detail", operation_id="post_stock_institute_recommend_detail")
async def post_stock_institute_recommend_detail(request: SymbolRequest):
    """
    描述: 新浪财经-机构推荐池-股票评级记录
    限量: 单次获取新浪财经-机构推荐池-股票评级记录的所有数据
    """
    try:
        stock_institute_recommend_detail_df = ak.stock_institute_recommend_detail(symbol=request.symbol)
        stock_institute_recommend_detail_df = sanitize_data_pandas(stock_institute_recommend_detail_df)

        return stock_institute_recommend_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据中心-评级预测-投资评级
@router.post("/stock_rank_forecast_cninfo", operation_id="post_stock_rank_forecast_cninfo")
async def post_stock_rank_forecast_cninfo(request: DateRequest):
    """
    描述: 巨潮资讯-数据中心-评级预测-投资评级
    限量: 单次获取指定交易日的所有数据
    """
    try:
        stock_rank_forecast_cninfo_df = ak.stock_rank_forecast_cninfo(date=request.date)
        return stock_rank_forecast_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
