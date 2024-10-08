import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class ExecutiveSymbolRequest(BaseModel):
    symbol: str = Field(..., title="请求类型", description="从以下选择: '全部', '股东增持', '股东减持'")


# 东方财富-数据中心-特色数据-高管持股
@router.post("/stock_ggcg_em", operation_id="stock_ggcg_em")
async def stock_ggcg_em(request: ExecutiveSymbolRequest):
    """
    东方财富-高管持股

    接口: stock_ggcg_em

    目标地址: http://data.eastmoney.com/executive/gdzjc.html

    描述: 东方财富-数据中心-特色数据-高管持股

    限量: 单次获取所有高管持股数据数据
    """
    try:
        stock_ggcg_em = ak.stock_ggcg_em(symbol=request.symbol)
        stock_ggcg_em_df = sanitize_data_pandas(stock_ggcg_em)
        return stock_ggcg_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ChouMaSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定个股代码", description="例：000066")
    adjust: str = Field(..., title="复权种类",
                        description="可选择: 'qfq': '前复权', 'hfq': '后复权', "": '不复权'")


# 东方财富-概念板-行情中心-日K-筹码分布
@router.post("/stock_cyq_em", operation_id="stock_cyq_em")
async def stock_cyq_em(request: ChouMaSymbolRequest):
    """
    东方财富-概念板-日K-筹码分布

    接口: stock_cyq_em

    目标地址: https://quote.eastmoney.com/concept/sz000001.html

    描述: 东方财富-概念板-行情中心-日K-筹码分布

    限量: 单次返回指定个股和指定复权种类的近 90 个交易日数据
    """
    try:
        stock_cyq_em = ak.stock_cyq_em(
            symbol=request.symbol,
            adjust=request.adjust
        )
        stock_cyq_em_df = sanitize_data_pandas(stock_cyq_em)
        return stock_cyq_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class StockYzxdrRequest(BaseModel):
    date: str = Field(..., title="每年的季度末时间点", description="例：20200930")


# 一致行动人
@router.post("/stock_yzxdr_em", operation_id="stock_yzxdr_em")
def stock_yzxdr_em(request: StockYzxdrRequest):
    """
    东方财富-一致行动人

    接口: stock_yzxdr_em

    目标地址: http://data.eastmoney.com/yzxdr/

    描述: 东方财富-数据中心-特色数据-一致行动人

    限量: 单次返回所有历史数据
    """
    try:
        stock_yzxdr_em = ak.stock_yzxdr_em(date=request.date)
        stock_yzxdr_em_df = sanitize_data_pandas(stock_yzxdr_em)
        return stock_yzxdr_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 赚钱效应分析
@router.get("/stock_market_activity_legu", operation_id="stock_market_activity_legu")
def stock_market_activity_legu():
    """
    乐咕乐股-赚钱效应分析数据

    接口: stock_market_activity_legu

    目标地址: https://www.legulegu.com/stockdata/market-activity

    描述: 乐咕乐股-赚钱效应分析数据

    限量: 单次返回当前赚钱效应分析数据
    """
    try:
        stock_market_activity_legu = ak.stock_market_activity_legu()
        stock_market_activity_legu_df = sanitize_data_pandas(stock_market_activity_legu)
        return stock_market_activity_legu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
