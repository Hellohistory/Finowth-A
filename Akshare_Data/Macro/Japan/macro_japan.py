import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 日本宏观-央行公布利率决议
@router.get("/macro_japan_bank_rate",
            operation_id="macro_japan_bank_rate")
async def macro_japan_bank_rate():
    """
    日本宏观-央行公布利率决议

    接口: macro_japan_bank_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_3_0.html

    描述: 东方财富-经济数据-日本-央行公布利率决议

    限量: 单次返回所有历史数据
    """
    try:
        macro_japan_bank_rate = ak.macro_japan_bank_rate()
        macro_japan_bank_rate_df = sanitize_data_pandas(macro_japan_bank_rate)
        return macro_japan_bank_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 日本宏观-全国消费者物价指数年率
@router.get("/macro_japan_cpi_yearly",
            operation_id="macro_japan_cpi_yearly")
async def macro_japan_cpi_yearly():
    """
    日本宏观-全国消费者物价指数年率

    接口: macro_japan_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_3_1.html

    描述: 东方财富-经济数据-日本-全国消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_japan_cpi_yearly = ak.macro_japan_cpi_yearly()
        macro_japan_cpi_yearly_df = sanitize_data_pandas(macro_japan_cpi_yearly)
        return macro_japan_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 日本宏观-全国核心消费者物价指数年率
@router.get("/macro_japan_core_cpi_yearly",
            operation_id="macro_japan_core_cpi_yearly")
async def macro_japan_core_cpi_yearly():
    """
    日本宏观-全国核心消费者物价指数年率

    接口: macro_japan_core_cpi_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_2.html

    描述: 东方财富-经济数据-日本-全国核心消费者物价指数年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_japan_core_cpi_yearly = ak.macro_japan_core_cpi_yearly()
        macro_japan_core_cpi_yearly_df = sanitize_data_pandas(macro_japan_core_cpi_yearly)
        return macro_japan_core_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 日本宏观-失业率
@router.get("/macro_japan_unemployment_rate",
            operation_id="macro_japan_unemployment_rate")
async def macro_japan_unemployment_rate():
    """
    日本宏观-失业率

    接口: macro_japan_unemployment_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_3.html

    描述: 东方财富-经济数据-日本-失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_japan_unemployment_rate = ak.macro_japan_unemployment_rate()
        macro_japan_unemployment_rate_df = sanitize_data_pandas(macro_japan_unemployment_rate)
        return macro_japan_unemployment_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 日本宏观-领先指标终值
@router.get("/macro_japan_head_indicator",
            operation_id="macro_japan_head_indicator")
async def macro_japan_head_indicator():
    """
    日本宏观-领先指标终值

    接口: macro_japan_head_indicator

    目标地址: http://data.eastmoney.com/cjsj/foreign_3_4.html

    描述: 东方财富-经济数据-日本-领先指标终值

    限量: 单次返回所有历史数据
    """
    try:
        macro_japan_head_indicator = ak.macro_japan_head_indicator()
        macro_japan_head_indicator_df = sanitize_data_pandas(macro_japan_head_indicator)
        return macro_japan_head_indicator_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
