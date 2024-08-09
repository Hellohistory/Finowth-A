import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockZHIndexValueCsindex(BaseModel):
    symbol: str = Field(..., title="指数代码", description="例：H30374")


# 指数数据-指数估值-指数估值-中证
@router.post("/stock_zh_index_value_csindex",
             operation_id="stock_zh_index_value_csindex")
def stock_zh_index_value_csindex(request: StockZHIndexValueCsindex):
    """
    指数数据-指数估值-指数估值-中证

    接口: stock_zh_index_value_csindex

    目标地址: https://www.csindex.com.cn/zh-CN/indices/index-detail/H30374#/indices/family/detail?indexCode=H30374

    描述: 中证指数-指数估值数据

    限量: 该接口返回指定的指数的估值数据, 该接口只能返回近期的数据
    """
    try:
        stock_zh_index_value_csindex = ak.stock_zh_index_value_csindex(
            symbol=request.symbol
        )
        stock_zh_index_value_csindex_df = sanitize_data_pandas(stock_zh_index_value_csindex)

        return stock_zh_index_value_csindex_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-指数估值-指数信息-韭圈儿
@router.get("/index_value_name_funddb", operation_id="index_value_name_funddb")
def index_value_name_funddb():
    """
    指数数据-指数估值-指数估值-指数信息-韭圈儿

    接口: index_value_name_funddb

    目标地址: https://funddb.cn/site/index

    描述: funddb-指数估值-指数信息

    限量: 该接口返回所有指数的基本信息
    """
    try:
        index_value_name_funddb = ak.index_value_name_funddb()
        data = index_value_name_funddb.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexValueHistFunddb(BaseModel):
    symbol: str = Field(..., title="指数名称",
                        description="例：创业板成长，可通过 index_value_name_funddb 获取")
    indicator: str = Field(..., title="获取类型",
                           description="可选择 市盈率 , 市净率 , 股息率 , 风险溢价 ")


# 指数数据-指数估值-中证
@router.post("/index_value_hist_funddb", operation_id="index_value_hist_funddb")
def index_value_hist_funddb(request: IndexValueHistFunddb):
    """
    指数数据-指数估值-指数估值-中证

    接口: index_value_hist_funddb

    目标地址: https://funddb.cn/site/index

    描述: funddb-指数估值-估值信息

    限量: 该接口返回指定指数和指标的估值数据
    """
    try:
        index_value_hist_funddb = ak.index_value_hist_funddb(
            symbol=request.symbol,
            indicator=request.indicator
        )
        index_value_hist_funddb_df = sanitize_data_pandas(index_value_hist_funddb)

        return index_value_hist_funddb_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexValueHistFunddb(BaseModel):
    symbol: str = Field(..., title="指数类型",
                        description="可选择：上证指数, 沪深300")


# 指数数据-估值情绪-恐惧贪婪指数
@router.post("/index_fear_greed_funddb",
             operation_id="index_fear_greed_funddb")
def index_fear_greed_funddb(request: IndexValueHistFunddb):
    """
    指数数据-估值情绪-恐惧贪婪指数

    接口: index_fear_greed_funddb

    目标地址: https://funddb.cn/tool/fear

    描述: funddb-工具-估值情绪-恐惧贪婪指数

    限量: 单次返回所有数据
    """
    try:
        index_fear_greed_funddb = ak.index_fear_greed_funddb(
            symbol=request.symbol
        )
        index_fear_greed_funddb_df = sanitize_data_pandas(index_fear_greed_funddb)

        return index_fear_greed_funddb_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
