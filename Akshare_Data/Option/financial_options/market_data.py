import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class InterestSymbolRequest(BaseModel):
    symbol: str = Field(..., title="合约名称",
                        description="例：华泰柏瑞沪深300ETF期权，请求option_list_of_financial_option_contract_names获取")
    end_month: str = Field(..., title="合约到期月份",
                           description="例：2406，只能获取近期合约的数据")


# 期权-金融期权-三大交易所-行情数据
@router.post("/option_finance_board",
             operation_id="post_option_finance_board")
def post_option_finance_board(request: InterestSymbolRequest):
    """
    期权-金融期权-三大交易所-行情数据

    接口: option_finance_board

    目标地址:

    (1)http://www.sse.com.cn/assortment/options/price/

    (2)http://www.szse.cn/market/derivative/derivative_list/index.html

    (3)http://www.cffex.com.cn/hs300gzqq/

    (4)http://www.cffex.com.cn/zz1000gzqq/

    描述: 上海证券交易所、深圳证券交易所、中国金融期货交易所的金融期权行情数据

    限量: 单次返回当前交易日指定合约期权行情数据

    P.S. 可以通过调用 option_finance_sse_underlying 来获取上海证券交易所 金融期权标的物当日行情数据
    """
    try:
        option_finance_board = ak.option_finance_board(
            symbol=request.symbol,
            end_month=request.end_month,
        )
        option_finance_board_df = sanitize_data_pandas(option_finance_board)

        return option_finance_board_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionSseSpotPriceSina(BaseModel):
    symbol: str = Field(..., title="代码类型", description="例：10002273")


# 期权-金融期权-上交所-实时数据
@router.post("/option_sse_spot_price_sina",
             operation_id="post_option_sse_spot_price_sina")
def post_option_sse_spot_price_sina(request: OptionSseSpotPriceSina):
    """
    期权-金融期权-上交所-实时数据

    接口: option_sse_spot_price_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 期权实时数据

    限量: 单次返回期权实时数据
    """
    try:
        option_sse_spot_price_sina = ak.option_sse_spot_price_sina(
            symbol=request.symbol,
        )
        option_sse_spot_price_sina_df = sanitize_data_pandas(option_sse_spot_price_sina)

        return option_sse_spot_price_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-上交所-期权行情分钟数据
@router.post("/option_sse_minute_sina",
             operation_id="post_option_sse_minute_sina")
def post_option_sse_minute_sina(request: OptionSseSpotPriceSina):
    """
    期权-金融期权-上交所-期权行情分钟数据

    接口: option_sse_minute_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 期权行情分钟数据, 只能返还当天的分钟数据

    限量: 单次返回期权行情分钟数据
    """
    try:
        option_sse_minute_sina = ak.option_sse_minute_sina(
            symbol=request.symbol,
        )
        option_sse_minute_sina_df = sanitize_data_pandas(option_sse_minute_sina)

        return option_sse_minute_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-上交所-期权行情日数据
@router.post("/option_sse_daily_sina",
             operation_id="post_option_sse_daily_sina")
def post_option_sse_daily_sina(request: OptionSseSpotPriceSina):
    """
    期权-金融期权-上交所-期权行情日数据

    接口: option_sse_daily_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 期权行情日数据

    限量: 单次返回期权行情日数据
    """
    try:
        option_sse_daily_sina = ak.option_sse_daily_sina(
            symbol=request.symbol,
        )
        option_sse_daily_sina_df = sanitize_data_pandas(option_sse_daily_sina)

        return option_sse_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionFinanceMinuteSina(BaseModel):
    symbol: str = Field(..., title="期权代码",
                        description="例：10002530，可通过 option_sse_codes_sina 获取")


# 期权-金融期权-新浪-期权行情分时数据
@router.post("/option_finance_minute_sina",
             operation_id="post_option_finance_minute_sina")
def post_option_finance_minute_sina(request: OptionFinanceMinuteSina):
    """
    期权-金融期权-新浪-期权行情分时数据

    接口: option_finance_minute_sina

    目标地址: https://stock.finance.sina.com.cn/option/quotes.html

    描述: 新浪财经-金融期权-股票期权分时行情数据

    限量: 单次返回指定期权的分时行情数据
    """
    try:
        option_finance_minute_sina = ak.option_finance_minute_sina(
            symbol=request.symbol,
        )
        option_finance_minute_sina_df = sanitize_data_pandas(option_finance_minute_sina)

        return option_finance_minute_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionMinuteEM(BaseModel):
    symbol: str = Field(..., title="期权代码",
                        description="例：MO2402-C-5400，可通过 option_sse_codes_sina 获取")


# 期权-金融期权-东财-期权行情分时数据
@router.post("/option_minute_em",
             operation_id="post_option_minute_em")
def post_option_minute_em(request: OptionMinuteEM):
    """
    期权-金融期权-东财-期权行情分时数据

    接口: option_minute_em

    目标地址: https://wap.eastmoney.com/quote/stock/151.cu2404P61000.html

    描述: 东方财富网-行情中心-期权市场-分时行情

    限量: 单次返回指定期权的分时行情数据; 只能获取近期合约的数据
    """
    try:
        option_minute_em = ak.option_minute_em(
            symbol=request.symbol,
        )
        option_minute_em_df = sanitize_data_pandas(option_minute_em)

        return option_minute_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-期权市场-期权实时行情
@router.get("/option_current_em", operation_id="get_option_current_em")
def get_option_current_em():
    """
    东方财富-期权市场-期权实时行情

    接口: option_current_em

    目标地址: https://quote.eastmoney.com/center/qqsc.html

    描述: 东方财富网-行情中心-期权市场

    限量: 单次返回全部合约的实时行情
    """
    try:
        option_current_em = ak.option_current_em()
        data = option_current_em.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionSseSpotUnderlyingPriceSina(BaseModel):
    symbol: str = Field(..., title="期权代码", description="可选择510050, 510300, 159919")
    indicator: str = Field(..., title="交易类型",
                           description="可选择：期权交易情况-认沽交易量, 期权持仓情况-认沽持仓量, "
                                       "期权交易情况-认购交易量, 期权持仓情况-认购持仓量")
    trade_date: str = Field(..., title="交易日期", description="例：20200204")


# 期权-金融期权-上交所-期权标的物的实时数据
@router.post("/option_lhb_em", operation_id="post_option_lhb_em")
def post_option_lhb_em(request: OptionSseSpotUnderlyingPriceSina):
    """
    期权-金融期权-上交所-期权标的物的实时数据

    接口: option_lhb_em

    目标地址: https://data.eastmoney.com/other/qqlhb.html

    描述: 东方财富网-数据中心-特色数据-期权龙虎榜单-金融期权

    限量: 单次返回指定 symbol, indicator 和 trade_date 的所有数据
    """
    try:
        option_lhb_em = ak.option_lhb_em(
            symbol=request.symbol,
            indicator=request.indicator,
            trade_date=request.trade_date
        )
        option_lhb_em_df = sanitize_data_pandas(option_lhb_em)

        return option_lhb_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
