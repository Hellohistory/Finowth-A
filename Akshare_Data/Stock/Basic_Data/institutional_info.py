import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class XinLangSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定数据时间",
                        description="数据从2005年开始, 其中'一季报':1, '中报':2 '三季报':3 '年报':4"
                                    "示例: '20191', 其中的 1 表示一季报; '20193', 其中的 3 表示三季报;")


# 新浪财经-机构持股-机构持股一览表
@router.post("/stock_institute_hold", operation_id="post_stock_institute_hold")
async def post_stock_institute_hold(request: XinLangSymbolRequest):
    """
    接口: stock_institute_hold

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml

    描述: 新浪财经-机构持股-机构持股一览表

    限量: 单次获取所有历史数据
    """
    try:
        stock_institute_hold_df = ak.stock_institute_hold(symbol=request.symbol)
        return stock_institute_hold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangStockQuarterRequest(BaseModel):
    stock: str = Field(..., title="股票代码", description="例：300003")
    quarter: str = Field(..., title="指定数据时间",
                         description="数据从2005 年开始,'一季报':1, '中报':2 '三季报':3 '年报':4"
                                     "示例: '20191', 其中的 1 表示一季报; '20193', 其中的 3 表示三季报;")


# 新浪财经-机构持股-机构持股详情
@router.post("/stock_institute_hold_detail", operation_id="post_stock_institute_hold_detail")
async def post_stock_institute_hold_detail(request: XinLangStockQuarterRequest):
    """
    接口: stock_institute_hold_detail

    目标地址: http://vip.stock.finance.sina.com.cn/q/go.php/vComStockHold/kind/jgcg/index.phtml

    描述: 新浪财经-机构持股-机构持股详情

    限量: 单次所有历史数据
    """
    try:
        stock_institute_hold_detail_df = ak.stock_institute_hold_detail(stock=request.stock, quarter=request.quarter)
        return stock_institute_hold_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class XinLangJiGouSymbolRequest(BaseModel):
    symbol: str = Field(..., title="数据指标",
                        description="可选择'最新投资评级', '上调评级股票', '下调评级股票', '股票综合评级', "
                                    "'首次评级股票', '目标涨幅排名', '机构关注度', '行业关注度', '投资评级选股'")


# 新浪财经-机构推荐池-具体指标的数据
@router.post("/stock_institute_recommend", operation_id="post_stock_institute_recommend")
async def post_stock_institute_recommend(request: XinLangJiGouSymbolRequest):
    """
    接口: stock_institute_recommend

    目标地址: http://stock.finance.sina.com.cn/stock/go.php/vIR_RatingNewest/index.phtml

    描述: 新浪财经-机构推荐池-具体指标的数据

    限量: 单次获取新浪财经-机构推荐池-具体指标的所有数据
    """
    try:
        stock_institute_recommend_df = ak.stock_institute_recommend(symbol=request.symbol)
        return stock_institute_recommend_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 新浪财经-机构推荐池-股票评级记录
@router.post("/stock_institute_recommend_detail", operation_id="post_stock_institute_recommend_detail")
async def post_stock_institute_recommend_detail(request: SymbolRequest):
    """
    接口: stock_institute_recommend_detail

    目标地址: http://stock.finance.sina.com.cn/stock/go.php/vIR_StockSearch/key/sz000001.phtml

    描述: 新浪财经-机构推荐池-股票评级记录

    限量: 单次获取新浪财经-机构推荐池-股票评级记录的所有数据
    """
    try:
        stock_institute_recommend_detail_df = ak.stock_institute_recommend_detail(symbol=request.symbol)
        stock_institute_recommend_detail_df = sanitize_data_pandas(stock_institute_recommend_detail_df)

        return stock_institute_recommend_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20230808")


# 巨潮资讯-数据中心-评级预测-投资评级
@router.post("/stock_rank_forecast_cninfo", operation_id="post_stock_rank_forecast_cninfo")
async def post_stock_rank_forecast_cninfo(request: DateRequest):
    """
    接口: stock_rank_forecast_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics?name=%E6%8A%95%E8%B5%84%E8%AF%84%E7%BA%A7

    描述: 巨潮资讯-数据中心-评级预测-投资评级

    限量: 单次获取指定交易日的所有数据
    """
    try:
        stock_rank_forecast_cninfo_df = ak.stock_rank_forecast_cninfo(date=request.date)
        return stock_rank_forecast_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
