import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美联储利率决议报告
@router.get("/interest_macro_bank_usa_interest_rate",
            operation_id="interest_macro_bank_usa_interest_rate")
async def interest_macro_bank_usa_interest_rate():
    """
    接口: macro_bank_usa_interest_rate

    """
    try:
        interest_macro_bank_usa_interest_rate = ak.macro_bank_usa_interest_rate()
        interest_macro_bank_usa_interest_rate_df = sanitize_data_pandas(interest_macro_bank_usa_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_usa_interest_rate_df.to_dict(orient="records")


# 欧洲央行决议报告
@router.get("/interest_macro_bank_euro_interest_rate",
            operation_id="interest_macro_bank_euro_interest_rate")
async def interest_macro_bank_euro_interest_rate():
    """
    接口: macro_bank_euro_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_interest_rate_decision

    描述: 欧洲央行决议报告, 数据区间从 19990101-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_euro_interest_rate = ak.macro_bank_euro_interest_rate()
        interest_macro_bank_euro_interest_rate_df = sanitize_data_pandas(interest_macro_bank_euro_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_euro_interest_rate_df.to_dict(orient="records")


# 新西兰联储决议报告
@router.get("/interest_macro_bank_newzealand_interest_rate",
            operation_id="interest_macro_bank_newzealand_interest_rate")
async def interest_macro_bank_newzealand_interest_rate():
    """
    接口: macro_bank_newzealand_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_newzealand_interest_rate_decision

    描述: 新西兰联储决议报告, 数据区间从 19990401-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_newzealand_interest_rate = ak.macro_bank_newzealand_interest_rate()
        interest_macro_bank_newzealand_interest_rate_df = sanitize_data_pandas(
            interest_macro_bank_newzealand_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_newzealand_interest_rate_df.to_dict(orient="records")


# 瑞士央行利率决议报告
@router.get("/interest_macro_bank_switzerland_interest_rate",
            operation_id="interest_macro_bank_switzerland_interest_rate")
async def interest_macro_bank_switzerland_interest_rate():
    """
    接口: macro_bank_switzerland_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_switzerland_interest_rate_decision

    描述: 瑞士央行利率决议报告, 数据区间从20080313-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_switzerland_interest_rate = ak.macro_bank_switzerland_interest_rate()
        interest_macro_bank_switzerland_interest_rate_df = sanitize_data_pandas(
            interest_macro_bank_switzerland_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_switzerland_interest_rate_df.to_dict(orient="records")


# 英国央行决议报告
@router.get("/interest_macro_bank_english_interest_rate", operation_id="interest_macro_bank_english_interest_rate")
async def interest_macro_bank_english_interest_rate():
    """
    接口: macro_bank_english_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_english_interest_rate_decision

    描述: 英国央行决议报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_english_interest_rate = ak.macro_bank_english_interest_rate()
        interest_macro_bank_english_interest_rate_df = sanitize_data_pandas(interest_macro_bank_english_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_english_interest_rate_df.to_dict(orient="records")


# 澳洲联储决议报告
@router.get("/interest_macro_bank_australia_interest_rate",
            operation_id="interest_macro_bank_australia_interest_rate")
async def interest_macro_bank_australia_interest_rate():
    """
    接口: macro_bank_australia_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_australia_interest_rate_decision

    描述: 澳洲联储决议报告, 数据区间从 19800201-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_australia_interest_rate = ak.macro_bank_australia_interest_rate()
        interest_macro_bank_australia_interest_rate_df = sanitize_data_pandas(
            interest_macro_bank_australia_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_australia_interest_rate_df.to_dict(orient="records")


# 日本利率决议报告
@router.get("/interest_macro_bank_japan_interest_rate",
            operation_id="interest_macro_bank_japan_interest_rate")
async def interest_macro_bank_japan_interest_rate():
    """
    接口: macro_bank_japan_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_japan_interest_rate_decision

    描述: 日本利率决议报告, 数据区间从 20080214-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_japan_interest_rate = ak.macro_bank_japan_interest_rate()
        interest_macro_bank_japan_interest_rate_df = sanitize_data_pandas(interest_macro_bank_japan_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_japan_interest_rate_df.to_dict(orient="records")


# 俄罗斯利率决议报告
@router.get("/interest_macro_bank_russia_interest_rate",
            operation_id="interest_macro_bank_russia_interest_rate")
async def interest_macro_bank_russia_interest_rate():
    """
    接口: macro_bank_russia_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_russia_interest_rate_decision

    描述: 俄罗斯利率决议报告, 数据区间从 20030601-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_russia_interest_rate = ak.macro_bank_russia_interest_rate()
        interest_macro_bank_russia_interest_rate_df = sanitize_data_pandas(interest_macro_bank_russia_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_russia_interest_rate_df.to_dict(orient="records")


# 印度利率决议报告
@router.get("/interest_macro_bank_india_interest_rate", operation_id="interest_macro_bank_india_interest_rate")
async def interest_macro_bank_india_interest_rate():
    """
    接口: macro_bank_india_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_india_interest_rate_decision

    描述: 印度利率决议报告, 数据区间从 20000801-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_india_interest_rate = ak.macro_bank_india_interest_rate()
        interest_macro_bank_india_interest_rate_df = sanitize_data_pandas(interest_macro_bank_india_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_india_interest_rate_df.to_dict(orient="records")


# 巴西利率决议报告
@router.get("/interest_macro_bank_brazil_interest_rate",
            operation_id="interest_macro_bank_brazil_interest_rate")
async def interest_macro_bank_brazil_interest_rate():
    """
    接口: macro_bank_brazil_interest_rate

    目标地址: https://datacenter.jin10.com/reportType/dc_brazil_interest_rate_decision

    描述: 巴西利率决议报告, 数据区间从20080201-至今

    限量: 单次返回所有历史数据
    """
    try:
        interest_macro_bank_brazil_interest_rate = ak.macro_bank_brazil_interest_rate()
        interest_macro_bank_brazil_interest_rate_df = sanitize_data_pandas(interest_macro_bank_brazil_interest_rate)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return interest_macro_bank_brazil_interest_rate_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
