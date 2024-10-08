import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockHotXQRequest(BaseModel):
    symbol: str = Field(..., title="数据类型", description="可选择'本周新增', '最热门'")


@router.post("/stock_hot_follow_xq", operation_id="stock_hot_follow_xq")
async def stock_hot_follow_xq(request: StockHotXQRequest):
    """
    雪球-沪深股市-热度排行榜-关注排行榜

    接口: stock_hot_follow_xq

    目标地址: https://xueqiu.com/hq

    描述: 雪球-沪深股市-热度排行榜-关注排行榜

    限量: 单次返回指定个股的排行数据
    """
    try:
        stock_hot_follow_xq = ak.stock_hot_follow_xq(symbol=request.symbol)
        stock_hot_follow_xq_df = sanitize_data_pandas(stock_hot_follow_xq)
        return stock_hot_follow_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 雪球-沪深股市-热度排行榜-讨论排行榜
@router.post("/stock_hot_tweet_xq", operation_id="stock_hot_tweet_xq")
async def stock_hot_tweet_xq(request: StockHotXQRequest):
    """
    雪球-沪深股市-热度排行榜-讨论排行榜

    接口: stock_hot_tweet_xq

    目标地址: https://xueqiu.com/hq

    描述: 雪球-沪深股市-热度排行榜-讨论排行榜

    限量: 单次返回指定个股的排行数据
    """
    try:
        stock_hot_tweet_xq = ak.stock_hot_tweet_xq(symbol=request.symbol)
        stock_hot_tweet_xq_df = sanitize_data_pandas(stock_hot_tweet_xq)
        return stock_hot_tweet_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stock_hot_deal_xq", operation_id="stock_hot_deal_xq")
def stock_hot_deal_xq(request: StockHotXQRequest):
    """
    雪球-沪深股市-热度排行榜-交易排行榜

    接口: stock_hot_deal_xq

    目标地址: https://xueqiu.com/hq

    描述: 雪球-沪深股市-热度排行榜-交易排行榜

    限量: 单次返回指定个股的排行数据
    """
    try:
        stock_hot_deal_xq = ak.stock_hot_deal_xq(symbol=request.symbol)
        stock_hot_deal_xq_df = sanitize_data_pandas(stock_hot_deal_xq)
        return stock_hot_deal_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHotRankWCRequest(BaseModel):
    date: str = Field(..., title="查询日期", description="例：20230129")


@router.post("/stock_hot_rank_wc", operation_id="stock_hot_rank_wc")
def stock_hot_rank_wc(request: StockHotRankWCRequest):
    """
    问财-热门股票排名数据

    接口: stock_hot_rank_wc

    目标地址: https://www.iwencai.com/unifiedwap/home/index

    描述: 问财-热门股票排名数据; 请注意访问的频率

    限量: 单次返回近 5000 个股票的热门排名数据, 当前交易日的数据请在收盘后访问
    """
    try:
        stock_hot_rank_wc = ak.stock_hot_rank_wc(date=request.date)
        stock_hot_rank_wc_df = sanitize_data_pandas(stock_hot_rank_wc)
        return stock_hot_rank_wc_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_rank_em", operation_id="stock_hot_rank_em")
def stock_hot_rank_em():
    """
    东方财富站-股票热度

    接口: stock_hot_rank_em

    目标地址: http://guba.eastmoney.com/rank/

    描述: 东方财富站-股票热度

    限量: 单次返回当前交易日前 100 个股票的人气排名数据
    """
    try:
        stock_hot_rank_em = ak.stock_hot_rank_em()
        stock_hot_rank_em_df = sanitize_data_pandas(stock_hot_rank_em)
        return stock_hot_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_up_em", operation_id="stock_hot_up_em")
def stock_hot_up_em():
    """
    东方财富-个股人气榜-飙升榜

    接口: stock_hot_up_em

    目标地址: http://guba.eastmoney.com/rank/

    描述: 东方财富-个股人气榜-飙升榜

    限量: 单次返回当前交易日前 100 个股票的飙升榜排名数据
    """
    try:
        stock_hot_up_em = ak.stock_hot_up_em()
        stock_hot_up_em_df = sanitize_data_pandas(stock_hot_up_em)
        return stock_hot_up_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hk_hot_rank_em", operation_id="stock_hk_hot_rank_em")
def stock_hk_hot_rank_em():
    """
    东方财富-个股人气榜-人气榜-港股市场

    接口: stock_hk_hot_rank_em

    目标地址: https://guba.eastmoney.com/rank/

    描述: 东方财富-个股人气榜-人气榜-港股市场

    限量: 单次返回当前交易日前 100 个股票的人气排名数据
    """
    try:
        stock_hk_hot_rank_em = ak.stock_hk_hot_rank_em()
        stock_hk_hot_rank_em_df = sanitize_data_pandas(stock_hk_hot_rank_em)
        return stock_hk_hot_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHKHotRankDetailEMRequest(BaseModel):
    symbol: str = Field(..., title="港股代码", description="例：00700")


@router.post("/stock_hk_hot_rank_detail_em", operation_id="stock_hk_hot_rank_detail_em")
async def stock_hk_hot_rank_detail_em(request: StockHKHotRankDetailEMRequest):
    """
    东方财富-股票热度-历史趋势及粉丝特征

    接口: stock_hot_rank_detail_em

    目标地址: http://guba.eastmoney.com/rank/stock?code=000665

    描述: 东方财富-股票热度-历史趋势及粉丝特征

    限量: 单次返回指定个股的股票近期历史数据
    """
    try:
        stock_hk_hot_rank_detail_em = ak.stock_hk_hot_rank_detail_em(symbol=request.symbol)
        stock_hk_hot_rank_detail_em_df = sanitize_data_pandas(stock_hk_hot_rank_detail_em)
        return stock_hk_hot_rank_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 内部交易
@router.get("/stock_inner_trade_xq", operation_id="stock_inner_trade_xq")
def stock_inner_trade_xq():
    """
    雪球-沪深股市-内部交易

    接口: stock_inner_trade_xq

    目标地址: https://xueqiu.com/hq/insider

    描述: 雪球-行情中心-沪深股市-内部交易

    限量: 单次返回所有历史数据
    """
    try:
        stock_inner_trade_xq = ak.stock_inner_trade_xq()
        stock_inner_trade_xq_df = sanitize_data_pandas(stock_inner_trade_xq)
        return stock_inner_trade_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHotRankDetailEMRequest(BaseModel):
    symbol: str = Field(..., title="需带有市场标识个股", description="例：SZ000665")


# 个股人气榜-实时变动
@router.post("/stock_hot_rank_detail_realtime_em",
             operation_id="stock_hot_rank_detail_realtime_em")
async def stock_hot_rank_detail_realtime_em(request: StockHotRankDetailEMRequest):
    """
    东方财富-个股人气榜-实时变动

    接口: stock_hot_rank_detail_realtime_em

    目标地址: http://guba.eastmoney.com/rank/stock?code=000665

    描述: 东方财富-个股人气榜-实时变动

    限量: 单次返回指定个股的股票近期历史数据
    """
    try:
        stock_hot_rank_detail_realtime_em = ak.stock_hot_rank_detail_realtime_em(symbol=request.symbol)
        stock_hot_rank_detail_realtime_em_df = sanitize_data_pandas(stock_hot_rank_detail_realtime_em)
        return stock_hot_rank_detail_realtime_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHotRankHKDetailEMRequest(BaseModel):
    symbol: str = Field(..., title="港股代码", description="例：00700")


# 港股-个股人气榜-实时变动
@router.post("/stock_hk_hot_rank_detail_realtime_em",
             operation_id="stock_hk_hot_rank_detail_realtime_em")
async def stock_hk_hot_rank_detail_realtime_em(request: StockHotRankHKDetailEMRequest):
    """
    东方财富-个股人气榜-实时变动

    接口: stock_hk_hot_rank_detail_realtime_em

    目标地址: https://guba.eastmoney.com/rank/stock?code=HK_00700

    描述: 东方财富-个股人气榜-实时变动

    限量: 单次返回指定个股的股票近期历史数据
    """
    try:
        stock_hk_hot_rank_detail_realtime_em = ak.stock_hk_hot_rank_detail_realtime_em(symbol=request.symbol)
        stock_hk_hot_rank_detail_realtime_em_df = sanitize_data_pandas(stock_hk_hot_rank_detail_realtime_em)
        return stock_hk_hot_rank_detail_realtime_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHotKeywordRequest(BaseModel):
    symbol: str = Field(..., title="需带有市场标识个股", description="例：SZ000665")


# 热门关键词
@router.post("/stock_hot_keyword_em", operation_id="stock_hot_keyword_em")
async def stock_hot_keyword_em(request: StockHotKeywordRequest):
    """
    东方财富-个股人气榜-热门关键词

    接口: stock_hot_keyword_em

    目标地址: http://guba.eastmoney.com/rank/stock?code=000665

    描述: 东方财富-个股人气榜-热门关键词

    限量: 单次返回指定个股的最近交易日时点数据
    """
    try:
        stock_hot_keyword_em = ak.stock_hot_keyword_em(symbol=request.symbol)
        stock_hot_keyword_em_df = sanitize_data_pandas(stock_hot_keyword_em)
        return stock_hot_keyword_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 个股人气榜-最新排名
@router.post("/stock_hot_rank_latest_em", operation_id="stock_hot_rank_latest_em")
async def stock_hot_rank_latest_em(request: StockHotKeywordRequest):
    """
    东方财富-个股人气榜-最新排名

    接口: stock_hot_rank_latest_em

    目标地址: http://guba.eastmoney.com/rank/stock?code=000665

    描述: 东方财富-个股人气榜-最新排名

    限量: 单次返回指定个股的股票近期历史数据
    """
    try:
        stock_hot_rank_latest_em = ak.stock_hot_rank_latest_em(symbol=request.symbol)
        stock_hot_rank_latest_em_df = sanitize_data_pandas(stock_hot_rank_latest_em)
        return stock_hot_rank_latest_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 港股-个股人气榜-最新排名
@router.post("/stock_hk_hot_rank_latest_em", operation_id="stock_hk_hot_rank_latest_em")
async def stock_hk_hot_rank_latest_em(request: StockHotRankHKDetailEMRequest):
    """
    东方财富-个股人气榜-最新排名

    接口: stock_hk_hot_rank_latest_em

    目标地址: https://guba.eastmoney.com/rank/stock?code=HK_00700

    描述: 东方财富-个股人气榜-最新排名

    限量: 单次返回指定个股的股票近期历史数据
    """
    try:
        stock_hk_hot_rank_latest_em = ak.stock_hk_hot_rank_latest_em(symbol=request.symbol)
        stock_hk_hot_rank_latest_em_df = sanitize_data_pandas(stock_hk_hot_rank_latest_em)
        return stock_hk_hot_rank_latest_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 热搜股票
class HotSearchRequest(BaseModel):
    symbol: str = Field(..., title="数据类型",
                        description="可选择'全部','A股','港股','美股'")
    date: str = Field(..., title="指定时间", description="例：20230421")
    time: str = Field(..., title="时间周期", description="可选择'今日','1小时'")


@router.post("/stock_hot_search_baidu", operation_id="stock_hot_search_baidu")
async def stock_hot_search_baidu(request: HotSearchRequest):
    """
    百度股市通-热搜股票

    接口: stock_hot_search_baidu

    目标地址: https://gushitong.baidu.com/expressnews

    描述: 百度股市通-热搜股票

    限量: 单次返回指定类型, 日期和时段的热搜股票数据
    """
    try:
        stock_hot_search_baidu = ak.stock_hot_search_baidu(symbol=request.symbol, date=request.date,
                                                              time=request.time)
        stock_hot_search_baidu_df = sanitize_data_pandas(stock_hot_search_baidu)

        return stock_hot_search_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHotRankSymbolRequest(BaseModel):
    symbol: str = Field(..., title="需带有市场标识个股", description="例：SZ000665")


# 相关股票
@router.post("/stock_hot_rank_relate_em", operation_id="stock_hot_rank_relate_em")
async def stock_hot_rank_relate_em(request: StockHotRankSymbolRequest):
    """
    东方财富-个股人气榜-相关股票

    接口: stock_hot_rank_relate_em

    目标地址: http://guba.eastmoney.com/rank/stock?code=000665

    描述: 东方财富-个股人气榜-相关股票

    限量: 单次返回指定个股的股票近期历史数据
    """
    try:
        stock_hot_rank_relate_em = ak.stock_hot_rank_relate_em(symbol=request.symbol)
        stock_hot_rank_relate_em_df = sanitize_data_pandas(stock_hot_rank_relate_em)
        return stock_hot_rank_relate_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
