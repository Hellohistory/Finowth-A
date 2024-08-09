from typing import List

import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DongCaiBankSymbolRequest(BaseModel):
    market: str = Field(..., title="市场类型",
                        description="可请求interest_rate_interbank_market_data获取")
    symbol: str = Field(..., title="利率品种", description="可请求interest_rate_interbank_market_data获取")
    indicator: str = Field(..., title="利率指标", description="可请求interest_rate_interbank_market_data获取")


# 东方财富-拆借利率一览-具体市场的具体品种的具体指标的拆借利率数据
@router.post("/interest_rate_interbank", operation_id="interest_rate_interbank")
async def interest_rate_interbank(request: DongCaiBankSymbolRequest):
    """
    接口: rate_interbank

    目标地址: https://data.eastmoney.com/shibor/shibor.aspx?m=sg&t=88&d=99333&cu=sgd&type=009065&p=79

    描述: 东方财富-拆借利率一览-具体市场的具体品种的具体指标的拆借利率数据

    限量: 返回所有历史数据
    """
    try:
        rate_interbank_df = ak.rate_interbank(market=request.market,
                                              symbol=request.symbol,
                                              indicator=request.indicator,
                                              )
        rate_interbank_df = sanitize_data_pandas(rate_interbank_df)

        return rate_interbank_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class MarketData(BaseModel):
    market: str
    symbol: str
    indicator: str


# 数据列表
data = [
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="隔夜"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="1周"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="2周"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="1月"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="3月"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="6月"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="9月"),
    MarketData(market="上海银行同业拆借市场", symbol="Shibor人民币", indicator="1年"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="隔夜"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="1周"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="2周"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="3周"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="1月"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="2月"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="3月"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="4月"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="6月"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="9月"),
    MarketData(market="中国银行同业拆借市场", symbol="Chibor人民币", indicator="1年"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor英镑", indicator="隔夜"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor英镑", indicator="1周"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor英镑", indicator="1月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor英镑", indicator="2月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor英镑", indicator="3月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor英镑", indicator="8月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator="隔夜"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator="1周"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator="1月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator="2月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator="3月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor美元", indicator="8月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor欧元", indicator="隔夜"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor欧元", indicator="1周"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor欧元", indicator="1月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor欧元", indicator="2月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor欧元", indicator="3月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor欧元", indicator="8月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor日元", indicator="隔夜"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor日元", indicator="1周"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor日元", indicator="1月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor日元", indicator="2月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor日元", indicator="3月"),
    MarketData(market="伦敦银行同业拆借市场", symbol="Libor日元", indicator="8月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="1周"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="2周"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="3周"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="1月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="2月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="3月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="4月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="5月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="6月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="7月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="8月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="9月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="10月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="11月"),
    MarketData(market="欧洲银行同业拆借市场", symbol="Euribor欧元", indicator="1年"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="隔夜"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="1周"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="2周"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="1月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="2月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="3月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="4月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="5月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="6月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="7月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="8月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="9月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="10月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="11月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor港币", indicator="1年"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="隔夜"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="1周"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="2周"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="1月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="2月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="3月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="4月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="5月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="6月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="7月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="8月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="9月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="10月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="11月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor美元", indicator="1年"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="隔夜"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="1周"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="2周"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="1月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="2月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="3月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="6月"),
    MarketData(market="香港银行同业拆借市场", symbol="Hibor人民币", indicator="1年"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="1月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="2月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="3月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="6月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="9月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor星元", indicator="1年"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor美元", indicator="1月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor美元", indicator="2月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor美元", indicator="3月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor美元", indicator="6月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor美元", indicator="9月"),
    MarketData(market="新加坡银行同业拆借市场", symbol="Sibor美元", indicator="1年")
]


@router.get("/interest_rate_interbank_market_data",
            response_model=List[MarketData],
            operation_id="interest_rate_interbank_market_data"
            )
def market_data():
    """
    接口: interest_rate_interbank_market_data

    银行间拆借利率

    描述: 返回市场-品种-指标  银行间拆借利率数据

    限量: 单次返回所有历史数据
    """
    return data


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
