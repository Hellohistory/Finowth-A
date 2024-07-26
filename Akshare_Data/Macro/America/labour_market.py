import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-劳动力市场-LMCI
@router.get("/macro_usa_lmci",
            operation_id="get_macro_usa_lmci")
async def get_macro_usa_lmci():
    """
    美国-劳动力市场-LMCI

    接口: macro_usa_lmci

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_lmci

    描述: 美联储劳动力市场状况指数报告, 数据区间从 20141006-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_lmci = ak.macro_usa_lmci()
        macro_usa_lmci_df = sanitize_data_pandas(macro_usa_lmci)
        return macro_usa_lmci_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-劳动力市场-失业率-美国失业率报告
@router.get("/macro_usa_unemployment_rate",
            operation_id="get_macro_usa_unemployment_rate")
async def get_macro_usa_unemployment_rate():
    """
    美国-劳动力市场-失业率-美国失业率报告

    接口: macro_usa_unemployment_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_unemployment_rate

    描述: 美国失业率报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_unemployment_rate = ak.macro_usa_unemployment_rate()
        macro_usa_unemployment_rate_df = sanitize_data_pandas(macro_usa_unemployment_rate)
        return macro_usa_unemployment_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-劳动力市场-失业率-美国挑战者企业裁员人数报告
@router.get("/macro_usa_job_cuts",
            operation_id="get_macro_usa_job_cuts")
async def get_macro_usa_job_cuts():
    """
    美国-劳动力市场-失业率-美国挑战者企业裁员人数报告

    接口: macro_usa_job_cuts

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_job_cuts

    描述: 美国挑战者企业裁员人数报告, 数据区间从 19940201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_job_cuts = ak.macro_usa_job_cuts()
        macro_usa_job_cuts_df = sanitize_data_pandas(macro_usa_job_cuts)
        return macro_usa_job_cuts_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-劳动力市场-就业人口-美国非农就业人数报告
@router.get("/macro_usa_non_farm",
            operation_id="get_macro_usa_non_farm")
async def get_macro_usa_non_farm():
    """
    美国-劳动力市场-就业人口-美国非农就业人数报告

    接口: macro_usa_non_farm

    目标地址: https://datacenter.jin10.com/reportType/dc_nonfarm_payrolls

    描述: 美国非农就业人数报告, 数据区间从 19700102-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_non_farm = ak.macro_usa_non_farm()
        macro_usa_non_farm_df = sanitize_data_pandas(macro_usa_non_farm)
        return macro_usa_non_farm_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-劳动力市场-就业人口-美国ADP就业人数报告
@router.get("/macro_usa_adp_employment",
            operation_id="get_macro_usa_adp_employment")
async def get_macro_usa_adp_employment():
    """
    美国-劳动力市场-就业人口-美国ADP就业人数报告

    接口: macro_usa_adp_employment

    目标地址: https://datacenter.jin10.com/reportType/dc_adp_nonfarm_employment

    描述: 美国 ADP 就业人数报告, 数据区间从 20010601-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_adp_employment = ak.macro_usa_adp_employment()
        macro_usa_adp_employment_df = sanitize_data_pandas(macro_usa_adp_employment)
        return macro_usa_adp_employment_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
