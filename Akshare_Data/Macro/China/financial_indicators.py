import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-金融指标-外汇储备(亿美元)
@router.get("/macro_china_fx_reserves_yearly", operation_id="get_macro_china_fx_reserves_yearly")
async def get_macro_china_fx_reserves_yearly():
    """
    国民经济运行状况-金融指标-外汇储备(亿美元)

    接口: macro_china_fx_reserves_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_fx_reserves

    描述: 中国年度外汇储备数据, 数据区间从 20140115-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_fx_reserves_yearly = ak.macro_china_fx_reserves_yearly()
        macro_china_fx_reserves_yearly_df = sanitize_data_pandas(macro_china_fx_reserves_yearly)
        return macro_china_fx_reserves_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-M2货币供应年率
@router.get("/macro_china_m2_yearly", operation_id="get_macro_china_m2_yearly")
async def get_macro_china_m2_yearly():
    """
    国民经济运行状况-金融指标-M2货币供应年率

    接口: macro_china_m2_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_m2_money_supply_yoy

    描述: 中国年度 M2 数据, 数据区间从 19980201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_m2_yearly = ak.macro_china_m2_yearly()
        macro_china_m2_yearly_df = sanitize_data_pandas(macro_china_m2_yearly)
        return macro_china_m2_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-新房价指数
@router.get("/macro_china_new_house_price", operation_id="get_macro_china_new_house_price")
async def get_macro_china_new_house_price():
    """
    国民经济运行状况-金融指标-新房价指数

    接口: macro_china_new_house_price

    目标地址: http://data.eastmoney.com/cjsj/newhouse.html

    描述: 中国新房价指数月度数据, 数据区间从 201101-至今

    限量: 单次返回指定城市的所有历史数据
    """
    try:
        macro_china_new_house_price = ak.macro_china_new_house_price()
        macro_china_new_house_price_df = sanitize_data_pandas(macro_china_new_house_price)
        return macro_china_new_house_price_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-企业景气及企业家信心指数
@router.get("/macro_china_enterprise_boom_index", operation_id="get_macro_china_enterprise_boom_index")
async def get_macro_china_enterprise_boom_index():
    """
    国民经济运行状况-金融指标-企业景气及企业家信心指数

    接口: macro_china_enterprise_boom_index

    目标地址: http://data.eastmoney.com/cjsj/qyjqzs.html

    描述: 中国企业景气及企业家信心指数数据, 数据区间从 2005 一季度-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_enterprise_boom_index = ak.macro_china_enterprise_boom_index()
        macro_china_enterprise_boom_index_df = sanitize_data_pandas(macro_china_enterprise_boom_index)
        return macro_china_enterprise_boom_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-全国税收收入
@router.get("/macro_china_national_tax_receipts", operation_id="get_macro_china_national_tax_receipts")
async def get_macro_china_national_tax_receipts():
    """
    国民经济运行状况-金融指标-全国税收收入

    接口: macro_china_national_tax_receipts

    目标地址: http://data.eastmoney.com/cjsj/nationaltaxreceipts.aspx

    描述: 中国全国税收收入数据, 数据区间从 2005 一季度-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_national_tax_receipts = ak.macro_china_national_tax_receipts()
        macro_china_national_tax_receipts_df = sanitize_data_pandas(macro_china_national_tax_receipts)
        return macro_china_national_tax_receipts_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-银行理财产品发行数量
@router.get("/macro_china_bank_financing", operation_id="get_macro_china_bank_financing")
async def get_macro_china_bank_financing():
    """
    国民经济运行状况-金融指标-银行理财产品发行数量

    接口: macro_china_bank_financing

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMI01516267.html

    描述: 银行理财产品发行数量, 数据区间从 2000 一月-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_bank_financing = ak.macro_china_bank_financing()
        macro_china_bank_financing_df = sanitize_data_pandas(macro_china_bank_financing)
        return macro_china_bank_financing_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-原保险保费收入
@router.get("/macro_china_insurance_income", operation_id="get_macro_china_insurance_income")
async def get_macro_china_insurance_income():
    """
    国民经济运行状况-金融指标-原保险保费收入

    接口: macro_china_insurance_income

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMM00088870.html

    描述: 原保险保费收入, 数据区间从 200407-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_insurance_income = ak.macro_china_insurance_income()
        macro_china_insurance_income_df = sanitize_data_pandas(macro_china_insurance_income)
        return macro_china_insurance_income_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-原保险保费收入
@router.get("/macro_china_mobile_number", operation_id="get_macro_china_mobile_number")
async def get_macro_china_mobile_number():
    """
    国民经济运行状况-金融指标-原保险保费收入

    接口: macro_china_insurance_income

    目标地址: https://data.eastmoney.com/cjsj/hyzs_list_EMM00088870.html

    描述: 原保险保费收入, 数据区间从 200407-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_mobile_number = ak.macro_china_mobile_number()
        macro_china_mobile_number_df = sanitize_data_pandas(macro_china_mobile_number)
        return macro_china_mobile_number_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融指标-中国城镇固定资产投资
@router.get("/macro_china_gdzctz",
            operation_id="get_macro_china_gdzctz")
async def get_macro_china_gdzctz():
    """
    国民经济运行状况-金融指标-中国城镇固定资产投资

    接口: macro_china_gdzctz

    目标地址: http://data.eastmoney.com/cjsj/gdzctz.html

    描述: 中国城镇固定资产投资, 数据区间从 200802 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_gdzctz = ak.macro_china_gdzctz()
        macro_china_gdzctz_df = sanitize_data_pandas(macro_china_gdzctz)
        return macro_china_gdzctz_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
