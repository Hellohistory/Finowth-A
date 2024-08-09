import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-市场情绪指数-A 股新闻情绪指数
@router.get("/index_news_sentiment_scope",
            operation_id="index_news_sentiment_scope")
def index_news_sentiment_scope():
    """
    指数数据-市场情绪指数-A 股新闻情绪指数

    接口: index_news_sentiment_scope

    目标地址: https://www.chinascope.com/reasearch.html

    描述: 数库-A股新闻情绪指数

    限量: 该接口返回近一年的 A 股新闻情绪指数数据
    """
    try:
        index_news_sentiment_scope = ak.index_news_sentiment_scope()
        data = index_news_sentiment_scope.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
