import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FundReportStockCninfo(BaseModel):
    date: str = Field(..., title="指定日期",
                      description="例：20210630，可选择：XXXX0331, XXXX0630, XXXX0930, XXXX1231")


# 公募基金数据-巨潮资讯-基金报告-基金重仓股
@router.post("/fund_report_stock_cninfo",
             operation_id="post_fund_report_stock_cninfo")
def post_fund_report_stock_cninfo(request: FundReportStockCninfo):
    """
    公募基金数据-巨潮资讯-基金报告-基金重仓股

    接口: fund_report_stock_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-基金报表-基金重仓股

    限量: 返回指定日期的所有数据; 数据从 2017 年开始
    """
    try:
        fund_report_stock_cninfo = ak.fund_report_stock_cninfo(date=request.date)
        fund_report_stock_cninfo_df = sanitize_data_pandas(fund_report_stock_cninfo)

        return fund_report_stock_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-巨潮资讯-基金报告-基金行业配置
@router.post("/fund_report_industry_allocation_cninfo",
             operation_id="post_fund_report_industry_allocation_cninfo")
def post_fund_report_industry_allocation_cninfo(request: FundReportStockCninfo):
    """
    公募基金数据-巨潮资讯-基金报告-基金行业配置

    接口: fund_report_industry_allocation_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-基金报表-基金行业配置

    限量: 返回指定日期的所有数据; 数据从 2017 年开始
    """
    try:
        fund_report_industry_allocation_cninfo = ak.fund_report_industry_allocation_cninfo(
            date=request.date
        )
        fund_report_industry_allocation_cninfo_df = sanitize_data_pandas(fund_report_industry_allocation_cninfo)

        return fund_report_industry_allocation_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 公募基金数据-巨潮资讯-基金报告-基金资产配置
@router.get("/fund_report_asset_allocation_cninfo",
            operation_id="get_fund_report_asset_allocation_cninfo")
async def get_fund_report_asset_allocation_cninfo():
    """
    公募基金数据-巨潮资讯-基金报告-基金资产配置

    接口: fund_report_asset_allocation_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-基金报表-基金资产配置

    限量: 返回所有基金资产配置数据
    """
    try:
        fund_report_asset_allocation_cninfo = ak.fund_report_asset_allocation_cninfo()
        fund_report_asset_allocation_cninfo_df = sanitize_data_pandas(fund_report_asset_allocation_cninfo)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_report_asset_allocation_cninfo_df.to_dict(orient="records")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
