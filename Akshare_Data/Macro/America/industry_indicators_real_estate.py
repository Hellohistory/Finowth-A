import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-产业指标-房地产-美国NAHB房产市场指数报告
@router.get("/macro_usa_nahb_house_market_index",
            operation_id="macro_usa_nahb_house_market_index")
async def macro_usa_nahb_house_market_index():
    """
    美国-产业指标-房地产-美国NAHB房产市场指数报告

    接口: macro_usa_nahb_house_market_index

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_nahb_house_market_index

    描述: 美国 NAHB 房产市场指数报告, 数据区间从 19850201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_nahb_house_market_index = ak.macro_usa_nahb_house_market_index()
        macro_usa_nahb_house_market_index_df = sanitize_data_pandas(macro_usa_nahb_house_market_index)
        return macro_usa_nahb_house_market_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国新屋开工总数年化报告
@router.get("/macro_usa_house_starts",
            operation_id="macro_usa_house_starts")
async def macro_usa_house_starts():
    """
    美国-产业指标-房地产-美国新屋开工总数年化报告

    接口: macro_usa_house_starts

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_house_starts

    描述: 美国新屋开工总数年化报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_house_starts = ak.macro_usa_house_starts()
        macro_usa_house_starts_df = sanitize_data_pandas(macro_usa_house_starts)
        return macro_usa_house_starts_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国新屋销售总数年化报告
@router.get("/macro_usa_new_home_sales",
            operation_id="macro_usa_new_home_sales")
async def macro_usa_new_home_sales():
    """
    美国-产业指标-房地产-美国新屋销售总数年化报告

    接口: macro_usa_new_home_sales

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_new_home_sales

    描述: 美国新屋销售总数年化报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_new_home_sales = ak.macro_usa_new_home_sales()
        macro_usa_new_home_sales_df = sanitize_data_pandas(macro_usa_new_home_sales)
        return macro_usa_new_home_sales_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国营建许可总数报告
@router.get("/macro_usa_building_permits",
            operation_id="macro_usa_building_permits")
async def macro_usa_building_permits():
    """
    美国-产业指标-房地产-美国营建许可总数报告

    接口: macro_usa_building_permits

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_building_permits

    描述: 美国营建许可总数报告, 数据区间从 20080220-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_building_permits = ak.macro_usa_building_permits()
        macro_usa_building_permits_df = sanitize_data_pandas(macro_usa_building_permits)
        return macro_usa_building_permits_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国成屋销售总数年化报告
@router.get("/macro_usa_exist_home_sales",
            operation_id="macro_usa_exist_home_sales")
async def macro_usa_exist_home_sales():
    """
    美国-产业指标-房地产-美国成屋销售总数年化报告

    接口: macro_usa_exist_home_sales

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_exist_home_sales

    描述: 美国成屋销售总数年化报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_exist_home_sales = ak.macro_usa_exist_home_sales()
        macro_usa_exist_home_sales_df = sanitize_data_pandas(macro_usa_exist_home_sales)
        return macro_usa_exist_home_sales_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国FHFA房价指数月率报告
@router.get("/macro_usa_house_price_index",
            operation_id="macro_usa_house_price_index")
async def macro_usa_house_price_index():
    """
    美国-产业指标-房地产-美国FHFA房价指数月率报告

    接口: macro_usa_house_price_index

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_house_price_index

    描述: 美国 FHFA 房价指数月率报告, 数据区间从 19910301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_house_price_index = ak.macro_usa_house_price_index()
        macro_usa_house_price_index_df = sanitize_data_pandas(macro_usa_house_price_index)
        return macro_usa_house_price_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国S&P/CS20座大城市房价指数年率报告
@router.get("/macro_usa_spcs20",
            operation_id="macro_usa_spcs20")
async def macro_usa_spcs20():
    """
    美国-产业指标-房地产-美国S&P/CS20座大城市房价指数年率报告

    接口: macro_usa_spcs20

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_spcs20

    描述: 美国S&P/CS20座大城市房价指数年率报告, 数据区间从 20010201-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_spcs20 = ak.macro_usa_spcs20()
        macro_usa_spcs20_df = sanitize_data_pandas(macro_usa_spcs20)
        return macro_usa_spcs20_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-产业指标-房地产-美国成屋签约销售指数月率报告
@router.get("/macro_usa_pending_home_sales",
            operation_id="macro_usa_pending_home_sales")
async def macro_usa_pending_home_sales():
    """
    美国-产业指标-房地产-美国成屋签约销售指数月率报告

    接口: macro_usa_pending_home_sales

    目标地址: https://datacenter.jin10.com/reportType/dc_usa_pending_home_sales

    描述: 美国成屋签约销售指数月率报告, 数据区间从 20010301-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_pending_home_sales = ak.macro_usa_pending_home_sales()
        macro_usa_pending_home_sales_df = sanitize_data_pandas(macro_usa_pending_home_sales)
        return macro_usa_pending_home_sales_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
