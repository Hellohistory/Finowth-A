import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 东方财富-行情中心-沪深京板块-概念板块
@router.get("/stock_board_concept_name_em", operation_id="get_stock_board_concept_name_em")
def get_stock_board_concept_name_em():
    """
    东方财富-沪深京板块-概念板块

    接口: stock_board_concept_name_em

    目标地址: https://quote.eastmoney.com/center/boardlist.html#concept_board

    描述: 东方财富-行情中心-沪深京板块-概念板块

    限量: 单次返回当前时刻所有概念板块数据
    """
    try:
        stock_board_concept_name_em = ak.stock_board_concept_name_em()
        stock_board_concept_name_em_df = sanitize_data_pandas(stock_board_concept_name_em)
        return stock_board_concept_name_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DongCaiBankuaiSymbolRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：'车联网'; 可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有行业名称")


# 东方财富-沪深板块-概念板块-板块成份
@router.post("/stock_board_concept_cons_em", operation_id="post_stock_board_concept_cons_em")
async def post_stock_board_concept_cons_em(request: DongCaiBankuaiSymbolRequest):
    """
    东方财富-沪深板块-概念板块-板块成份

    接口: stock_board_concept_cons_em

    目标地址: http://quote.eastmoney.com/center/boardlist.html#boards-BK06551(示例)

    描述: 东方财富-沪深板块-概念板块-板块成份

    限量: 单次返回当前时刻所有成份股
    """
    try:
        stock_board_concept_cons_em = ak.stock_board_concept_cons_em(symbol=request.symbol)
        stock_board_concept_cons_em_df = sanitize_data_pandas(stock_board_concept_cons_em)
        return stock_board_concept_cons_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ConceptHistRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：'网络安全'; 可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有行业名称")
    period: str = Field(..., title="时间周期", description="'daily(天)', 'weekly(周)', 'monthly(月)'")
    start_date: str = Field(..., title="开始查询的日期", description="例：20240701")
    end_date: str = Field(..., title="结束查询的日期", description="例：20240716")
    adjust: str = Field(..., title="复权类型", description="'': 不复权, 默认; 'qfq': 前复权, 'hfq': 后复权")


# 东方财富-沪深板块-概念板块-历史行情数据
@router.post("/stock_board_concept_hist_em", operation_id="post_stock_board_concept_hist_em")
async def post_stock_board_concept_hist_em(request: ConceptHistRequest):
    """
    东方财富-沪深板块-概念板块-历史行情数据

    接口: stock_board_concept_hist_em

    目标地址: http://quote.eastmoney.com/bk/90.BK0715.html(示例)

    描述: 东方财富-沪深板块-概念板块-历史行情数据

    限量: 单次返回指定个股和 adjust 的历史数据
    """
    try:
        stock_board_concept_hist_em = ak.stock_board_concept_hist_em(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date,
            adjust=request.adjust
        )
        stock_board_concept_hist_em_df = sanitize_data_pandas(stock_board_concept_hist_em)
        return stock_board_concept_hist_em_df.to_dict(orient="records")
    except IndexError:
        raise HTTPException(status_code=404, detail="暂无该概念，请通过调用stock_board_concept_name_em接口检索")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ConceptHistMinRequest(BaseModel):
    symbol: str = Field(..., title="概念名称",
                        description="例：长寿药，可以通过调用stock_board_concept_name_em接口查看东方财富-概念板块的所有概念名称")
    period: str = Field(..., title="时间周期",
                        description="可选择1分钟:'1',5分钟:'5',15分钟:'15',30分钟:'30',60分钟:'60'")


# 东方财富-沪深板块-概念板块-分时历史行情数据
@router.post("/stock_board_concept_hist_min_em", operation_id="post_stock_board_concept_hist_min_em")
async def post_stock_board_concept_hist_min_em(request: ConceptHistMinRequest):
    """
    东方财富-沪深板块-概念板块-分时历史行情数据

    接口: stock_board_concept_hist_min_em

    目标地址: http://quote.eastmoney.com/bk/90.BK0715.html

    描述: 东方财富-沪深板块-概念板块-分时历史行情数据

    限量: 单次返回指定个股和时间周期的历史数据
    """
    try:
        stock_board_concept_hist_min_em = ak.stock_board_concept_hist_min_em(
            symbol=request.symbol,
            period=request.period
        )
        stock_board_concept_hist_min_em_df = sanitize_data_pandas(stock_board_concept_hist_min_em)
        return stock_board_concept_hist_min_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
