import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 期货交易费用参照表
@router.get("/futures_fees_info", operation_id="get_futures_fees_info")
async def get_futures_fees_info():
    """
    期货交易费用参照表

    接口: futures_fees_info

    目标地址: http://openctp.cn/fees.html

    描述: openctp 期货交易费用参照表

    限量: 单次返回所有数据
    """
    try:
        futures_fees_info = ak.futures_fees_info()
        futures_fees_info_df = sanitize_data_pandas(futures_fees_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return futures_fees_info_df.to_dict(orient="records")


class FuturesSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定交易所",
                        description="可选择 所有, 上海期货交易所, 大连商品交易所, 郑州商品交易所, 上海国际能源交易中心, 中国金融期货交易所, 广州期货交易所")


# 期货手续费与保证金
@router.post("/futures_comm_info", operation_id="post_futures_comm_info")
def post_futures_comm_info(request: FuturesSymbolRequest):
    """
    期货手续费与保证金

    接口: futures_comm_info

    目标地址: https://www.9qihuo.com/qihuoshouxufei

    描述: 九期网-期货手续费数据

    限量: 单次返回指定交易所的所有数据
    """
    try:
        futures_comm_info = ak.futures_comm_info(symbol=request.symbol)
        futures_comm_info_df = sanitize_data_pandas(futures_comm_info)

        return futures_comm_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FuturesDateRequest(BaseModel):
    date: str = Field(..., title="指定交易日",
                      description="例：20240723，需要指定为交易日,且为一年内")


# 期货手续费与保证金
@router.post("/futures_rule", operation_id="post_futures_rule")
def post_futures_rule(request: FuturesDateRequest):
    """
    期货规则-交易日历表

    接口: futures_rule

    目标地址: https://www.gtjaqh.com/pc/calendar.html

    描述: 国泰君安期货-交易日历数据表

    限量: 单次返回指定交易日所有合约的交易日历数据
    """
    try:
        futures_rule = ak.futures_rule(date=request.date)
        futures_rule_df = sanitize_data_pandas(futures_rule)

        return futures_rule_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ExchangeSymbolRequest(BaseModel):
    exchange: str = Field(..., title="指定交易所",
                          description="例：大连商品交易所，可选择：上海期货交易所, 郑州商品交易所, 大连商品交易所, LME, NYMEX, CBOT, NYBOT, TOCOM, "
                                      "上海国际能源交易中心, OSE; 具体交易所查询：http://www.99qh.com/d/store.aspx")
    symbol: str = Field(..., title="指定交易品种",
                        description="例： 豆一 ; 交易所对应的具体品种; 如：大连商品交易所的 豆一; 具体品种查询：http://www.99qh.com/d/store.aspx")


# 库存数据-99期货网
@router.post("/futures_inventory_99", operation_id="post_futures_inventory_99")
def post_futures_inventory_99(request: ExchangeSymbolRequest):
    """
    库存数据-99期货网

    接口: futures_inventory_99

    目标地址: http://www.99qh.com/d/store.aspx

    描述: 99 期货网-大宗商品库存数据; 周频率

    限量: 单次返回指定交易所和指定品种的具体品种的期货库存数据, 仓单日报数据
    """
    try:
        futures_inventory_99 = ak.futures_inventory_99(
            exchange=request.exchange,
            symbol=request.symbol
        )
        futures_inventory_99_df = sanitize_data_pandas(futures_inventory_99)

        return futures_inventory_99_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ExchangeSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定交易品种",
                        description="例： 豆一 ; http://data.eastmoney.com/ifdata/kcsj.html 对应的中文名称")


# 东方财富-库存数据
@router.post("/futures_inventory_em", operation_id="post_futures_inventory_em")
def post_futures_inventory_em(request: ExchangeSymbolRequest):
    """
    东方财富-库存数据

    接口: futures_inventory_em

    目标地址: http://data.eastmoney.com/ifdata/kcsj.html

    描述: 东方财富网-期货数据-库存数据; 近 60 个交易日的期货库存日频率数据

    限量: 返回指定交易所指定品种的期货库存数据, 仓单日报数据
    """
    try:
        futures_inventory_em = ak.futures_inventory_em(
            symbol=request.symbol
        )
        futures_inventory_em_df = sanitize_data_pandas(futures_inventory_em)

        return futures_inventory_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
