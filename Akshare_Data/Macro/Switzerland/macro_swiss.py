import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 瑞士宏观-SVME 采购经理人指数
@router.get("/macro_swiss_svme",
            operation_id="macro_swiss_svme")
async def macro_swiss_svme():
    """
    瑞士宏观-SVME 采购经理人指数

    接口: macro_swiss_svme

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_0.html

    描述: 东方财富-经济数据-瑞士-SVME采购经理人指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_swiss_svme = ak.macro_swiss_svme()
        macro_swiss_svme_df = sanitize_data_pandas(macro_swiss_svme)
        return macro_swiss_svme_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 瑞士宏观-贸易帐
@router.get("/macro_swiss_trade",
            operation_id="macro_swiss_trade")
async def macro_swiss_trade():
    """
    瑞士宏观-贸易帐

    接口: macro_swiss_trade

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_1.html

    描述: 东方财富-经济数据-瑞士-贸易帐

    限量: 单次返回所有历史数据
    """
    try:
        macro_swiss_trade = ak.macro_swiss_trade()
        macro_swiss_trade_df = sanitize_data_pandas(macro_swiss_trade)
        return macro_swiss_trade_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 瑞士宏观-GDP 季率
@router.get("/macro_swiss_gdp_quarterly",
            operation_id="macro_swiss_gdp_quarterly")
async def macro_swiss_gdp_quarterly():
    """
    瑞士宏观-GDP 季率

    接口: macro_swiss_gdp_quarterly

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_3.html

    描述: 东方财富-经济数据-瑞士-GDP 季率

    限量: 单次返回所有历史数据
    """
    try:
        macro_swiss_gdp_quarterly = ak.macro_swiss_gdp_quarterly()
        macro_swiss_gdp_quarterly_df = sanitize_data_pandas(macro_swiss_gdp_quarterly)
        return macro_swiss_gdp_quarterly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 瑞士宏观-GDP 年率
@router.get("/macro_swiss_gbd_yearly",
            operation_id="macro_swiss_gbd_yearly")
async def macro_swiss_gbd_yearly():
    """
    瑞士宏观-GDP 季率

    接口: macro_swiss_gbd_yearly

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_4.html

    描述: 东方财富-经济数据-瑞士-GDP 年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_swiss_gbd_yearly = ak.macro_swiss_gbd_yearly()
        macro_swiss_gbd_yearly_df = sanitize_data_pandas(macro_swiss_gbd_yearly)
        return macro_swiss_gbd_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 瑞士宏观-央行公布利率决议
@router.get("/macro_swiss_gbd_bank_rate",
            operation_id="macro_swiss_gbd_bank_rate")
async def macro_swiss_gbd_bank_rate():
    """
    瑞士宏观-央行公布利率决议

    接口: macro_swiss_gbd_bank_rate

    目标地址: http://data.eastmoney.com/cjsj/foreign_2_5.html

    描述: 东方财富-经济数据-瑞士-央行公布利率决议

    限量: 单次返回所有历史数据
    """
    try:
        macro_swiss_gbd_bank_rate = ak.macro_swiss_gbd_bank_rate()
        macro_swiss_gbd_bank_rate_df = sanitize_data_pandas(macro_swiss_gbd_bank_rate)
        return macro_swiss_gbd_bank_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
