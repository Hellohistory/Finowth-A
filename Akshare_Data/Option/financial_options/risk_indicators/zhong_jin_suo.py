import akshare as ak
import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 期权-金融期权-新浪财经-中金所-上证50指数列表
@router.get("/option_cffex_sz50_list_sina",
            operation_id="option_cffex_sz50_list_sina")
async def option_cffex_sz50_list_sina():
    """
    期权-金融期权-新浪财经-中金所-上证50指数列表

    接口: option_cffex_sz50_list_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php/ho/cffex

    描述: 中金所-上证50指数-所有合约, 返回的第一个合约为主力合约

    限量: 单次返回所有合约
    """
    try:
        # 获取数据
        option_cffex_sz50_list_sina = ak.option_cffex_sz50_list_sina()

        # 检查返回值是否为 DataFrame 类型，如果不是，则进行转换
        if isinstance(option_cffex_sz50_list_sina, dict):
            # 将字典转换为 DataFrame
            option_cffex_sz50_list_sina_df = pd.DataFrame([option_cffex_sz50_list_sina])
        else:
            option_cffex_sz50_list_sina_df = option_cffex_sz50_list_sina

        # 清理数据并返回
        option_cffex_sz50_list_sina_df = sanitize_data_pandas(option_cffex_sz50_list_sina_df)
        return option_cffex_sz50_list_sina_df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-新浪财经-中金所-沪深300指数列表
@router.get("/option_cffex_hs300_list_sina",
            operation_id="option_cffex_hs300_list_sina")
async def option_cffex_hs300_list_sina():
    """
    期权-金融期权-新浪财经-中金所-沪深300指数列表

    接口: option_cffex_hs300_list_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 中金所-沪深300指数-所有合约, 返回的第一个合约为主力合约

    限量: 单次返回所有合约
    """
    try:
        option_cffex_hs300_list_sina = ak.option_cffex_hs300_list_sina()
        option_cffex_hs300_list_sina_df = sanitize_data_pandas(option_cffex_hs300_list_sina)
        return option_cffex_hs300_list_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-新浪财经-中金所-中证1000指数列表
@router.get("/option_cffex_zz1000_list_sina",
            operation_id="option_cffex_zz1000_list_sina")
async def option_cffex_zz1000_list_sina():
    """
    期权-金融期权-新浪财经-中金所-中证1000指数列表

    接口: option_cffex_zz1000_list_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 中金所-中证1000指数-所有合约, 返回的第一个合约为主力合约

    限量: 单次返回所有合约
    """
    try:
        option_cffex_zz1000_list_sina = ak.option_cffex_zz1000_list_sina()
        option_cffex_zz1000_list_sina_df = sanitize_data_pandas(option_cffex_zz1000_list_sina)
        return option_cffex_zz1000_list_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionCffexSZ50SpotSina(BaseModel):
    symbol: str = Field(..., title="指定合约", description="例：ho2303")


# 期权-金融期权-新浪财经-中金所-实时行情-上证50指数
@router.post("/option_cffex_sz50_spot_sina",
             operation_id="option_cffex_sz50_spot_sina")
def option_cffex_sz50_spot_sina(request: OptionCffexSZ50SpotSina):
    """
    期权-金融期权-新浪财经-中金所-实时行情-上证50指数

    接口: option_cffex_sz50_spot_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php/ho/cffex

    描述: 新浪财经-中金所-上证50指数-指定合约-实时行情

    限量: 单次返回指定合约的实时行情
    """
    try:
        option_cffex_sz50_spot_sina = ak.option_cffex_sz50_spot_sina(
            symbol=request.symbol,
        )
        option_cffex_sz50_spot_sina_df = sanitize_data_pandas(option_cffex_sz50_spot_sina)

        return option_cffex_sz50_spot_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-新浪财经-中金所-实时行情-沪深300指数
@router.post("/option_cffex_hs300_spot_sina",
             operation_id="option_cffex_hs300_spot_sina")
def option_cffex_hs300_spot_sina(request: OptionCffexSZ50SpotSina):
    """
    期权-金融期权-新浪财经-中金所-实时行情-沪深300指数

    接口: option_cffex_hs300_spot_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 新浪财经-中金所-沪深300指数-指定合约-实时行情

    限量: 单次返回指定合约的实时行情
    """
    try:
        option_cffex_hs300_spot_sina = ak.option_cffex_hs300_spot_sina(
            symbol=request.symbol,
        )
        option_cffex_hs300_spot_sina_df = sanitize_data_pandas(option_cffex_hs300_spot_sina)

        return option_cffex_hs300_spot_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-新浪财经-中金所-实时行情-中证1000指数
@router.post("/option_cffex_zz1000_spot_sina",
             operation_id="option_cffex_zz1000_spot_sina")
def option_cffex_zz1000_spot_sina(request: OptionCffexSZ50SpotSina):
    """
    期权-金融期权-新浪财经-中金所-实时行情-中证1000指数

    接口: option_cffex_zz1000_spot_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 新浪财经-中金所-中证1000指数-指定合约-实时行情

    限量: 单次返回指定合约的实时行情
    """
    try:
        option_cffex_zz1000_spot_sina = ak.option_cffex_zz1000_spot_sina(
            symbol=request.symbol,
        )
        option_cffex_zz1000_spot_sina_df = sanitize_data_pandas(option_cffex_zz1000_spot_sina)

        return option_cffex_zz1000_spot_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionCffexSZ50DailySina(BaseModel):
    symbol: str = Field(..., title="具体合约代码(包括看涨和看跌标识)",
                        description="例：ho2303P2350，可通过option_cffex_sz50_spot_sina 中的 call-标识 获取")


# 期权-金融期权-新浪财经-中金所-日频行情-上证50指数
@router.post("/option_cffex_sz50_daily_sina",
             operation_id="option_cffex_sz50_daily_sina")
def option_cffex_sz50_daily_sina(request: OptionCffexSZ50DailySina):
    """
    期权-金融期权-新浪财经-中金所-日频行情-上证50指数

    接口: option_cffex_sz50_daily_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php/ho/cffex

    描述: 中金所-上证50指数-指定合约-日频行情

    限量: 单次返回指定合约的日频行情
    """
    try:
        option_cffex_sz50_daily_sina = ak.option_cffex_sz50_daily_sina(
            symbol=request.symbol,
        )
        option_cffex_sz50_daily_sina_df = sanitize_data_pandas(option_cffex_sz50_daily_sina)

        return option_cffex_sz50_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-新浪财经-中金所-日频行情-沪深300指数
@router.post("/option_cffex_hs300_daily_sina",
             operation_id="option_cffex_hs300_daily_sina")
def option_cffex_hs300_daily_sina(request: OptionCffexSZ50DailySina):
    """
    期权-金融期权-新浪财经-中金所-日频行情-沪深300指数

    接口: option_cffex_hs300_daily_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 中金所-沪深300指数-指定合约-日频行情

    限量: 单次返回指定合约的日频行情
    """
    try:
        option_cffex_hs300_daily_sina = ak.option_cffex_hs300_daily_sina(
            symbol=request.symbol,
        )
        option_cffex_hs300_daily_sina_df = sanitize_data_pandas(option_cffex_hs300_daily_sina)

        return option_cffex_hs300_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-金融期权-新浪财经-中金所-日频行情-中证1000指数
@router.post("/option_cffex_zz1000_daily_sina",
             operation_id="option_cffex_zz1000_daily_sina")
def option_cffex_zz1000_daily_sina(request: OptionCffexSZ50DailySina):
    """
    期权-金融期权-新浪财经-中金所-日频行情-中证1000指数

    接口: option_cffex_zz1000_daily_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsCffexDP.php

    描述: 中金所-中证1000指数-指定合约-日频行情

    限量: 单次返回指定合约的日频行情
    """
    try:
        option_cffex_zz1000_daily_sina = ak.option_cffex_zz1000_daily_sina(
            symbol=request.symbol,
        )
        option_cffex_zz1000_daily_sina_df = sanitize_data_pandas(option_cffex_zz1000_daily_sina)

        return option_cffex_zz1000_daily_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
