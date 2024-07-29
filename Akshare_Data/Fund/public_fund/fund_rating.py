import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-东方财富-基金评级-基金评级总汇
@router.get("/fund_rating_all", operation_id="get_fund_rating_all")
async def get_fund_rating_all():
    """
    公募基金数据-东方财富-基金评级-基金评级总汇

    接口: fund_rating_all

    目标地址: https://fund.eastmoney.com/data/fundrating.html

    描述: 天天基金网-基金评级-基金评级总汇

    限量: 单次返回所有基金评级数据
    """
    try:
        fund_rating_all = ak.fund_rating_all()
        fund_rating_all_df = sanitize_data_pandas(fund_rating_all)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_rating_all_df.to_dict(orient="records")


class FundRating(BaseModel):
    date: str = Field(..., title="指定日期",
                      description="通过 https://fund.eastmoney.com/data/fundrating_3.html 获取查询日期")


# 公募基金数据-东方财富-基金评级-上海证券评级
@router.post("/fund_rating_sh",
             operation_id="post_fund_rating_sh")
def post_fund_rating_sh(request: FundRating):
    """
    公募基金数据-东方财富-基金评级-上海证券评级

    接口: fund_rating_sh

    目标地址: https://fund.eastmoney.com/data/fundrating_3.html

    描述: 天天基金网-基金评级-上海证券评级

    限量: 单次返回指定交易日的所有基金评级数据
    """
    try:
        fund_rating_sh = ak.fund_rating_sh(
            date=request.date
        )
        fund_rating_sh_df = sanitize_data_pandas(fund_rating_sh)

        return fund_rating_sh_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-东方财富-基金评级-招商证券评级
@router.post("/fund_rating_zs",
             operation_id="post_fund_rating_zs")
def post_fund_rating_zs(request: FundRating):
    """
    公募基金数据-东方财富-基金评级-招商证券评级

    接口: fund_rating_zs

    目标地址: http://fund.eastmoney.com/data/fundrating_2.html

    描述: 天天基金网-基金评级-招商证券评级

    限量: 单次返回指定交易日的所有基金评级数据
    """
    try:
        fund_rating_zs = ak.fund_rating_zs(
            date=request.date
        )
        fund_rating_zs_df = sanitize_data_pandas(fund_rating_zs)

        return fund_rating_zs_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-东方财富-基金评级-招商证券评级
@router.post("/fund_rating_ja",
             operation_id="post_fund_rating_ja")
def post_fund_rating_ja(request: FundRating):
    """
    公募基金数据-东方财富-基金评级-招商证券评级

    接口: fund_rating_ja

    目标地址: https://fund.eastmoney.com/data/fundrating_4.html

    描述: 天天基金网-基金评级-济安金信评级

    限量: 单次返回指定交易日的所有基金评级数据
    """
    try:
        fund_rating_ja = ak.fund_rating_ja(
            date=request.date
        )
        fund_rating_ja_df = sanitize_data_pandas(fund_rating_ja)

        return fund_rating_ja_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-东方财富-基金评级-基金评级总汇
@router.get("/fund_manager_em", operation_id="get_fund_manager_em")
async def get_fund_manager_em():
    """
    公募基金数据-东方财富-基金评级-基金评级总汇

    接口: fund_manager_em

    目标地址: https://fund.eastmoney.com/manager/default.html

    描述: 天天基金网-基金数据-基金经理大全

    限量: 单次返回所有基金经理数据
    """
    try:
        fund_manager_em = ak.fund_manager_em()
        fund_manager_em_df = sanitize_data_pandas(fund_manager_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_manager_em_df.to_dict(orient="records")


# 公募基金数据-东方财富-基金评级-新发基金
@router.get("/fund_new_found_em", operation_id="get_fund_new_found_em")
async def get_fund_new_found_em():
    """
    公募基金数据-东方财富-基金评级-新发基金

    接口: fund_new_found_em

    目标地址: https://fund.eastmoney.com/data/xinfound.html

    描述: 天天基金网-基金数据-新发基金-新成立基金

    限量: 单次返回所有新发基金数据
    """
    try:
        fund_new_found_em = ak.fund_new_found_em()
        fund_new_found_em_df = sanitize_data_pandas(fund_new_found_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_new_found_em_df.to_dict(orient="records")
