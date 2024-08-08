import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-新浪财经-港股股票指数数据-实时行情数据
@router.get("/stock_hk_index_spot_sina",
            operation_id="get_stock_hk_index_spot_sina")
def get_stock_hk_index_spot_sina():
    """
    指数数据-新浪财经-A股股票指数数据-实时行情数据

    接口: stock_hk_index_spot_sina

    目标地址: https://vip.stock.finance.sina.com.cn/mkt/#zs_hk

    描述: 新浪财经-行情中心-港股指数

    限量: 单次返回所有数据
    """
    try:
        stock_hk_index_spot_sina = ak.stock_hk_index_spot_sina()
        data = stock_hk_index_spot_sina.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHKIndexDailySina(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：CES100")


# 指数数据-东方财富-港股股票指数数据-历史行情数据
@router.post("/stock_hk_index_daily_sina",
             operation_id="post_stock_hk_index_daily_sina")
def post_stock_hk_index_daily_sina(request: StockHKIndexDailySina):
    """
    指数数据-东方财富-历史行情数据-通用

    接口: stock_hk_index_daily_sina

    目标地址: https://stock.finance.sina.com.cn/hkstock/quotes/CES100.html

    描述: 新浪财经-港股指数-历史行情数据

    限量: 单次返回指定 symbol 的所有数据
    """
    try:
        stock_hk_index_daily_sina = ak.stock_hk_index_daily_sina(
            symbol=request.symbol
        )
        stock_hk_index_daily_sina_df = sanitize_data_pandas(stock_hk_index_daily_sina)

        return stock_hk_index_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-东方财富-港股股票指数数据-实时行情数据
@router.get("/stock_hk_index_spot_em",
            operation_id="get_stock_hk_index_spot_em")
def get_stock_hk_index_spot_em():
    """
    指数数据-东方财富-A股股票指数数据-实时行情数据

    接口: stock_hk_index_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#hk_index

    描述: 东方财富网-行情中心-港股-指数实时行情

    限量: 单次返回所有数据
    """
    try:
        stock_hk_index_spot_em = ak.stock_hk_index_spot_em()
        data = stock_hk_index_spot_em.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockHKIndexDailySina(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：HSTECF2L，可通过 stock_hk_index_spot_em 获取")


# 指数数据-东方财富-港股股票指数数据-历史行情数据
@router.post("/stock_hk_index_daily_em",
             operation_id="post_stock_hk_index_daily_em")
def post_stock_hk_index_daily_em(request: StockHKIndexDailySina):
    """
    指数数据-东方财富-港股股票指数数据-历史行情数据

    接口: stock_hk_index_daily_em

    目标地址: https://quote.eastmoney.com/gb/zsHSTECF2L.html

    描述: 东方财富网-港股-股票指数数据

    限量: 单次返回指定代码的所有数据
    """
    try:
        stock_hk_index_daily_em = ak.stock_hk_index_daily_em(
            symbol=request.symbol
        )
        stock_hk_index_daily_em_df = sanitize_data_pandas(stock_hk_index_daily_em)

        return stock_hk_index_daily_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
