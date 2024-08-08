import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-东方财富-分红送配-基金分红
@router.get("/fund_fh_em", operation_id="get_fund_fh_em")
async def get_fund_fh_em():
    """
    公募基金数据-东方财富-分红送配-基金分红

    接口: fund_fh_em

    目标地址: http://fund.eastmoney.com/data/fundfenhong.html

    描述: 天天基金网-基金数据-分红送配-基金分红

    限量: 单次返回所有历史数据
    """
    try:
        fund_fh_em = ak.fund_fh_em()
        fund_fh_em_df = sanitize_data_pandas(fund_fh_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_fh_em_df.to_dict(orient="records")


# 公募基金数据-东方财富-分红送配-基金拆分
@router.get("/fund_cf_em", operation_id="get_fund_cf_em")
async def get_fund_cf_em():
    """
    公募基金数据-东方财富-分红送配-基金拆分

    接口: fund_cf_em

    目标地址: http://fund.eastmoney.com/data/fundchaifen.html

    描述: 天天基金网-基金数据-分红送配-基金拆分

    限量: 单次返回所有历史数据
    """
    try:
        fund_cf_em = ak.fund_cf_em()
        fund_cf_em_df = sanitize_data_pandas(fund_cf_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_cf_em_df.to_dict(orient="records")


# 公募基金数据-东方财富-分红送配-基金分红排行
@router.get("/fund_fh_rank_em", operation_id="get_fund_fh_rank_em")
async def get_fund_fh_rank_em():
    """
    公募基金数据-东方财富-分红送配-基金拆分

    接口: fund_fh_rank_em

    目标地址: http://fund.eastmoney.com/data/fundleijifenhong.html

    描述: 天天基金网-基金数据-分红送配-基金分红排行

    限量: 单次返回所有历史数据
    """
    try:
        fund_fh_rank_em = ak.fund_fh_rank_em()
        fund_fh_rank_em_df = sanitize_data_pandas(fund_fh_rank_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_fh_rank_em_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
