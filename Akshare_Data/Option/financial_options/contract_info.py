import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class OptionSseListSina(BaseModel):
    symbol: str = Field(..., title="选择品种", description="可选择 50ETF 或 300ETF")
    exchange: str = Field(..., title="选择类型", description="例：null")


# 期权-金融期权-上交所-合约到期月份列表
@router.post("/option_sse_list_sina",
             operation_id="post_option_sse_list_sina")
def post_option_sse_list_sina(request: OptionSseListSina):
    """
    期权-金融期权-上交所-合约到期月份列表

    接口: option_sse_list_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 获取期权-上交所-50ETF-合约到期月份列表

    限量: 单次返回指定品种的到期月份列表
    """
    try:
        option_sse_list_sina = ak.option_sse_list_sina(
            symbol=request.symbol,
            exchange=request.exchange
        )
        option_sse_list_sina_df = sanitize_data_pandas(option_sse_list_sina)

        return option_sse_list_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionSseExpireDaySina(BaseModel):
    trade_date: str = Field(..., title="选择年月", description="例：202406")
    symbol: str = Field(..., title="选择期权类型", description="可选择 看涨期权, 看跌期权")
    underlying: str = Field(..., title="选择类型", description="例：510300")


# 期权-金融期权-上交所-所有合约的代码
@router.post("/option_sse_codes_sina",
             operation_id="post_option_sse_codes_sina")
def post_option_sse_codes_sina(request: OptionSseExpireDaySina):
    """
    期权-金融期权-上交所-所有合约的代码

    接口: option_sse_codes_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 新浪期权-看涨看跌合约合约的代码

    限量: 单次返回指定期权类型合约的代码
    """
    try:
        option_sse_codes_sina = ak.option_sse_codes_sina(
            underlying=request.underlying,
            symbol=request.symbol,
            trade_date=request.trade_date
        )
        option_sse_codes_sina_df = sanitize_data_pandas(option_sse_codes_sina)

        return option_sse_codes_sina_df.to_dict(orient="records")
    except ValueError as ve:
        error_message = str(ve)
        # 分析错误信息以确定问题来源
        if "Length mismatch" in error_message:
            error_detail = (
                "这个问题可能是由于 'trade_date' 字段格式不正确导致的。"
                "请确保 'trade_date' 采用 'YYYYMM' 格式，仅包含年和月。"
                "且时间范围需自行控制"
            )
        else:
            error_detail = error_message

        raise HTTPException(status_code=400, detail=f"ValueError: {error_detail}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")


class OptionSseSpotPriceSina(BaseModel):
    symbol: str = Field(..., title="代码类型", description="例：10002273")


# 期权-金融期权-上交所-期权希腊字母信息表
@router.post("/option_sse_greeks_sina",
             operation_id="post_option_sse_greeks_sina")
def post_option_sse_greeks_sina(request: OptionSseSpotPriceSina):
    """
    期权-金融期权-上交所-期权希腊字母信息表

    接口: option_sse_greeks_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 新浪财经-期权希腊字母信息表

    限量: 单次返回当前交易日的期权希腊字母信息表
    """
    try:
        option_sse_greeks_sina = ak.option_sse_greeks_sina(
            symbol=request.symbol,
        )
        option_sse_greeks_sina_df = sanitize_data_pandas(option_sse_greeks_sina)

        return option_sse_greeks_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionSseSpotUnderlyingPriceSina(BaseModel):
    symbol: str = Field(..., title="带有市场类型的期权代码", description="例：sh510300")


# 期权-金融期权-上交所-期权标的物的实时数据
@router.post("/option_sse_underlying_spot_price_sina",
             operation_id="post_option_sse_underlying_spot_price_sina")
def post_option_sse_underlying_spot_price_sina(request: OptionSseSpotUnderlyingPriceSina):
    """
    期权-金融期权-上交所-期权标的物的实时数据

    接口: option_sse_underlying_spot_price_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 获取期权标的物的实时数据

    限量: 单次返回期权标的物的实时数据
    """
    try:
        option_sse_underlying_spot_price_sina = ak.option_sse_underlying_spot_price_sina(
            symbol=request.symbol,
        )
        option_sse_underlying_spot_price_sina_df = sanitize_data_pandas(option_sse_underlying_spot_price_sina)

        return option_sse_underlying_spot_price_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-期权市场-期权价值分析
@router.get("/option_value_analysis_em", operation_id="get_option_value_analysis_em")
def get_option_value_analysis_em():
    """
    东方财富-期权市场-期权价值分析

    接口: option_value_analysis_em

    目标地址: https://data.eastmoney.com/other/valueAnal.html

    描述: 东方财富网-数据中心-特色数据-期权价值分析

    限量: 单次返回所有数据
    """
    try:
        option_value_analysis_em = ak.option_value_analysis_em()
        data = option_value_analysis_em.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-期权市场-期权风险分析
@router.get("/option_risk_analysis_em", operation_id="get_option_risk_analysis_em")
def get_option_risk_analysis_em():
    """
    东方财富-期权市场-期权风险分析

    接口: option_risk_analysis_em

    目标地址: https://data.eastmoney.com/other/riskanal.html

    描述: 东方财富网-数据中心-特色数据-期权风险分析

    限量: 单次返回所有数据
    """
    try:
        option_risk_analysis_em = ak.option_risk_analysis_em()
        data = option_risk_analysis_em.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-期权市场-期权折溢价
@router.get("/option_premium_analysis_em", operation_id="get_option_premium_analysis_em")
def get_option_premium_analysis_em():
    """
    东方财富-期权市场-期权折溢价

    接口: option_premium_analysis_em

    目标地址: https://data.eastmoney.com/other/premium.html

    描述: 东方财富网-数据中心-特色数据-期权折溢价

    限量: 单次返回所有数据
    """
    try:
        option_premium_analysis_em = ak.option_premium_analysis_em()
        data = option_premium_analysis_em.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
