import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 重要机构-全球最大黄金 ETF—SPDR Gold Trust 持仓报告
@router.get("/macro_cons_gold",
            operation_id="get_macro_cons_gold")
async def get_macro_cons_gold():
    """
    重要机构-全球最大黄金 ETF—SPDR Gold Trust 持仓报告

    接口: macro_cons_gold

    目标地址: https://datacenter.jin10.com/reportType/dc_etf_gold

    描述: 全球最大黄金 ETF—SPDR Gold Trust 持仓报告, 数据区间从 20041119-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_cons_gold = ak.macro_cons_gold()
        macro_cons_gold_df = sanitize_data_pandas(macro_cons_gold)
        return macro_cons_gold_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-全球最大白银ETF–iShares Silver Trust持仓报告
@router.get("/macro_cons_silver",
            operation_id="get_macro_cons_silver")
async def get_macro_cons_silver():
    """
    重要机构-全球最大白银ETF–iShares Silver Trust持仓报告

    接口: macro_cons_silver

    目标地址: https://datacenter.jin10.com/reportType/dc_etf_sliver

    描述: 全球最大白银 ETF–iShares Silver Trust 持仓报告, 数据区间从 20041202-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_cons_silver = ak.macro_cons_silver()
        macro_cons_silver_df = sanitize_data_pandas(macro_cons_silver)
        return macro_cons_silver_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-欧佩克报告
@router.get("/macro_cons_opec_month",
            operation_id="get_macro_cons_opec_month")
async def get_macro_cons_opec_month():
    """
    重要机构-欧佩克报告

    接口: macro_cons_opec_month

    目标地址: https://datacenter.jin10.com/reportType/dc_opec_report

    描述: 欧佩克报告, 数据区间从 20170118-至今

    限量: 单次返回所有历史数据, 以网页数据为准
    """
    try:
        macro_cons_opec_month = ak.macro_cons_opec_month()
        macro_cons_opec_month_df = sanitize_data_pandas(macro_cons_opec_month)
        return macro_cons_opec_month_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-伦敦金属交易所-持仓报告
@router.get("/macro_euro_lme_holding",
            operation_id="get_macro_euro_lme_holding")
async def get_macro_euro_lme_holding():
    """
    重要机构-伦敦金属交易所-持仓报告

    接口: macro_euro_lme_holding

    目标地址: https://datacenter.jin10.com/reportType/dc_lme_traders_report

    描述: 伦敦金属交易所(LME)-持仓报告, 数据区间从 20151022-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_lme_holding = ak.macro_euro_lme_holding()
        macro_euro_lme_holding_df = sanitize_data_pandas(macro_euro_lme_holding)
        return macro_euro_lme_holding_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-伦敦金属交易所-持仓报告
@router.get("/macro_euro_lme_stock",
            operation_id="get_macro_euro_lme_stock")
async def get_macro_euro_lme_stock():
    """
    重要机构-伦敦金属交易所-库存报告

    接口: macro_euro_lme_stock

    目标地址: https://datacenter.jin10.com/reportType/dc_lme_report

    描述: 伦敦金属交易所(LME)-库存报告, 数据区间从 20140702-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_euro_lme_stock = ak.macro_euro_lme_stock()
        macro_euro_lme_stock_df = sanitize_data_pandas(macro_euro_lme_stock)
        return macro_euro_lme_stock_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-美国商品期货交易委员会-外汇类非商业持仓报告
@router.get("/macro_usa_cftc_nc_holding",
            operation_id="get_macro_usa_cftc_nc_holding")
async def get_macro_usa_cftc_nc_holding():
    """
    重要机构-美国商品期货交易委员会-外汇类非商业持仓报告

    接口: macro_usa_cftc_nc_holding

    目标地址: https://datacenter.jin10.com/reportType/dc_cftc_nc_report

    描述: 美国商品期货交易委员会CFTC外汇类非商业持仓报告, 数据区间从 19830107-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cftc_nc_holding = ak.macro_usa_cftc_nc_holding()
        macro_usa_cftc_nc_holding_df = sanitize_data_pandas(macro_usa_cftc_nc_holding)
        return macro_usa_cftc_nc_holding_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-美国商品期货交易委员会-商品类非商业持仓报告
@router.get("/macro_usa_cftc_c_holding",
            operation_id="get_macro_usa_cftc_c_holding")
async def get_macro_usa_cftc_c_holding():
    """
    重要机构-美国商品期货交易委员会-商品类非商业持仓报告

    接口: macro_usa_cftc_c_holding

    目标地址: https://datacenter.jin10.com/reportType/dc_cftc_c_report

    描述: 美国商品期货交易委员会CFTC商品类非商业持仓报告, 数据区间从 19830107-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cftc_c_holding = ak.macro_usa_cftc_c_holding()
        macro_usa_cftc_c_holding_df = sanitize_data_pandas(macro_usa_cftc_c_holding)
        return macro_usa_cftc_c_holding_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-美国商品期货交易委员会-外汇类商业持仓报告
@router.get("/macro_usa_cftc_merchant_currency_holding",
            operation_id="get_macro_usa_cftc_merchant_currency_holding")
async def get_macro_usa_cftc_merchant_currency_holding():
    """
    重要机构-美国商品期货交易委员会-外汇类商业持仓报告

    接口: macro_usa_cftc_merchant_currency_holding

    目标地址: https://datacenter.jin10.com/reportType/dc_cftc_merchant_currency

    描述: 美国商品期货交易委员会CFTC外汇类商业持仓报告, 数据区间从 19860115-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cftc_merchant_currency_holding = ak.macro_usa_cftc_merchant_currency_holding()
        macro_usa_cftc_merchant_currency_holding_df = sanitize_data_pandas(macro_usa_cftc_merchant_currency_holding)
        return macro_usa_cftc_merchant_currency_holding_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-美国商品期货交易委员会-商品类商业持仓报告
@router.get("/macro_usa_cftc_merchant_goods_holding",
            operation_id="get_macro_usa_cftc_merchant_goods_holding")
async def get_macro_usa_cftc_merchant_goods_holding():
    """
    重要机构-美国商品期货交易委员会-商品类商业持仓报告

    接口: macro_usa_cftc_merchant_goods_holding

    目标地址: https://datacenter.jin10.com/reportType/dc_cftc_merchant_goods

    描述: 美国商品期货交易委员会 CFTC 商品类商业持仓报告, 数据区间从 19860115-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cftc_merchant_goods_holding = ak.macro_usa_cftc_merchant_goods_holding()
        macro_usa_cftc_merchant_goods_holding_df = sanitize_data_pandas(macro_usa_cftc_merchant_goods_holding)
        return macro_usa_cftc_merchant_goods_holding_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 重要机构-芝加哥交易所-贵金属
@router.get("/macro_usa_cme_merchant_goods_holding",
            operation_id="get_macro_usa_cme_merchant_goods_holding")
async def get_macro_usa_cme_merchant_goods_holding():
    """
    重要机构-芝加哥交易所-贵金属

    接口: macro_usa_cme_merchant_goods_holding

    目标地址: https://datacenter.jin10.com/org

    描述: CME-贵金属, 数据区间从 20180405-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_cme_merchant_goods_holding = ak.macro_usa_cme_merchant_goods_holding()
        macro_usa_cme_merchant_goods_holding_df = sanitize_data_pandas(macro_usa_cme_merchant_goods_holding)
        return macro_usa_cme_merchant_goods_holding_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
