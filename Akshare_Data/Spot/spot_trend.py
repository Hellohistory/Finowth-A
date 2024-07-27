import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()


class SpotPriceSymbolRequest(BaseModel):
    symbol: str = Field(..., title="品种类型",
                        description="例：螺纹钢，可通过spot_price_table_qh获取")


# 99 期货-数据-期现-现货走势
@router.post("/spot_price_qh", operation_id="post_spot_price_qh")
async def post_spot_price_qh(request: SpotPriceSymbolRequest):
    """
    接口: spot_price_qh

    目标地址: https://www.99qh.com/data/spotTrend

    描述: 99 期货-数据-期现-现货走势

    限量: 单次返回指定品种的所有历史数据
    """
    try:
        spot_price_qh_df = ak.spot_price_qh(symbol=request.symbol)
        return spot_price_qh_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SpotHistSymbolRequest(BaseModel):
    symbol: str = Field(..., title="品种代码",
                        description="例：Au99.99，可通过spot_symbol_table_sge获取")


# 上海黄金交易所-行情走势-历史数据
@router.post("/spot_hist_sge", operation_id="post_spot_hist_sge")
async def post_spot_hist_sge(request: SpotPriceSymbolRequest):
    """
    接口: spot_hist_sge

    目标地址: https://www.sge.com.cn/sjzx/mrhq

    描述: 上海黄金交易所-数据资讯-行情走势-历史数据

    限量: 单次返回指定品种的所有历史数据
    """
    try:
        spot_hist_sge_df = ak.spot_hist_sge(symbol=request.symbol)
        return spot_hist_sge_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 上海黄金交易所-上海金基准价-历史数据
@router.get("/spot_golden_benchmark_sge", operation_id="get_spot_golden_benchmark_sge")
async def get_spot_golden_benchmark_sge():
    """
    上海黄金交易所-上海金基准价-历史数据

    接口: spot_golden_benchmark_sge

    目标地址: https://www.sge.com.cn/sjzx/jzj

    描述: 上海黄金交易所-数据资讯-上海金基准价-历史数据

    限量: 单次返回所有历史数据
    """
    try:
        spot_golden_benchmark_sge = ak.spot_golden_benchmark_sge()
        data = spot_golden_benchmark_sge.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return data


# 上海黄金交易所-上海银基准价-历史数据
@router.get("/spot_silver_benchmark_sge", operation_id="get_spot_silver_benchmark_sge")
async def get_spot_silver_benchmark_sge():
    """
    上海黄金交易所-上海银基准价-历史数据

    接口: spot_silver_benchmark_sge

    目标地址: https://www.sge.com.cn/sjzx/shyjzj

    描述: 上海黄金交易所-数据资讯-上海银基准价-历史数据

    限量: 单次返回所有历史数据
    """
    try:
        spot_silver_benchmark_sge = ak.spot_silver_benchmark_sge()
        data = spot_silver_benchmark_sge.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return data
