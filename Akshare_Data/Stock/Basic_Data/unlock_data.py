import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


# 新浪财经-发行分配-限售解禁
@router.post("/stock_restricted_release_queue_sina", operation_id="post_stock_restricted_release_queue_sina")
async def post_stock_restricted_release_queue_sina(request: SymbolRequest):
    """
    新浪财经-发行分配-限售解禁

    接口: stock_restricted_release_queue_sina

    目标地址: https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/xsjj/index.phtml?symbol=sh600000

    描述: 新浪财经-发行分配-限售解禁

    限量: 单次获取指定个股的限售解禁数据
    """
    try:
        stock_restricted_release_queue_sina = ak.stock_restricted_release_queue_sina(symbol=request.symbol)
        stock_restricted_release_queue_sina_df = sanitize_data_pandas(stock_restricted_release_queue_sina)
        return stock_restricted_release_queue_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class RestrictedReleaseSummaryRequest(BaseModel):
    symbol: str = Field(..., title="市场类型",
                        description="可选择' 全部股票 ', ' 沪市A股 ', ' 科创板 ', ' 深市A股 ', ' 创业板 ', ' 京市A股 '")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# 东方财富-数据中心-特色数据-限售股解禁
@router.post("/stock_restricted_release_summary_em", operation_id="post_stock_restricted_release_summary_em")
async def post_stock_restricted_release_summary_em(request: RestrictedReleaseSummaryRequest):
    """
    东方财富-限售股解禁

    接口: stock_restricted_release_summary_em

    目标地址: https://data.eastmoney.com/dxf/marketStatistics.html?type=day&startdate=2022-11-08&enddate=2022-12-19

    描述: 东方财富-数据中心-特色数据-限售股解禁

    限量: 单次获取指定个股在近期限售股解禁数据
    """
    try:
        stock_restricted_release_summary_em = ak.stock_restricted_release_summary_em(symbol=request.symbol,
                                                                                     start_date=request.start_date,
                                                                                     end_date=request.end_date)
        stock_restricted_release_summary_em_df = sanitize_data_pandas(stock_restricted_release_summary_em)
        return stock_restricted_release_summary_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DateRangeRequest(BaseModel):
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# 东方财富-数据中心-限售股解禁-解禁详情一览
@router.post("/stock_restricted_release_detail_em", operation_id="post_stock_restricted_release_detail_em")
async def post_stock_restricted_release_detail_em(request: DateRangeRequest):
    """
    东方财富-限售股解禁-解禁详情一览

    接口: stock_restricted_release_detail_em

    目标地址: https://data.eastmoney.com/dxf/detail.html

    描述: 东方财富-数据中心-限售股解禁-解禁详情一览

    限量: 单次获取指定时间段限售股解禁数据
    """
    try:
        stock_restricted_release_detail_em = ak.stock_restricted_release_detail_em(
            start_date=request.start_date,
            end_date=request.end_date
        )
        stock_restricted_release_detail_em_df = sanitize_data_pandas(stock_restricted_release_detail_em)
        return stock_restricted_release_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SectorSpotRequest(BaseModel):
    indicator: str = Field(..., title="概念类型", description="可选择'新浪行业', '启明星行业', '概念', '地域', '行业'")


# 新浪行业-板块行情
@router.post("/stock_sector_spot", operation_id="post_stock_sector_spot")
async def post_stock_sector_spot(request: SectorSpotRequest):
    """
    新浪行业-板块行情

    接口: stock_sector_spot

    目标地址: http://finance.sina.com.cn/stock/sl/

    描述: 新浪行业-板块行情

    限量: 单次获取指定的板块行情实时数据
    """
    try:
        stock_sector_spot = ak.stock_sector_spot(indicator=request.indicator)
        stock_sector_spot_df = sanitize_data_pandas(stock_sector_spot)
        return stock_sector_spot_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-个股限售解禁-解禁批次
@router.post("/stock_restricted_release_queue_em", operation_id="post_stock_restricted_release_queue_em")
async def post_stock_restricted_release_queue_em(request: SymbolRequest):
    """
    东方财富-个股限售解禁-解禁批次

    接口: stock_restricted_release_queue_em

    目标地址: https://data.eastmoney.com/dxf/q/600000.html

    描述: 东方财富-数据中心-个股限售解禁-解禁批次

    限量: 单次获取指定个股的解禁批次数据
    """
    try:
        stock_restricted_release_queue_em = ak.stock_restricted_release_queue_em(symbol=request.symbol)
        stock_restricted_release_queue_em_df = sanitize_data_pandas(stock_restricted_release_queue_em)
        return stock_restricted_release_queue_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SymbolDateRequest(BaseModel):
    symbol: str = Field(..., title="个股代码", description="例：600000")
    date: str = Field(..., title="时间", description="通过请求stock_restricted_release_queue_em获取")


# 东方财富-数据中心-个股限售解禁-解禁股东
@router.post("/stock_restricted_release_stockholder_em", operation_id="post_stock_restricted_release_stockholder_em")
async def post_stock_restricted_release_stockholder_em(request: SymbolDateRequest):
    """
    东方财富-个股限售解禁-解禁股东

    接口: stock_restricted_release_stockholder_em

    目标地址: https://data.eastmoney.com/dxf/q/600000.html

    描述: 东方财富-数据中心-个股限售解禁-解禁股东

    限量: 单次获取指定个股的解禁股东数据
    """
    try:
        stock_restricted_release_stockholder_em = ak.stock_restricted_release_stockholder_em(
            symbol=request.symbol,
            date=request.date
        )
        stock_restricted_release_stockholder_em_df = sanitize_data_pandas(stock_restricted_release_stockholder_em)
        return stock_restricted_release_stockholder_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
