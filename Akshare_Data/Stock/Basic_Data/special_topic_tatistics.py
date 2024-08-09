import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class JuChaoSymbolDateRangeRequest(BaseModel):
    symbol: str = Field(..., title="指定获取类型", description="可选择'全部', '深市主板', '沪市', '创业板', '科创板'")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")


# 巨潮资讯-数据中心-专题统计-公司治理-对外担保
@router.post("/stock_cg_guarantee_cninfo", operation_id="stock_cg_guarantee_cninfo")
async def stock_cg_guarantee_cninfo(request: JuChaoSymbolDateRangeRequest):
    """
    巨潮资讯-公司治理-对外担保

    接口: stock_cg_guarantee_cninfo

    目标地址: https://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-公司治理-对外担保

    限量: 单次指定个股和起始日期的对外担保数据
    """
    try:
        stock_corporate_governance_guarantee = ak.stock_cg_guarantee_cninfo(
            symbol=request.symbol, start_date=request.start_date, end_date=request.end_date
        )
        stock_corporate_governance_guarantee_df = sanitize_data_pandas(stock_corporate_governance_guarantee)
        return stock_corporate_governance_guarantee_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 巨潮资讯-数据中心-专题统计-公司治理-公司诉讼
@router.post("/stock_cg_lawsuit_cninfo", operation_id="stock_cg_lawsuit_cninfo")
async def stock_cg_lawsuit_cninfo(request: JuChaoSymbolDateRangeRequest):
    """
    巨潮资讯-公司治理-公司诉讼

    接口: stock_cg_lawsuit_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-公司治理-公司诉讼

    限量: 单次指定个股和起始日期的公司诉讼数据
    """
    try:
        stock_cg_lawsuit_cninfo = ak.stock_cg_lawsuit_cninfo(
            symbol=request.symbol, start_date=request.start_date, end_date=request.end_date
        )
        stock_cg_lawsuit_cninfo_df = sanitize_data_pandas(stock_cg_lawsuit_cninfo)
        return stock_cg_lawsuit_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoDateRequest(BaseModel):
    date: str = Field(..., title="指定时间", description="例：20210930")


# 巨潮资讯-数据中心-专题统计-公司治理-股权质押
@router.post("/stock_cg_equity_mortgage_cninfo", operation_id="stock_cg_equity_mortgage_cninfo")
async def stock_cg_equity_mortgage_cninfo(request: JuChaoDateRequest):
    """
    巨潮资讯-公司治理-股权质押

    接口: stock_cg_equity_mortgage_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-公司治理-股权质押

    限量: 单次指定时间的股权质押数据
    """
    try:
        stock_cg_equity_mortgage_cninfo = ak.stock_cg_equity_mortgage_cninfo(date=request.date)
        stock_cg_equity_mortgage_cninfo_df = sanitize_data_pandas(stock_cg_equity_mortgage_cninfo)
        return stock_cg_equity_mortgage_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiTeSeDateRequest(BaseModel):
    date: str = Field(..., title="输入需要查询月份的最后一天的日期", description="例：20200430")


# 东方财富-数据中心-特色数据-券商业绩月报
@router.post("/stock_qsjy_em", operation_id="stock_qsjy_em")
async def stock_qsjy_em(request: DongCaiTeSeDateRequest):
    """
    东方财富-券商业绩月报

    接口: stock_qsjy_em

    目标地址: http://data.eastmoney.com/other/qsjy.html

    描述: 东方财富-数据中心-特色数据-券商业绩月报

    限量: 单次获取所有数据, 数据从 201006-202007, 月频率
    """
    try:
        stock_qsjy_em = ak.stock_qsjy_em(date=request.date)
        stock_qsjy_em_df = sanitize_data_pandas(stock_qsjy_em)
        return stock_qsjy_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class JuChaoSymbolRequest(BaseModel):
    symbol: str = Field(..., title="指定获取类型",
                        description="数据从2010开始，可选择 单独控制 , 实际控制人 , 一致行动人 , 家族控制 , 全部 ")


# 巨潮资讯-数据中心-专题统计-股东股本-实际控制人持股变动
@router.post("/stock_hold_control_cninfo", operation_id="stock_hold_control_cninfo")
async def stock_hold_control_cninfo(request: JuChaoSymbolRequest):
    """
    巨潮资讯-股东股本-实际控制人持股变动

    接口: stock_hold_control_cninfo

    目标地址: http://webapi.cninfo.com.cn/#/thematicStatistics

    描述: 巨潮资讯-数据中心-专题统计-股东股本-实际控制人持股变动

    限量: 单次指定个股的实际控制人持股变动数据, 从 2010 开始
    """
    try:
        stock_hold_control_cninfo = ak.stock_hold_control_cninfo(symbol=request.symbol)
        stock_hold_control_cninfo_df = sanitize_data_pandas(stock_hold_control_cninfo)
        return stock_hold_control_cninfo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
