import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockIndexSpotEM(BaseModel):
    symbol: str = Field(..., title="指数类型",
                        description="可选择：上证系列指数, 深证系列指数, 指数成份, 中证系列指数")


# 指数数据-东方财富-A股股票指数数据-实时行情数据
@router.post("/stock_zh_index_spot_em",
             operation_id="post_stock_zh_index_spot_em")
def post_stock_zh_index_spot_em(request: StockIndexSpotEM):
    """
    指数数据-东方财富-A股股票指数数据-实时行情数据

    接口: stock_zh_index_spot_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#index_sz

    描述: 东方财富网-行情中心-沪深京指数

    限量: 单次返回所有指数的实时行情数据
    """
    try:
        stock_zh_index_spot_em = ak.stock_zh_index_spot_em(
            symbol=request.symbol
        )
        stock_zh_index_spot_em_df = sanitize_data_pandas(stock_zh_index_spot_em)

        return stock_zh_index_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-新浪财经-A股股票指数数据-实时行情数据
@router.get("/stock_zh_index_spot_sina",
            operation_id="get_stock_zh_index_spot_sina")
def get_stock_zh_index_spot_sina():
    """
    指数数据-新浪财经-A股股票指数数据-实时行情数据

    接口: stock_zh_index_spot_sina

    目标地址: https://vip.stock.finance.sina.com.cn/mkt/#hs_s

    描述: 新浪财经-中国股票指数数据

    限量: 单次返回所有指数的实时行情数据
    """
    try:
        stock_zh_index_spot_sina = ak.stock_zh_index_spot_sina()
        data = stock_zh_index_spot_sina.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockIndexHistCsindex(BaseModel):
    symbol: str = Field(..., title="指数代码", description="例：000928")
    start_date: str = Field(..., title="开始日期", description="例：20180526")
    end_date: str = Field(..., title="结束日期", description="例：20240604")


# 指数数据-中证指数
@router.post("/stock_zh_index_hist_csindex",
             operation_id="post_stock_zh_index_hist_csindex")
def post_stock_zh_index_hist_csindex(request: StockIndexHistCsindex):
    """
    指数数据-中证指数

    接口: stock_zh_index_hist_csindex

    目标地址: https://www.csindex.com.cn/zh-CN/indices/index-detail/H30374#/indices/family/detail?indexCode=H30374

    描述: 中证指数日频率的数据

    限量: 该接口返回指定指数的开始时间和结束时间的指数日频率数据
    """
    try:
        stock_zh_index_hist_csindex = ak.stock_zh_index_hist_csindex(
            symbol=request.symbol
        )
        stock_zh_index_hist_csindex_df = sanitize_data_pandas(stock_zh_index_hist_csindex)

        return stock_zh_index_hist_csindex_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
