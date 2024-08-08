import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockUSIndexDailySina(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="可选择：.IXIC, .DJI, .INX, .NDX")


# 指数数据-新浪财经-美股股票指数数据-指数行情
@router.post("/index_us_stock_sina",
             operation_id="post_index_us_stock_sina")
def post_index_us_stock_sina(request: StockUSIndexDailySina):
    """
    指数数据-新浪财经-美股股票指数数据-指数行情

    接口: index_us_stock_sina

    目标地址: https://stock.finance.sina.com.cn/usstock/quotes/.IXIC.html

    描述: 新浪财经-美股指数行情
    """
    try:
        index_us_stock_sina = ak.index_us_stock_sina(
            symbol=request.symbol
        )
        index_us_stock_sina_df = sanitize_data_pandas(index_us_stock_sina)

        return index_us_stock_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
