import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class CarMarketTotalCpca(BaseModel):
    symbol: str = Field(..., title="车辆类型",
                        description="可选择 狭义乘用车 , 广义乘用车 ")
    indicator: str = Field(..., title="销售类型",
                           description="可选择 产量 , 批发 , 零售 , 出口 ")


# 另类数据-汽车销量排行-乘联会-统计数据-总体市场
@router.post("/car_market_total_cpca",
             operation_id="car_market_total_cpca")
def car_market_total_cpca(request: CarMarketTotalCpca):
    """
    另类数据-汽车销量排行-乘联会-统计数据-总体市场

    接口: car_market_total_cpca

    目标地址: http://data.cpcaauto.com/TotalMarket

    描述: 乘联会-统计数据-总体市场

    限量: 单次返回指定车辆类型和销售类型的数据
    """
    try:
        car_market_total_cpca = ak.car_market_total_cpca(
            symbol=request.symbol,
            indicator=request.indicator
        )
        car_market_total_cpca_df = sanitize_data_pandas(car_market_total_cpca)

        return car_market_total_cpca_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-汽车销量排行-乘联会-统计数据-总体市场
@router.post("/car_market_man_rank_cpca",
             operation_id="car_market_man_rank_cpca")
def car_market_man_rank_cpca(request: CarMarketTotalCpca):
    """
    另类数据-汽车销量排行-乘联会-统计数据-总体市场

    接口: car_market_man_rank_cpca

    目标地址: http://data.cpcaauto.com/ManRank

    描述: 乘联会-统计数据-厂商排名

    限量: 单次返回指定车辆类型和销售类型的数据
    """
    try:
        car_market_man_rank_cpca = ak.car_market_man_rank_cpca(
            symbol=request.symbol,
            indicator=request.indicator
        )
        car_market_man_rank_cpca_df = sanitize_data_pandas(car_market_man_rank_cpca)

        return car_market_man_rank_cpca_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class CarMarketCateCpca(BaseModel):
    symbol: str = Field(..., title="车辆类型", description="可选择 轿车, MPV , SUV , 占比 ")
    indicator: str = Field(..., title="销售类型", description="可选择 批发 , 零售 ")


# 另类数据-汽车销量排行-乘联会-统计数据-总体市场
@router.post("/car_market_cate_cpca",
             operation_id="car_market_cate_cpca")
def car_market_cate_cpca(request: CarMarketCateCpca):
    """
    另类数据-汽车销量排行-乘联会-统计数据-车型大类

    接口: car_market_cate_cpca

    目标地址: http://data.cpcaauto.com/CategoryMarket

    描述: 乘联会-统计数据-车型大类

    限量: 单次返回指定 symbol 和 indicator 的数据
    """
    try:
        car_market_cate_cpca = ak.car_market_cate_cpca(
            symbol=request.symbol,
            indicator=request.indicator
        )
        car_market_cate_cpca_df = sanitize_data_pandas(car_market_cate_cpca)

        return car_market_cate_cpca_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-汽车销量排行-乘联会-统计数据-国别细分市场
@router.get("/car_market_country_cpca", operation_id="car_market_country_cpca")
def car_market_country_cpca():
    """
    另类数据-汽车销量排行-乘联会-统计数据-国别细分市场

    接口: car_market_country_cpca

    目标地址: http://data.cpcaauto.com/CountryMarket

    描述: 乘联会-统计数据-国别细分市场

    限量: 单次返回指定 symbol 和 indicator 的数据
    """
    try:
        car_market_country_cpca = ak.car_market_country_cpca()
        car_market_country_cpca_df = sanitize_data_pandas(car_market_country_cpca)
        return car_market_country_cpca_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class CarMarketCateCpca(BaseModel):
    symbol: str = Field(..., title="车辆类型", description="可选择 轿车, MPV , SUV ")


# 另类数据-汽车销量排行-乘联会-统计数据-级别细分市场
@router.post("/car_market_segment_cpca",
             operation_id="car_market_segment_cpca")
def car_market_segment_cpca(request: CarMarketCateCpca):
    """
    另类数据-汽车销量排行-乘联会-统计数据-级别细分市场

    接口: car_market_segment_cpca

    目标地址: http://data.cpcaauto.com/SegmentMarket

    描述: 乘联会-统计数据-级别细分市场

    限量: 单次返回指定车辆类型的数据
    """
    try:
        car_market_segment_cpca = ak.car_market_segment_cpca(
            symbol=request.symbol
        )
        car_market_segment_cpca_df = sanitize_data_pandas(car_market_segment_cpca)

        return car_market_segment_cpca_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class CarMarketFuelCpca(BaseModel):
    symbol: str = Field(..., title="指定类型", description="可选择 整体市场, 销量占比-PHEV-BEV, 销量占比-ICE-NEV")


# 另类数据-汽车销量排行-乘联会-统计数据-新能源细分市场
@router.post("/car_market_fuel_cpca",
             operation_id="car_market_fuel_cpca")
def car_market_fuel_cpca(request: CarMarketFuelCpca):
    """
    另类数据-汽车销量排行-乘联会-统计数据-新能源细分市场

    接口: car_market_fuel_cpca

    目标地址: http://data.cpcaauto.com/FuelMarket

    描述: 乘联会-统计数据-车型大类

    限量: 单次返回指定 symbol 的数据
    """
    try:
        car_market_fuel_cpca = ak.car_market_fuel_cpca(
            symbol=request.symbol
        )
        car_market_fuel_cpca_df = sanitize_data_pandas(car_market_fuel_cpca)

        return car_market_fuel_cpca_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class CarSaleRankGasgoo(BaseModel):
    symbol: str = Field(..., title="指定类型", description="可选择 车企榜, 品牌榜 , 车型榜 ")
    date: str = Field(..., title="指定年月", description="例：202104")


# 另类数据-汽车销量排行-盖世研究院
@router.post("/car_sale_rank_gasgoo",
             operation_id="car_sale_rank_gasgoo")
def car_sale_rank_gasgoo(request: CarSaleRankGasgoo):
    """
    另类数据-汽车销量排行-盖世研究院

    接口: car_sale_rank_gasgoo

    目标地址: https://i.gasgoo.com/data/ranking

    描述: 盖世汽车资讯的汽车销量排行榜数据

    限量: 单次返回指定类型和年月的汽车销量排行榜数据
    """
    try:
        car_sale_rank_gasgoo = ak.car_sale_rank_gasgoo(
            symbol=request.symbol,
            date=request.date
        )
        car_sale_rank_gasgoo_df = sanitize_data_pandas(car_sale_rank_gasgoo)

        return car_sale_rank_gasgoo_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
