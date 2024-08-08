import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 美国-其他-美国EIA原油库存报告
@router.get("/macro_usa_eia_crude_rate",
            operation_id="get_macro_usa_eia_crude_rate")
async def get_macro_usa_eia_crude_rate():
    """
    美国-其他-美国EIA原油库存报告

    接口: macro_usa_eia_crude_rate

    目标地址: https://cdn.jin10.com/dc/reports/dc_usa_michigan_consumer_sentiment_all.js?v=1578576228

    描述: 美国EIA原油库存报告, 数据区间从 19950801-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_eia_crude_rate = ak.macro_usa_eia_crude_rate()
        macro_usa_eia_crude_rate_df = sanitize_data_pandas(macro_usa_eia_crude_rate)
        return macro_usa_eia_crude_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-其他-美国初请失业金人数报告
@router.get("/macro_usa_initial_jobless",
            operation_id="get_macro_usa_initial_jobless")
async def get_macro_usa_initial_jobless():
    """
    美国-其他-美国初请失业金人数报告

    接口: macro_usa_initial_jobless

    目标地址: https://cdn.jin10.com/dc/reports/dc_usa_michigan_consumer_sentiment_all.js?v=1578576228

    描述: 美国初请失业金人数报告, 数据区间从 19700101-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_usa_initial_jobless = ak.macro_usa_initial_jobless()
        macro_usa_initial_jobless_df = sanitize_data_pandas(macro_usa_initial_jobless)
        return macro_usa_initial_jobless_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 美国-其他-美国原油产量报告
@router.get("/macro_usa_crude_inner",
            operation_id="get_macro_usa_crude_inner")
async def get_macro_usa_crude_inner():
    """
    美国-其他-美国原油产量报告

    接口: macro_usa_crude_inner

    目标地址: https://datacenter.jin10.com/reportType/dc_eia_crude_oil_produce

    描述: 美国原油产量报告, 数据区间从 19830107-至今, 每周三公布(美国节假日除外), 美国能源信息署(EIA)

    限量: 单次返回所有历史数据

    (1)报告内容: 美国能源信息署（EIA）在北京时间每周三晚公布EIA报告，除了公布美国原油库存、汽油库存等数据外，报告还包含美国上周国内原油产量的数据。

    (2)报告组成：美国国内原油产量、美国本土48州原油产量和美国阿拉斯加州原油产量。

    (3)数据关系：美国国内原油产量=美国本土48州原油产量+美国阿拉斯加州原油产量 单位均为万桶/日。

    (4)数据解读: 该数据反映了美国原油供应侧的情况，理论而言，当美国国内原油产量录得增加，通常导致油价下跌；当产量减少，则通常导致油价上扬。
    """
    try:
        macro_usa_crude_inner = ak.macro_usa_crude_inner()
        macro_usa_crude_inner_df = sanitize_data_pandas(macro_usa_crude_inner)
        return macro_usa_crude_inner_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
