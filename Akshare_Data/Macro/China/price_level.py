import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-物价水平-中国 CPI 年率报告
@router.get("/macro_china_cpi_yearly", operation_id="get_macro_china_cpi_yearly")
async def get_macro_china_cpi_yearly():
    """
    国民经济运行状况-物价水平-中国 CPI 年率报告

    接口: macro_china_cpi_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_cpi_yoy

    描述: 中国年度 CPI 数据, 数据区间从 19860201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_cpi_yearly = ak.macro_china_cpi_yearly()
        macro_china_cpi_yearly_df = sanitize_data_pandas(macro_china_cpi_yearly)
        return macro_china_cpi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-中国 CPI 月率报告
@router.get("/macro_china_cpi_monthly", operation_id="get_macro_china_cpi_monthly")
async def get_macro_china_cpi_monthly():
    """
    国民经济运行状况-物价水平-中国 CPI 月率报告

    接口: macro_china_cpi_monthly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_cpi_mom

    描述: 中国月度 CPI 数据, 数据区间从 19960201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_cpi_monthly = ak.macro_china_cpi_monthly()
        macro_china_cpi_monthly_df = sanitize_data_pandas(macro_china_cpi_monthly)
        return macro_china_cpi_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-中国 PPI 年率报告
@router.get("/macro_china_ppi_yearly", operation_id="get_macro_china_ppi_yearly")
async def get_macro_china_ppi_yearly():
    """
    国民经济运行状况-物价水平-中国 PPI 年率报告

    接口: macro_china_ppi_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_ppi_yoy

    描述: 中国年度 PPI 数据, 数据区间从 19950801-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_ppi_yearly = ak.macro_china_ppi_yearly()
        macro_china_ppi_yearly_df = sanitize_data_pandas(macro_china_ppi_yearly)
        return macro_china_ppi_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-采购经理人指数
@router.get("/macro_china_pmi",
            operation_id="get_mmacro_china_pmi")
async def get_mmacro_china_pmi():
    """
    国民经济运行状况-物价水平-采购经理人指数

    接口: macro_china_pmi

    目标地址: http://data.eastmoney.com/cjsj/pmi.html

    描述: 采购经理人指数, 数据区间从 200801 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_pmi = ak.macro_china_pmi()
        macro_china_pmi_df = sanitize_data_pandas(macro_china_pmi)
        return macro_china_pmi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-物价水平-消费者信心指数
@router.get("/macro_china_xfzxx",
            operation_id="get_macro_china_xfzxx")
async def get_macro_china_xfzxx():
    """
    国民经济运行状况-物价水平-消费者信心指数

    接口: macro_china_xfzxx

    目标地址: https://data.eastmoney.com/cjsj/xfzxx.html

    描述: 东方财富网-消费者信心指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_xfzxx = ak.macro_china_xfzxx()
        macro_china_xfzxx_df = sanitize_data_pandas(macro_china_xfzxx)
        return macro_china_xfzxx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
