import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")


@router.post("/stock_a_indicator_lg", operation_id="stock_a_indicator_lg")
async def stock_a_indicator_lg(request: SymbolRequest):
    """
    乐咕乐股-A 股个股指标: 市盈率, 市净率, 股息率

    接口: stock_a_indicator_lg

    目标地址: https://www.legulegu.com/stocklist

    描述: 乐咕乐股-A 股个股指标: 市盈率, 市净率, 股息率

    限量: 单次获取指定个股的所有历史数据
    """
    try:
        stock_a_indicator_lg = ak.stock_a_indicator_lg(symbol=request.symbol)

        stock_a_indicator_lg_df = sanitize_data_pandas(stock_a_indicator_lg)

        stock_a_indicator_lg_df.rename(columns={
            "trade_date": "交易日期",
            "pe": "市盈率",
            "pe_ttm": "市盈率(TTM)",
            "pb": "市净率",
            "ps": "市销率",
            "ps_ttm": "市销率(TTM)",
            "dv_ratio": "股息率",
            "dv_ttm": "股息率(TTM)",
            "total_mv": "总市值"
        }, inplace=True)

        return stock_a_indicator_lg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
