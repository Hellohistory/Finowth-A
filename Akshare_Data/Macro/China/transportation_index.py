import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-经济状况-民航客座率及载运率
@router.get("/macro_china_passenger_load_factor",
            operation_id="get_macro_china_passenger_load_factor")
async def get_macro_china_passenger_load_factor():
    """
    国民经济运行状况-经济状况-民航客座率及载运率

    接口: macro_china_passenger_load_factor

    目标地址: http://finance.sina.com.cn/mac/#industry-20-0-31-1

    描述: 国家统计局-民航客座率及载运率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_passenger_load_factor = ak.macro_china_passenger_load_factor()
        macro_china_passenger_load_factor_df = sanitize_data_pandas(macro_china_passenger_load_factor)
        return macro_china_passenger_load_factor_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-经济状况-航贸运价指数
@router.get("/macro_china_freight_index",
            operation_id="get_macro_china_freight_index")
async def get_macro_china_freight_index():
    """
    国民经济运行状况-经济状况-航贸运价指数

    接口: macro_china_freight_index

    目标地址: http://finance.sina.com.cn/mac/#industry-22-0-31-2

    描述: 新浪财经-中国宏观经济数据-航贸运价指数

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_freight_index = ak.macro_china_freight_index()
        macro_china_freight_index_df = sanitize_data_pandas(macro_china_freight_index)
        return macro_china_freight_index_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
