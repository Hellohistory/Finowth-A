import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockUSIndexDailySina(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="可通过 index_stock_info 获取一览表")


# 指数数据-新浪财经-中国股票指数成份-最新成份
@router.post("/index_stock_cons",
             operation_id="post_index_stock_cons")
def post_index_stock_cons(request: StockUSIndexDailySina):
    """
    指数数据-新浪财经-中国股票指数成份-最新成份

    接口: index_stock_cons

    目标地址: http://vip.stock.finance.sina.com.cn/corp/view/vII_NewestComponent.php?page=1&indexid=399639

    描述: 指定指数的最新成份股票信息, 注意该接口返回的数据有部分是重复会导致数据缺失,
    可以调用 index_stock_cons_sina 获取主流指数数据,
    或调用 index_stock_cons_csindex 获取中证指数网提供的成分数据
    """
    try:
        index_stock_cons = ak.index_stock_cons(
            symbol=request.symbol
        )
        index_stock_cons_df = sanitize_data_pandas(index_stock_cons)

        return index_stock_cons_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-新浪财经-A股股票指数数据-实时行情数据
@router.get("/index_stock_info",
            operation_id="get_index_stock_info")
def get_index_stock_info():
    """
    指数数据-股指一览表

    接口: index_stock_info
    """
    try:
        index_stock_info = ak.index_stock_info()
        data = index_stock_info.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexStockConsCsindex(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：000300")


# 指数数据-新浪财经-中国股票指数成份-中证指数成份股
@router.post("/index_stock_cons_csindex",
             operation_id="post_index_stock_cons_csindex")
def post_index_stock_cons_csindex(request: IndexStockConsCsindex):
    """
    指数数据-新浪财经-中国股票指数成份-中证指数成份股

    接口: index_stock_cons_csindex

    目标地址: http://www.csindex.com.cn/zh-CN/indices/index-detail/000300

    描述: 中证指数网站-成份股目录
    """
    try:
        index_stock_cons_csindex = ak.index_stock_cons_csindex(
            symbol=request.symbol
        )
        index_stock_cons_df = sanitize_data_pandas(index_stock_cons_csindex)

        return index_stock_cons_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-新浪财经-中国股票指数成份-中证指数成份股权重
@router.post("/index_stock_cons_weight_csindex",
             operation_id="post_index_stock_cons_weight_csindex")
def post_index_stock_cons_weight_csindex(request: IndexStockConsCsindex):
    """
    指数数据-新浪财经-中国股票指数成份-中证指数成份股权重

    接口: index_stock_cons_weight_csindex

    目标地址: http://www.csindex.com.cn/zh-CN/indices/index-detail/000300

    描述: 中证指数网站-成份股权重
    """
    try:
        index_stock_cons_weight_csindex = ak.index_stock_cons_weight_csindex(
            symbol=request.symbol
        )
        index_stock_cons_weight_csindex_df = sanitize_data_pandas(index_stock_cons_weight_csindex)

        return index_stock_cons_weight_csindex_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
