import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class BondPageRequest(BaseModel):
    page: str = Field(..., title="需要获取页面", description="例：1")


# 债券-债券基础数据-银行间市场债券发行基础数据
@router.post("/bond_debt_nafmii", operation_id="post_bond_debt_nafmii")
def post_bond_debt_nafmii(request: BondPageRequest):
    """
    债券-上交所债券-债券现券市场概览

    接口: bond_debt_nafmii

    目标地址: http://zhuce.nafmii.org.cn/fans/publicQuery/manager

    描述: 中国银行间市场交易商协会-非金融企业债务融资工具注册信息系统

    限量: 单次获取指定 page 页面数据的 50 条数据
    """
    try:
        bond_debt_nafmii = ak.bond_debt_nafmii(page=request.page)
        bond_debt_nafmii_df = sanitize_data_pandas(bond_debt_nafmii)

        return bond_debt_nafmii_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-中国债券市场行情数据-现券市场做市报价
@router.get("/bond_spot_quote", operation_id="get_bond_spot_quote")
async def get_bond_spot_quote():
    """
    债券-上交所债券-债券现券市场概览

    接口: bond_spot_quote

    目标地址: https://www.chinamoney.com.cn/chinese/mkdatabond/

    描述: 中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-债券市场行情-现券市场做市报价

    限量: 单次返回所有数据
    """
    try:
        bond_spot_quote = ak.bond_spot_quote()
        bond_spot_quote_df = sanitize_data_pandas(bond_spot_quote)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_spot_quote_df.to_dict(orient="records")


# 债券-中国债券市场行情数据-现券市场成交行情
@router.get("/bond_spot_deal", operation_id="get_bond_spot_deal")
async def get_bond_spot_deal():
    """
    债券-上交所债券-现券市场成交行情

    接口: bond_spot_deal

    目标地址: https://www.chinamoney.com.cn/chinese/mkdatabond/

    描述: 中国外汇交易中心暨全国银行间同业拆借中心-市场数据-市场行情-债券市场行情-现券市场成交行情

    限量: 单次返回所有即期数据
    """
    try:
        bond_spot_deal = ak.bond_spot_deal()
        bond_spot_deal_df = sanitize_data_pandas(bond_spot_deal)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_spot_deal_df.to_dict(orient="records")


class BondChinaYield(BaseModel):
    start_date: str = Field(..., title="指定开始日期", description="例：20190204")
    end_date: str = Field(..., title="指定结束日期", description="例：20190224")


# 债券-债券基础数据-国债及其他债券收益率曲线
@router.post("/bond_china_yield", operation_id="post_bond_china_yield")
def post_bond_china_yield(request: BondChinaYield):
    """
    债券-上交所债券-国债及其他债券收益率曲线

    接口: bond_china_yield

    目标地址: https://yield.chinabond.com.cn/cbweb-pbc-web/pbc/historyQuery?startDate=2019-02-07&endDate=2020-02-04&gjqx=0&qxId=ycqx&locale=cn_ZH

    描述: 中国债券信息网-国债及其他债券收益率曲线

    限量: 单次返回所有指定日期间指定开始日期到指定结束日期需要小于一年的所有数据
    """
    try:
        bond_china_yield = ak.bond_china_yield(
            start_date=request.start_date,
            end_date=request.end_date
        )
        bond_china_yield_df = sanitize_data_pandas(bond_china_yield)

        return bond_china_yield_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
