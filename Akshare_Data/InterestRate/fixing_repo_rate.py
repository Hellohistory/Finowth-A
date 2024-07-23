import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class RepoRateHistRequest(BaseModel):
    start_date: str = Field(..., title="开始时间",
                            description="例：20200930,开始时间与结束时间需要在一年内")
    end_date: str = Field(..., title="结束时间",
                          description="例：20230129,开始时间与结束时间需要在一年内")


@router.post("/interest_repo_rate_hist", operation_id="post_interest_repo_rate_hist")
def post_interest_repo_rate_hist(request: RepoRateHistRequest):
    """
    接口: repo_rate_hist

    目标地址: https://www.chinamoney.com.cn/chinese/bkfrr/

    描述: 回购定盘利率数据

    限量: 单次返回指定日期间(一年)的所有历史数据
    """
    try:
        repo_rate_hist_df = ak.repo_rate_hist(
            start_date=request.start_date,
            end_date=request.end_date,
        )
        repo_rate_hist_df = sanitize_data_pandas(repo_rate_hist_df)

        return repo_rate_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class RepoRateSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定回购定盘利率类型", description="可选择回购定盘利率, 银银间回购定盘利率")


@router.post("/interest_repo_rate_query", operation_id="post_interest_repo_rate_query")
def post_interest_repo_rate_query(request: RepoRateSymbolRequest):
    """
    接口: stock_hot_rank_wc

    目标地址: https://www.iwencai.com/unifiedwap/home/index

    描述: 问财-热门股票排名数据; 请注意访问的频率

    限量: 单次返回近 5000 个股票的热门排名数据, 当前交易日的数据请在收盘后访问
    """
    try:
        interest_repo_rate_query_df = ak.repo_rate_query(symbol=request.symbol)
        interest_repo_rate_query_df = sanitize_data_pandas(interest_repo_rate_query_df)

        return interest_repo_rate_query_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
