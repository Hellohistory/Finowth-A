import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-宏观经济-中国宏观杠杆率
@router.get("/macro_cnbs", operation_id="macro_cnbs")
async def macro_cnbs():
    """
    国民经济运行状况-宏观经济-中国宏观杠杆率

    接口: macro_cnbs

    目标地址: http://114.115.232.154:8080/

    描述: 中国国家金融与发展实验室-中国宏观杠杆率数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_cnbs = ak.macro_cnbs()
        macro_cnbs_df = sanitize_data_pandas(macro_cnbs)
        return macro_cnbs_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-海关进出口增减情况
@router.get("/macro_china_hgjck", operation_id="macro_china_hgjck")
async def macro_china_hgjck():
    """
    国民经济运行状况-宏观经济-海关进出口增减情况

    接口: macro_china_hgjck

    目标地址: https://data.eastmoney.com/cjsj/hgjck.html

    描述: 中国海关进出口增减情况一览表, 数据区间从 200801 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hgjck = ak.macro_china_hgjck()
        macro_china_hgjck_df = sanitize_data_pandas(macro_china_hgjck)
        return macro_china_hgjck_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-财政收入
@router.get("/macro_china_czsr", operation_id="macro_china_czsr")
async def macro_china_czsr():
    """
    国民经济运行状况-宏观经济-财政收入

    接口: macro_china_czsr

    目标地址: http://data.eastmoney.com/cjsj/czsr.html

    描述: 中国财政收入, 数据区间从 200801 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_czsr = ak.macro_china_czsr()
        macro_china_czsr_df = sanitize_data_pandas(macro_china_czsr)
        return macro_china_czsr_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-外汇贷款数据
@router.get("/macro_china_whxd", operation_id="macro_china_whxd")
async def macro_china_whxd():
    """
    国民经济运行状况-宏观经济-外汇贷款数据

    接口: macro_china_whxd

    目标地址: http://data.eastmoney.com/cjsj/whxd.html

    描述: 外汇贷款数据, 数据区间从 200802 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_whxd = ak.macro_china_whxd()
        macro_china_whxd_df = sanitize_data_pandas(macro_china_whxd)
        return macro_china_whxd_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-新债发行
@router.get("/macro_china_bond_public", operation_id="macro_china_bond_public")
async def macro_china_bond_public():
    """
    国民经济运行状况-宏观经济-新债发行

    接口: macro_china_bond_public

    目标地址: https://www.chinamoney.com.cn/chinese/xzjfx/

    描述: 中国外汇交易中心暨全国银行间同业拆借中心-债券信息披露-新债发行; 近期债券发行数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_bond_public = ak.macro_china_bond_public()
        macro_china_bond_public_df = sanitize_data_pandas(macro_china_bond_public)
        return macro_china_bond_public_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-社会消费品零售总额
@router.get("/macro_china_consumer_goods_retail",
            operation_id="macro_china_consumer_goods_retail")
async def macro_china_consumer_goods_retail():
    """
    国民经济运行状况-宏观经济-社会消费品零售总额

    接口: macro_china_consumer_goods_retail

    目标地址: http://data.eastmoney.com/cjsj/xfp.html

    描述: 东方财富-经济数据-社会消费品零售总额

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_consumer_goods_retail = ak.macro_china_consumer_goods_retail()
        macro_china_consumer_goods_retail_df = sanitize_data_pandas(macro_china_consumer_goods_retail)
        return macro_china_consumer_goods_retail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-全社会用电分类情况表
@router.get("/macro_china_society_electricity",
            operation_id="macro_china_society_electricity")
async def macro_china_society_electricity():
    """
    国民经济运行状况-宏观经济-全社会用电分类情况表

    接口: macro_china_society_electricity

    目标地址: http://finance.sina.com.cn/mac/#industry-6-0-31-1

    描述: 国家统计局-全社会用电分类情况表

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_society_electricity = ak.macro_china_society_electricity()
        macro_china_society_electricity_df = sanitize_data_pandas(macro_china_society_electricity)
        return macro_china_society_electricity_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-全社会用电分类情况表
@router.get("/macro_china_society_traffic_volume",
            operation_id="macro_china_society_traffic_volume")
async def macro_china_society_traffic_volume():
    """
    国民经济运行状况-宏观经济-全社会用电分类情况表

    接口: macro_china_society_traffic_volume

    目标地址: http://finance.sina.com.cn/mac/#industry-10-0-31-1

    描述: 国家统计局-全社会客货运输量-非累计

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_society_traffic_volume = ak.macro_china_society_traffic_volume()
        macro_china_society_traffic_volume_df = sanitize_data_pandas(macro_china_society_traffic_volume)
        return macro_china_society_traffic_volume_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-邮电业务基本情况
@router.get("/macro_china_postal_telecommunicational",
            operation_id="macro_china_postal_telecommunicational")
async def macro_china_postal_telecommunicational():
    """
    国民经济运行状况-宏观经济-邮电业务基本情况

    接口: macro_china_postal_telecommunicational

    目标地址: http://finance.sina.com.cn/mac/#industry-11-0-31-1

    描述: 国家统计局-邮电业务基本情况-非累计

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_postal_telecommunicational = ak.macro_china_postal_telecommunicational()
        macro_china_postal_telecommunicational_df = sanitize_data_pandas(macro_china_postal_telecommunicational)
        return macro_china_postal_telecommunicational_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-央行货币当局资产负债
@router.get("/macro_china_central_bank_balance",
            operation_id="macro_china_central_bank_balance")
async def macro_china_central_bank_balance():
    """
    国民经济运行状况-宏观经济-央行货币当局资产负债

    接口: macro_china_central_bank_balance

    目标地址: http://finance.sina.com.cn/mac/#fininfo-8-0-31-2

    描述: 新浪财经-中国宏观经济数据-央行货币当局资产负债

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_central_bank_balance = ak.macro_china_central_bank_balance()
        macro_china_central_bank_balance_df = sanitize_data_pandas(macro_china_central_bank_balance)
        return macro_china_central_bank_balance_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-货币供应量
@router.get("/macro_china_supply_of_money",
            operation_id="macro_china_supply_of_money")
async def macro_china_supply_of_money():
    """
    国民经济运行状况-宏观经济-货币供应量

    接口: macro_china_supply_of_money

    目标地址: http://finance.sina.com.cn/mac/#fininfo-1-0-31-1

    描述: 新浪财经-中国宏观经济数据-货币供应量

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_supply_of_money = ak.macro_china_supply_of_money()
        macro_china_supply_of_money_df = sanitize_data_pandas(macro_china_supply_of_money)
        return macro_china_supply_of_money_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-央行黄金和外汇储备
@router.get("/macro_china_foreign_exchange_gold",
            operation_id="macro_china_foreign_exchange_gold")
async def macro_china_foreign_exchange_gold():
    """
    国民经济运行状况-宏观经济-央行黄金和外汇储备

    接口: macro_china_foreign_exchange_gold

    目标地址: http://finance.sina.com.cn/mac/#fininfo-5-0-31-2

    描述: 国家统计局-央行黄金和外汇储备, 比东财接口数据时间长

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_foreign_exchange_gold = ak.macro_china_foreign_exchange_gold()
        macro_china_foreign_exchange_gold_df = sanitize_data_pandas(macro_china_foreign_exchange_gold)
        return macro_china_foreign_exchange_gold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-宏观经济-外汇和黄金储备
@router.get("/macro_china_fx_gold",
            operation_id="macro_china_fx_gold")
async def macro_china_fx_gold():
    """
    国民经济运行状况-宏观经济-外汇和黄金储备

    接口: macro_china_fx_gold

    目标地址: http://data.eastmoney.com/cjsj/hjwh.html

    描述: 中国外汇和黄金储备, 数据区间从 200801 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_fx_gold = ak.macro_china_fx_gold()
        macro_china_fx_gold_df = sanitize_data_pandas(macro_china_fx_gold)
        return macro_china_fx_gold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 中国央行决议报告
@router.get("/macro_bank_china_interest_rate",
            operation_id="macro_bank_china_interest_rate")
async def macro_bank_china_interest_rate():
    """
    中国央行决议报告

    接口: macro_bank_china_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_china_interest_rate_decision

    描述: 中国央行决议报告, 数据区间从 19910105-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_bank_china_interest_rate = ak.macro_bank_china_interest_rate()
        macro_bank_china_interest_rate_df = sanitize_data_pandas(macro_bank_china_interest_rate)
        return macro_bank_china_interest_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
