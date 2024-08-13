import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class SpotPriceSymbolRequest(BaseModel):
    symbol: str = Field(..., title="品种类型",
                        description="例：螺纹钢，可通过spot_price_table_qh获取")


# 99 期货-数据-期现-现货走势
@router.post("/spot_price_qh", operation_id="spot_price_qh")
async def spot_price_qh(request: SpotPriceSymbolRequest):
    """
    接口: spot_price_qh

    目标地址: https://www.99qh.com/data/spotTrend

    描述: 99 期货-数据-期现-现货走势

    限量: 单次返回指定品种的所有历史数据
    """
    try:
        spot_price_qh = ak.spot_price_qh(symbol=request.symbol)
        spot_price_qh_df = sanitize_data_pandas(spot_price_qh)

        return spot_price_qh_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class SpotHistSymbolRequest(BaseModel):
    symbol: str = Field(..., title="品种代码",
                        description="例：Au99.99，可通过spot_symbol_table_sge获取")


# 上海黄金交易所-行情走势-历史数据
@router.post("/spot_hist_sge", operation_id="spot_hist_sge")
async def spot_hist_sge(request: SpotPriceSymbolRequest):
    """
    接口: spot_hist_sge

    目标地址: https://www.sge.com.cn/sjzx/mrhq

    描述: 上海黄金交易所-数据资讯-行情走势-历史数据

    限量: 单次返回指定品种的所有历史数据
    """
    try:
        spot_hist_sge = ak.spot_hist_sge(symbol=request.symbol)
        spot_hist_sge_df = sanitize_data_pandas(spot_hist_sge)

        return spot_hist_sge_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 上海黄金交易所-上海金基准价-历史数据
@router.get("/spot_golden_benchmark_sge", operation_id="spot_golden_benchmark_sge")
async def spot_golden_benchmark_sge():
    """
    上海黄金交易所-上海金基准价-历史数据

    接口: spot_golden_benchmark_sge

    目标地址: https://www.sge.com.cn/sjzx/jzj

    描述: 上海黄金交易所-数据资讯-上海金基准价-历史数据

    限量: 单次返回所有历史数据
    """
    try:
        spot_golden_benchmark_sge = ak.spot_golden_benchmark_sge()
        spot_golden_benchmark_sge_df = sanitize_data_pandas(spot_golden_benchmark_sge)
        return spot_golden_benchmark_sge_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 上海黄金交易所-上海银基准价-历史数据
@router.get("/spot_silver_benchmark_sge", operation_id="spot_silver_benchmark_sge")
async def spot_silver_benchmark_sge():
    """
    上海黄金交易所-上海银基准价-历史数据

    接口: spot_silver_benchmark_sge

    目标地址: https://www.sge.com.cn/sjzx/shyjzj

    描述: 上海黄金交易所-数据资讯-上海银基准价-历史数据

    限量: 单次返回所有历史数据
    """
    try:
        spot_silver_benchmark_sge = ak.spot_silver_benchmark_sge()
        spot_silver_benchmark_sge_df = sanitize_data_pandas(spot_silver_benchmark_sge)
        return spot_silver_benchmark_sge_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-全国瘦肉型肉猪
@router.get("/spot_hog_lean_price_soozhu", operation_id="spot_hog_lean_price_soozhu")
async def spot_hog_lean_price_soozhu():
    """
    搜猪-生猪大数据-全国瘦肉型肉猪

    接口: spot_hog_lean_price_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-全国瘦肉型肉猪

    限量: 单次返回近半个月的历史数据
    """
    try:
        spot_hog_lean_price_soozhu = ak.spot_hog_lean_price_soozhu()
        spot_hog_lean_price_soozhu_df = sanitize_data_pandas(spot_hog_lean_price_soozhu)
        return spot_hog_lean_price_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-今年以来全国出栏均价走势
@router.get("/spot_hog_year_trend_soozhu", operation_id="spot_hog_year_trend_soozhu")
async def spot_hog_year_trend_soozhu():
    """
    搜猪-生猪大数据-今年以来全国出栏均价走势

    接口: spot_hog_year_trend_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-今年以来全国出栏均价走势

    限量: 单次返回近一年所有历史数据
    """
    try:
        spot_hog_year_trend_soozhu = ak.spot_hog_year_trend_soozhu()
        spot_hog_year_trend_soozhu_df = sanitize_data_pandas(spot_hog_year_trend_soozhu)
        return spot_hog_year_trend_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-各省均价实时排行榜
@router.get("/spot_hog_soozhu", operation_id="spot_hog_soozhu")
async def spot_hog_soozhu():
    """
    搜猪-生猪大数据-各省均价实时排行榜

    接口: spot_hog_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-各省均价实时排行榜

    限量: 单次返回所有实时数据
    """
    try:
        spot_hog_soozhu = ak.spot_hog_soozhu()
        spot_hog_soozhu_df = sanitize_data_pandas(spot_hog_soozhu)
        return spot_hog_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-全国三元仔猪
@router.get("/spot_hog_three_way_soozhu", operation_id="spot_hog_three_way_soozhu")
async def spot_hog_three_way_soozhu():
    """
    搜猪-生猪大数据-全国三元仔猪

    接口: spot_hog_lean_price_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-全国三元仔猪

    限量: 单次返回近半个月的历史数据
    """
    try:
        spot_hog_three_way_soozhu = ak.spot_hog_three_way_soozhu()
        spot_hog_three_way_soozhu_df = sanitize_data_pandas(spot_hog_three_way_soozhu)
        return spot_hog_three_way_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-全国三元仔猪
@router.get("/spot_hog_crossbred_soozhu", operation_id="spot_hog_crossbred_soozhu")
async def spot_hog_crossbred_soozhu():
    """
    搜猪-生猪大数据-全国后备二元母猪

    接口: spot_hog_crossbred_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-全国后备二元母猪

    限量: 单次返回近半个月的历史数据
    """
    try:
        spot_hog_crossbred_soozhu = ak.spot_hog_crossbred_soozhu()
        spot_hog_crossbred_soozhu_df = sanitize_data_pandas(spot_hog_crossbred_soozhu)
        return spot_hog_crossbred_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-全国豆粕价格走势
@router.get("/spot_soybean_price_soozhu", operation_id="spot_soybean_price_soozhu")
async def spot_soybean_price_soozhu():
    """
    搜猪-生猪大数据-全国豆粕价格走势

    接口: spot_soybean_price_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-全国豆粕价格走势

    限量: 单次返回近半个月的历史数据
    """
    try:
        spot_soybean_price_soozhu = ak.spot_soybean_price_soozhu()
        spot_soybean_price_soozhu_df = sanitize_data_pandas(spot_soybean_price_soozhu)
        return spot_soybean_price_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 搜猪-生猪大数据-全国育肥猪合料（含自配料）半月走势
@router.get("/spot_mixed_feed_soozhu", operation_id="spot_mixed_feed_soozhu")
async def spot_mixed_feed_soozhu():
    """
    搜猪-生猪大数据-全国育肥猪合料（含自配料）半月走势

    接口: spot_mixed_feed_soozhu

    目标地址: https://www.soozhu.com/price/data/center/

    描述: 搜猪-生猪大数据-全国育肥猪合料（含自配料）半月走势

    限量: 单次返回近半个月的历史数据
    """
    try:
        spot_mixed_feed_soozhu = ak.spot_mixed_feed_soozhu()
        spot_mixed_feed_soozhu_df = sanitize_data_pandas(spot_mixed_feed_soozhu)
        return spot_mixed_feed_soozhu_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
