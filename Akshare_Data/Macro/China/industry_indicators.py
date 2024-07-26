import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-产业指标-工业增加值增长
@router.get("/macro_china_gyzjz", operation_id="get_macro_china_gyzjz")
async def get_macro_china_gyzjz():
    """
    国民经济运行状况-产业指标-工业增加值增长

    接口: macro_china_gyzjz

    目标地址: https://data.eastmoney.com/cjsj/gyzjz.html

    描述: 东方财富-中国工业增加值增长, 数据区间从 2008 - 至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_gyzjz = ak.macro_china_gyzjz()
        macro_china_gyzjz_df = sanitize_data_pandas(macro_china_gyzjz)
        return macro_china_gyzjz_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-产业指标-规模以上工业增加值年率
@router.get("/macro_china_industrial_production_yoy", operation_id="get_macro_china_industrial_production_yoy")
async def get_macro_china_industrial_production_yoy():
    """
    国民经济运行状况-产业指标-规模以上工业增加值年率

    接口: macro_china_industrial_production_yoy

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_industrial_production_yoy

    描述: 中国规模以上工业增加值年率报告, 数据区间从 19900301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_industrial_production_yoy = ak.macro_china_industrial_production_yoy()
        macro_china_industrial_production_yoy_df = sanitize_data_pandas(macro_china_industrial_production_yoy)
        return macro_china_industrial_production_yoy_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-产业指标-官方制造业 PMI
@router.get("/macro_china_pmi_yearly", operation_id="get_macro_china_pmi_yearly")
async def get_macro_china_pmi_yearly():
    """
    国民经济运行状况-产业指标-官方制造业 PMI

    接口: macro_china_pmi_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_pmi

    描述: 中国官方制造业 PMI 数据, 数据区间从 2005-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_pmi_yearly = ak.macro_china_pmi_yearly()
        macro_china_pmi_yearly_df = sanitize_data_pandas(macro_china_pmi_yearly)
        return macro_china_pmi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-产业指标-财新制造业PMI终值
@router.get("/macro_china_cx_pmi_yearly", operation_id="get_macro_china_cx_pmi_yearly")
async def get_macro_china_cx_pmi_yearly():
    """
    国民经济运行状况-产业指标-财新制造业PMI终值

    接口: macro_china_cx_pmi_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_caixin_manufacturing_pmi

    描述: 中国年度财新 PMI 数据, 数据区间从 20120120-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_cx_pmi_yearly = ak.macro_china_cx_pmi_yearly()
        macro_china_cx_pmi_yearly_df = sanitize_data_pandas(macro_china_cx_pmi_yearly)
        return macro_china_cx_pmi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-产业指标-财新服务业PMI
@router.get("/macro_china_cx_services_pmi_yearly", operation_id="get_macro_china_cx_services_pmi_yearly")
async def get_macro_china_cx_services_pmi_yearly():
    """
    国民经济运行状况-产业指标-财新服务业PMI

    接口: macro_china_cx_services_pmi_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_caixin_services_pmi

    描述: 中国财新服务业 PMI 报告, 数据区间从 20120405-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_cx_services_pmi_yearly = ak.macro_china_cx_services_pmi_yearly()
        macro_china_cx_services_pmi_yearly_df = sanitize_data_pandas(macro_china_cx_services_pmi_yearly)
        return macro_china_cx_services_pmi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-产业指标-中国官方非制造业PMI
@router.get("/macro_china_non_man_pmi", operation_id="get_macro_china_non_man_pmi")
async def get_macro_china_non_man_pmi():
    """
    国民经济运行状况-产业指标-中国官方非制造业PMI

    接口: macro_china_non_man_pmi

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_non_manufacturing_pmi

    描述: 中国官方非制造业 PMI, 数据区间从 20160101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_non_man_pmi = ak.macro_china_non_man_pmi()
        macro_china_non_man_pmi_df = sanitize_data_pandas(macro_china_non_man_pmi)
        return macro_china_non_man_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-产业指标-工业品出厂价格指数
@router.get("/macro_china_ppi", operation_id="get_macro_china_ppi")
async def get_macro_china_ppi():
    """
    国民经济运行状况-产业指标-工业品出厂价格指数

    接口: macro_china_ppi

    目标地址: http://data.eastmoney.com/cjsj/ppi.html

    描述: 工业品出厂价格指数, 数据区间从 200601 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_ppi = ak.macro_china_ppi()
        macro_china_ppi_df = sanitize_data_pandas(macro_china_ppi)
        return macro_china_ppi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
