import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class TreasureIssueCNInfo(BaseModel):
    start_date: str = Field(..., title="开始日期", description="例：20210911")
    end_date: str = Field(..., title="结束日期", description="例：20211110")


# 债券-债券发行-国债发行
@router.post("/bond_treasure_issue_cninfo",
             operation_id="post_bond_treasure_issue_cninfo")
async def post_bond_treasure_issue_cninfo(request: TreasureIssueCNInfo):
    """
    债券-债券发行-国债发行

    接口: bond_treasure_issue_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-债券报表-债券发行-国债发行
    """
    try:
        bond_treasure_issue_cninfo = ak.bond_treasure_issue_cninfo(
            start_date=request.start_date,
            end_date=request.end_date
        )
        bond_treasure_issue_cninfo_df = sanitize_data_pandas(bond_treasure_issue_cninfo)

        return bond_treasure_issue_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-债券发行-地方债发行
@router.post("/bond_local_government_issue_cninfo",
             operation_id="post_bond_local_government_issue_cninfo")
async def post_bond_local_government_issue_cninfo(request: TreasureIssueCNInfo):
    """
    债券-债券发行-地方债发行

    接口: bond_local_government_issue_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-债券报表-债券发行-地方债发行
    """
    try:
        bond_local_government_issue_cninfo = ak.bond_local_government_issue_cninfo(
            start_date=request.start_date,
            end_date=request.end_date
        )
        bond_local_government_issue_cninfo_df = sanitize_data_pandas(bond_local_government_issue_cninfo)

        return bond_local_government_issue_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-债券发行-企业债发行
@router.post("/bond_corporate_issue_cninfo",
             operation_id="post_bond_corporate_issue_cninfo")
async def post_bond_corporate_issue_cninfo(request: TreasureIssueCNInfo):
    """
    债券-债券发行-企业债发行

    接口: bond_corporate_issue_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-债券报表-债券发行-企业债发行
    """
    try:
        bond_corporate_issue_cninfo = ak.bond_corporate_issue_cninfo(
            start_date=request.start_date,
            end_date=request.end_date
        )
        bond_corporate_issue_cninfo_df = sanitize_data_pandas(bond_corporate_issue_cninfo)

        return bond_corporate_issue_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-债券发行-可转债发行
@router.post("/bond_cov_issue_cninfo",
             operation_id="post_bond_cov_issue_cninfo")
async def post_bond_cov_issue_cninfo(request: TreasureIssueCNInfo):
    """
    债券-债券发行-可转债发行

    接口: bond_cov_issue_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-债券报表-债券发行-可转债发行
    """
    try:
        bond_cov_issue_cninfo = ak.bond_cov_issue_cninfo(
            start_date=request.start_date,
            end_date=request.end_date
        )
        bond_cov_issue_cninfo_df = sanitize_data_pandas(bond_cov_issue_cninfo)

        return bond_cov_issue_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-债券发行-可转债转股
@router.get("/bond_cov_stock_issue_cninfo", operation_id="get_bond_cov_stock_issue_cninfo")
async def get_bond_cov_stock_issue_cninfo():
    """
    债券-债券发行-可转债转股

    接口: bond_cov_stock_issue_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-债券报表-债券发行-可转债转股
    """
    try:
        bond_cov_stock_issue_cninfo = ak.bond_cov_stock_issue_cninfo()
        bond_cov_stock_issue_cninfo_df = sanitize_data_pandas(bond_cov_stock_issue_cninfo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_cov_stock_issue_cninfo_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)

