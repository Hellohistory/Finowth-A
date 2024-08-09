import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-经济状况-企业商品价格指数
@router.get("/macro_china_qyspjg", operation_id="macro_china_qyspjg")
async def macro_china_qyspjg():
    """
    国民经济运行状况-经济状况-企业商品价格指数

    接口: macro_china_qyspjg

    目标地址: http://data.eastmoney.com/cjsj/qyspjg.html

    描述: 东方财富-经济数据一览-中国-企业商品价格指数, 数据区间从 20050101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_qyspjg = ak.macro_china_qyspjg()
        macro_china_qyspjg_df = sanitize_data_pandas(macro_china_qyspjg)
        return macro_china_qyspjg_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-外商直接投资数据
@router.get("/macro_china_fdi", operation_id="macro_china_fdi")
async def macro_china_fdi():
    """
    国民经济运行状况-经济状况-外商直接投资数据

    接口: macro_china_fdi

    目标地址: https://data.eastmoney.com/cjsj/qyspjg.html

    描述: 东方财富-经济数据一览-中国-外商直接投资数据, 数据区间从 200801-202012

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_fdi = ak.macro_china_fdi()
        macro_china_fdi_df = sanitize_data_pandas(macro_china_fdi)
        return macro_china_fdi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-LPR品种数据
@router.get("/macro_china_lpr", operation_id="macro_china_lpr")
async def macro_china_lpr():
    """
    国民经济运行状况-经济状况-LPR品种数据

    接口: macro_china_lpr

    目标地址: https://data.eastmoney.com/cjsj/globalRateLPR.html

    描述: 中国 LPR 品种数据, 数据区间从 19910421-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_lpr = ak.macro_china_lpr()
        macro_china_lpr_df = sanitize_data_pandas(macro_china_lpr)
        return macro_china_lpr_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-城镇调查失业率
@router.get("/macro_china_urban_unemployment",
            operation_id="macro_china_urban_unemployment")
async def macro_china_urban_unemployment():
    """
    国民经济运行状况-经济状况-城镇调查失业率

    接口: macro_china_urban_unemployment

    目标地址: https://data.stats.gov.cn/easyquery.htm?cn=A01&zb=A0203&sj=202304

    描述: 国家统计局-月度数据-城镇调查失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_urban_unemployment = ak.macro_china_urban_unemployment()
        macro_china_urban_unemployment_df = sanitize_data_pandas(macro_china_urban_unemployment)
        return macro_china_urban_unemployment_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-社会融资规模增量统计
@router.get("/macro_china_shrzgm",
            operation_id="macro_china_shrzgm")
async def macro_china_shrzgm():
    """
    国民经济运行状况-经济状况-社会融资规模增量统计

    接口: macro_china_urban_unemployment

    目标地址: https://data.stats.gov.cn/easyquery.htm?cn=A01&zb=A0203&sj=202304

    描述: 国家统计局-月度数据-城镇调查失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_shrzgm = ak.macro_china_shrzgm()
        macro_china_shrzgm_df = sanitize_data_pandas(macro_china_shrzgm)
        return macro_china_shrzgm_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-中国 GDP 年率
@router.get("/macro_china_gdp_yearly",
            operation_id="macro_china_gdp_yearly")
async def macro_china_gdp_yearly():
    """
    国民经济运行状况-经济状况-中国 GDP 年率

    接口: macro_china_gdp_yearly

    目标地址: https://datacenter.jin10.com/reportType/dc_chinese_gdp_yoy

    描述: 金十数据中心-中国 GDP 年率报告, 数据区间从 20110120-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_gdp_yearly = ak.macro_china_gdp_yearly()
        macro_china_gdp_yearly_df = sanitize_data_pandas(macro_china_gdp_yearly)
        return macro_china_gdp_yearly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-新增信贷数据
@router.get("/macro_china_new_financial_credit",
            operation_id="macro_china_new_financial_credit")
async def macro_china_new_financial_credit():
    """
    国民经济运行状况-经济状况-新增信贷数据

    接口: macro_china_new_financial_credit

    目标地址: http://data.eastmoney.com/cjsj/xzxd.html

    描述: 中国新增信贷数据数据, 数据区间从 200801 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_new_financial_credit = ak.macro_china_new_financial_credit()
        macro_china_new_financial_credit_df = sanitize_data_pandas(macro_china_new_financial_credit)
        return macro_china_new_financial_credit_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-居民消费价格指数
@router.get("/macro_china_cpi",
            operation_id="macro_china_cpi")
async def macro_china_cpi():
    """
    国民经济运行状况-经济状况-居民消费价格指数

    接口: macro_china_cpi

    目标地址: http://data.eastmoney.com/cjsj/cpi.html

    描述: 中国居民消费价格指数, 数据区间从 200801 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_cpi = ak.macro_china_cpi()
        macro_china_cpi_df = sanitize_data_pandas(macro_china_cpi)
        return macro_china_cpi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-国内生产总值
@router.get("/macro_china_gdp",
            operation_id="macro_china_gdp")
async def macro_china_gdp():
    """
    国民经济运行状况-经济状况-国内生产总值

    接口: macro_china_gdp

    目标地址: http://data.eastmoney.com/cjsj/gdp.html

    描述: 中国国内生产总值, 数据区间从 200601 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_gdp = ak.macro_china_gdp()
        macro_china_gdp_df = sanitize_data_pandas(macro_china_gdp)
        return macro_china_gdp_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-本外币存款
@router.get("/macro_china_wbck",
            operation_id="macro_china_wbck")
async def macro_china_wbck():
    """
    国民经济运行状况-经济状况-本外币存款

    接口: macro_china_wbck

    目标地址: http://data.eastmoney.com/cjsj/wbck.html

    描述: 本外币存款, 数据区间从 200802 至今, 月度数据

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_wbck = ak.macro_china_wbck()
        macro_china_wbck_df = sanitize_data_pandas(macro_china_wbck)
        return macro_china_wbck_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-存款准备金率
@router.get("/macro_china_reserve_requirement_ratio",
            operation_id="macro_china_reserve_requirement_ratio")
async def macro_china_reserve_requirement_ratio():
    """
    国民经济运行状况-经济状况-存款准备金率

    接口: macro_china_reserve_requirement_ratio

    目标地址: https://data.eastmoney.com/cjsj/ckzbj.html

    描述: 国家统计局-存款准备金率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_reserve_requirement_ratio = ak.macro_china_reserve_requirement_ratio()
        macro_china_reserve_requirement_ratio_df = sanitize_data_pandas(macro_china_reserve_requirement_ratio)
        return macro_china_reserve_requirement_ratio_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-国际旅游外汇收入构成
@router.get("/macro_china_international_tourism_fx",
            operation_id="macro_china_international_tourism_fx")
async def macro_china_international_tourism_fx():
    """
    国民经济运行状况-经济状况-国际旅游外汇收入构成

    接口: macro_china_international_tourism_fx

    目标地址: http://finance.sina.com.cn/mac/#industry-15-0-31-3

    描述: 国家统计局-国际旅游外汇收入构成

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_international_tourism_fx = ak.macro_china_international_tourism_fx()
        macro_china_international_tourism_fx_df = sanitize_data_pandas(macro_china_international_tourism_fx)
        return macro_china_international_tourism_fx_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-保险业经营情况
@router.get("/macro_china_insurance",
            operation_id="macro_china_insurance")
async def macro_china_insurance():
    """
    国民经济运行状况-经济状况-保险业经营情况

    接口: macro_china_insurance

    目标地址: http://finance.sina.com.cn/mac/#fininfo-19-0-31-3

    描述: 新浪财经-中国宏观经济数据-保险业经营情况

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_insurance = ak.macro_china_insurance()
        macro_china_insurance_df = sanitize_data_pandas(macro_china_insurance)
        return macro_china_insurance_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
