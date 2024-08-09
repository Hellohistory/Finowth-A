import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class BondInfo(BaseModel):
    bond_name: str = Field(..., title="债券简称", description="默认为空，要查询的债券简称")
    bond_code: str = Field(..., title="债券代码", description="默认为空，要查询的债券代码")
    bond_issue: str = Field(..., title="债券发行人", description="默认为空，要查询的债券的发行人")
    bond_type: str = Field(..., title="债券类型", description="默认为空，要查询的债券类型")
    coupon_type: str = Field(..., title="票面利率类型", description="默认为空，要查询的票面利率类型")
    issue_year: str = Field(..., title="债券发行年份", description="默认为空，要查询的债券的发行年份")
    underwriter: str = Field(..., title="主承销商", description="默认为空，要查询的债券的主承销商")
    grade: str = Field(..., title="债券评级", description="默认为空，要查询的债券的评级")


# 债券-债券查询
@router.post("/bond_info_cm", operation_id="bond_info_cm")
def bond_info_cm(request: BondInfo):
    """
    债券-债券查询

    接口: bond_info_cm

    目标地址: https://www.chinamoney.com.cn/chinese/scsjzqxx/

    描述: 中国外汇交易中心暨全国银行间同业拆借中心-数据-债券信息-信息查询
    """
    try:
        bond_info_cm = ak.bond_info_cm(
            bond_name=request.bond_name,
            bond_code=request.bond_code,
            bond_issue=request.bond_issue,
            bond_type=request.bond_type,
            coupon_type=request.coupon_type,
            issue_year=request.issue_year,
            underwriter=request.underwriter,
            grade=request.grade
        )
        bond_info_cm_df = sanitize_data_pandas(bond_info_cm)

        return bond_info_cm_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BondInfoDetail(BaseModel):
    symbol: str = Field(..., title="债券简称",
                        description="例：19万林投资CP001，可通过bond_info_cm查询")


# 债券-债券基础信息
@router.post("/bond_info_detail_cm", operation_id="bond_info_detail_cm")
def bond_info_detail_cm(request: BondInfoDetail):
    """
    债券-债券基础信息

    接口: bond_info_detail_cm

    目标地址: https://www.chinamoney.com.cn/chinese/zqjc/?bondDefinedCode=egfjh08154

    描述: 中国外汇交易中心暨全国银行间同业拆借中心-数据-债券信息-信息查询-债券详情
    """
    try:
        bond_info_detail_cm = ak.bond_info_detail_cm(symbol=request.symbol)
        bond_info_detail_cm_df = sanitize_data_pandas(bond_info_detail_cm)

        return bond_info_detail_cm_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)

