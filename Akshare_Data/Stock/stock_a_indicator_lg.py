import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.request_model import SymbolRequest
from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


@router.post("/stock_a_indicator_lg", operation_id="post_stock_a_indicator_lg")
async def post_stock_a_indicator_lg(request: SymbolRequest):
    """
    接口: stock_a_indicator_lg

    目标地址: https://www.legulegu.com/stocklist

    描述: 乐咕乐股-A 股个股指标: 市盈率, 市净率, 股息率

    限量: 单次获取指定个股的所有历史数据
    """
    try:
        stock_a_indicator_lg_df = ak.stock_a_indicator_lg(symbol=request.symbol)
        stock_a_indicator_lg_df = sanitize_data_pandas(stock_a_indicator_lg_df)

        return stock_a_indicator_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
