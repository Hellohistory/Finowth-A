import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class CurrencyBocSina(BaseModel):
    symbol: str = Field(..., title="需查询的对应币种",
                        description="可选择 美元, 英镑, 欧元, 澳门元, 泰国铢, 菲律宾比索, 港币, "
                                    "瑞士法郎, 新加坡元, 瑞典克朗, 丹麦克朗, 挪威克朗, 日元, 加拿大元, "
                                    "澳大利亚元, 新西兰元, 韩国元")
    start_date: str = Field(..., title="开始日期",
                            description="例：20230304，开始日期和结束日期之间的间隔要超过 6 个月")
    end_date: str = Field(..., title="结束日期",
                          description="例：20231110，开始日期和结束日期之间的间隔要超过 6 个月 ")


# 外汇数据-人民币牌价数据
@router.post("/currency_boc_sina", operation_id="post_currency_boc_sina")
def post_currency_boc_sina(request: CurrencyBocSina):
    """
    外汇数据-人民币牌价数据

    接口: currency_boc_sina

    目标地址: https://biz.finance.sina.com.cn/forex/forex.php?startdate=2012-01-01&enddate=2021-06-14&money_code=EUR&type=0

    描述: 新浪财经-中行人民币牌价历史数据

    限量: 单次返回指定日期的所有历史数据
    """
    try:
        currency_boc_sina = ak.currency_boc_sina(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date
        )
        futures_comm_info_df = sanitize_data_pandas(currency_boc_sina)

        return futures_comm_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 外汇数据-人民币汇率中间价
@router.get("/currency_boc_safe", operation_id="get_currency_boc_safe")
async def get_currency_boc_safe():
    """
    外汇数据-人民币汇率中间价

    接口: currency_boc_safe

    目标地址: https://www.safe.gov.cn/safe/rmbhlzjj/index.html

    描述: 外汇管理局-人民币汇率中间价

    限量: 单次返回所有历史数据

    P.S. 人民币对马来西亚林吉特、俄罗斯卢布、南非兰特、韩元、阿联酋迪拉姆、沙特里亚尔、匈牙利福林、波兰兹罗提、
    丹麦克朗、瑞典克朗、挪威克朗、土耳其里拉、墨西哥比索、泰铢汇率中间价采取间接标价法，即100人民币折合多少外币。
    人民币对其它10种货币汇率中间价仍采取直接标价法，即100外币折合多少人民币。
    """
    try:
        currency_boc_safe = ak.currency_boc_safe()
        currency_boc_safe_df = sanitize_data_pandas(currency_boc_safe)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return currency_boc_safe_df.to_dict(orient="records")


# 外汇数据-人民币外汇即期报价
@router.get("/fx_spot_quote", operation_id="get_fx_spot_quote")
async def get_fx_spot_quote():
    """
    外汇数据-人民币外汇即期报价

    接口: fx_spot_quote

    目标地址: http://www.chinamoney.com.cn/chinese/mkdatapfx/

    描述: 人民币外汇即期报价

    限量: 单次返回实时行情数据

    注：本行情为询价报价行情(美元为ODM), 实时更新
    """
    try:
        fx_spot_quote = ak.fx_spot_quote()
        fx_spot_quote_df = sanitize_data_pandas(fx_spot_quote)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fx_spot_quote_df.to_dict(orient="records")


# 外汇数据-人民币外汇远掉报价
@router.get("/fx_swap_quote", operation_id="get_fx_swap_quote")
async def get_fx_swap_quote():
    """
    外汇数据-人民币外汇远掉报价

    接口: fx_swap_quote

    目标地址: http://www.chinamoney.com.cn/chinese/mkdatapfx/

    描述: 人民币外汇远掉报价

    限量: 单次返回实时行情数据
    """
    try:
        fx_swap_quote = ak.fx_swap_quote()
        fx_swap_quote_df = sanitize_data_pandas(fx_swap_quote)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fx_swap_quote_df.to_dict(orient="records")


class CurrencyPairMap(BaseModel):
    symbol: str = Field(..., title="中文的币种名称",
                        description="可通过 https://cn.investing.com/currencies/cny-jmd 查询")


# 外汇数据-指定币种的所有货币对
@router.post("/currency_pair_map", operation_id="post_currency_pair_map")
def post_currency_pair_map(request: CurrencyPairMap):
    """
    外汇数据-指定币种的所有货币对

    接口: currency_pair_map

    目标地址: https://cn.investing.com/currencies/cny-jmd

    描述: 指定币种的所有能够获取到的货币对信息，历史数据可以调用 currency_history 获取

    限量: 单次返回指定币种的所有能获取数据的货币对
    """
    try:
        currency_pair_map = ak.currency_pair_map(
            symbol=request.symbol
        )
        currency_pair_map_df = sanitize_data_pandas(currency_pair_map)

        return currency_pair_map_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class MacroFXSentiment(BaseModel):
    start_date: str = Field(..., title="开始时间",
                            description="所指定的日期必须在当前交易日之前的30个交易日内")
    end_date: str = Field(..., title="结束时间",
                          description="所指定的日期必须在当前交易日之前的30个交易日内")


# 外汇数据-指定币种的所有货币对
@router.post("/macro_fx_sentiment", operation_id="post_macro_fx_sentiment")
def post_macro_fx_sentiment(request: MacroFXSentiment):
    """
    外汇数据-指定币种的所有货币对

    接口: macro_fx_sentiment

    目标地址: https://datacenter.jin10.com/reportType/dc_ssi_trends

    描述: 货币对-投机情绪报告

    限量: 单次返回指定日期所有品种的数据(所指定的日期必须在当前交易日之前的30个交易日内)
    """
    try:
        macro_fx_sentiment = ak.macro_fx_sentiment(
            start_date=request.start_date,
            end_date=request.end_date
        )
        macro_fx_sentiment_df = sanitize_data_pandas(macro_fx_sentiment)

        return macro_fx_sentiment_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FXQuoteBaidu(BaseModel):
    symbol: str = Field(..., title="中文的币种名称",
                        description="可选择人民币, 美元")


# 外汇数据-指定币种的所有货币对
@router.post("/fx_quote_baidu", operation_id="post_fx_quote_baidu")
def post_fx_quote_baidu(request: FXQuoteBaidu):
    """
    外汇数据-指定币种的所有货币对

    接口: fx_quote_baidu

    目标地址: https://gushitong.baidu.com/top/foreign-common-%E5%B8%B8%E7%94%A8

    描述: 百度股市通-外汇-行情榜单

    限量: 单次返回指定品种当前时点的行情报价
    """
    try:
        fx_quote_baidu = ak.fx_quote_baidu(symbol=request.symbol)
        fx_quote_baidu_df = sanitize_data_pandas(fx_quote_baidu)

        return fx_quote_baidu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
