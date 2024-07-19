import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SymbolRequest(BaseModel):
    symbol: str


# 东方财富网-数据中心-特色数据-高管持股
@router.post("/stock_ggcg_em")
def get_stock_ggcg_em(request: SymbolRequest):
    """
    描述: 东方财富网-数据中心-特色数据-高管持股
    限量: 单次获取所有高管持股数据数据
    """
    try:
        stock_ggcg_em_df = ak.stock_ggcg_em(symbol=request.symbol)
        stock_us_famous_spot_em_df = sanitize_data_pandas(stock_ggcg_em_df)

        return stock_us_famous_spot_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富网-概念板-行情中心-日K-筹码分布
@router.post("/stock_cyq_em")
def get_stock_cyq_em(request: SymbolRequest):
    """
    描述: 东方财富网-概念板-行情中心-日K-筹码分布
    限量: 单次返回指定 symbol 和 adjust 的近 90 个交易日数据
    """
    try:
        stock_cyq_em_df = ak.stock_cyq_em(symbol=request.symbol, adjust="")
        return stock_cyq_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 一致行动人
@router.get("/stock_yzxdr_em")
def get_stock_yzxdr_em(date: str):
    """
    东方财富网-数据中心-特色数据-一致行动人
    单次返回所有历史数据
    """
    try:
        stock_yzxdr_em_df = ak.stock_yzxdr_em(date=date)
        return stock_yzxdr_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 赚钱效应分析
@router.get("/stock_market_activity_legu")
def get_stock_market_activity_legu():
    """
    接口: stock_market_activity_legu
    目标地址: https://www.legulegu.com/stockdata/market-activity
    描述: 乐咕乐股网-赚钱效应分析数据
    限量: 单次返回当前赚钱效应分析数据
    """
    try:
        stock_market_activity_legu_df = ak.stock_market_activity_legu()
        return stock_market_activity_legu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
