import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-东方财富-规模份额-规模变动
@router.get("/fund_scale_change_em",
            operation_id="get_fund_scale_change_em")
async def get_fund_scale_change_em():
    """
    公募基金数据-东方财富-规模份额-规模变动

    接口: fund_scale_change_em

    目标地址: https://fund.eastmoney.com/data/gmbdlist.html

    描述: 天天基金网-基金数据-规模份额-规模变动

    限量: 返回所有规模变动数据
    """
    try:
        fund_scale_change_em = ak.fund_scale_change_em()
        fund_scale_change_em_df = sanitize_data_pandas(fund_scale_change_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_scale_change_em_df.to_dict(orient="records")


# 公募基金数据-东方财富-规模份额-持有人结构
@router.get("/fund_hold_structure_em",
            operation_id="get_fund_hold_structure_em")
async def get_fund_hold_structure_em():
    """
    公募基金数据-东方财富-规模份额-持有人结构

    接口: fund_hold_structure_em

    目标地址: https://fund.eastmoney.com/data/cyrjglist.html

    描述: 天天基金网-基金数据-规模份额-持有人结构

    限量: 返回所有持有人结构数据
    """
    try:
        fund_hold_structure_em = ak.fund_hold_structure_em()
        fund_hold_structure_em_df = sanitize_data_pandas(fund_hold_structure_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_hold_structure_em_df.to_dict(orient="records")
