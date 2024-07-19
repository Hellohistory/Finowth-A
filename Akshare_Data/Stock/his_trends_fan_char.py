import akshare as ak
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/stock_hot_follow_xq")
def get_stock_hot_follow_xq(symbol: str):
    """
    雪球-沪深股市-热度排行榜-关注排行榜
    """
    try:
        stock_hot_follow_xq_df = ak.stock_hot_follow_xq(symbol=symbol)
        return stock_hot_follow_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_tweet_xq")
def get_stock_hot_tweet_xq(symbol: str):
    """
    雪球-沪深股市-热度排行榜-讨论排行榜
    """
    try:
        stock_hot_tweet_xq_df = ak.stock_hot_tweet_xq(symbol=symbol)
        return stock_hot_tweet_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_deal_xq")
def get_stock_hot_deal_xq(symbol: str):
    """
    雪球-沪深股市-热度排行榜-交易排行榜
    """
    try:
        stock_hot_deal_xq_df = ak.stock_hot_deal_xq(symbol=symbol)
        return stock_hot_deal_xq_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_rank_wc")
def get_stock_hot_rank_wc(date: str):
    """
    问财-热门股票排名数据
    """
    try:
        stock_hot_rank_wc_df = ak.stock_hot_rank_wc(date=date)
        return stock_hot_rank_wc_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_rank_em")
def get_stock_hot_rank_em():
    """
    东方财富网站-股票热度
    """
    try:
        stock_hot_rank_em_df = ak.stock_hot_rank_em()
        return stock_hot_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_up_em")
def get_stock_hot_up_em():
    """
    东方财富-个股人气榜-飙升榜
    """
    try:
        stock_hot_up_em_df = ak.stock_hot_up_em()
        return stock_hot_up_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hk_hot_rank_em")
def get_stock_hk_hot_rank_em():
    """
    东方财富-个股人气榜-人气榜-港股市场
    """
    try:
        stock_hk_hot_rank_em_df = ak.stock_hk_hot_rank_em()
        return stock_hk_hot_rank_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hot_rank_detail_em")
def get_stock_hot_rank_detail_em(symbol: str):
    """
    东方财富网-股票热度-历史趋势及粉丝特征
    """
    try:
        stock_hot_rank_detail_em_df = ak.stock_hot_rank_detail_em(symbol=symbol)
        return stock_hot_rank_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock_hk_hot_rank_detail_em")
def get_stock_hk_hot_rank_detail_em(symbol: str):
    """
    东方财富网-股票热度-历史趋势
    """
    try:
        stock_hk_hot_rank_detail_em_df = ak.stock_hk_hot_rank_detail_em(symbol=symbol)
        return stock_hk_hot_rank_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
