import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 中国香港-其他指数-失业率
@router.get("/macro_china_hk_rate_of_unemployment",
            operation_id="macro_china_hk_rate_of_unemployment")
async def macro_china_hk_rate_of_unemployment():
    """
    中国香港-其他指数-失业率

    接口: macro_china_hk_rate_of_unemployment

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_2.html

    描述: 东方财富-经济数据一览-中国香港-失业率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_rate_of_unemployment = ak.macro_china_hk_rate_of_unemployment()
        macro_china_hk_rate_of_unemployment_df = sanitize_data_pandas(macro_china_hk_rate_of_unemployment)
        return macro_china_hk_rate_of_unemployment_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 中国香港-其他指数-香港商品贸易差额年率
@router.get("/macro_china_hk_trade_diff_ratio",
            operation_id="macro_china_hk_trade_diff_ratio")
async def macro_china_hk_trade_diff_ratio():
    """
    中国香港-其他指数-香港商品贸易差额年率

    接口: macro_china_hk_trade_diff_ratio

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_7.html

    描述: 东方财富-经济数据一览-中国香港-香港商品贸易差额年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_trade_diff_ratio = ak.macro_china_hk_trade_diff_ratio()
        macro_china_hk_trade_diff_ratio_df = sanitize_data_pandas(macro_china_hk_trade_diff_ratio)
        return macro_china_hk_trade_diff_ratio_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 中国香港-其他指数-香港制造业 PPI 年率
@router.get("/macro_china_hk_ppi",
            operation_id="macro_china_hk_ppi")
async def macro_china_hk_ppi():
    """
    中国香港-其他指数-香港制造业 PPI 年率

    接口: macro_china_hk_trade_diff_ratio

    目标地址: https://data.eastmoney.com/cjsj/foreign_8_7.html

    描述: 东方财富-经济数据一览-中国香港-香港商品贸易差额年率

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_hk_ppi = ak.macro_china_hk_ppi()
        macro_china_hk_ppi_df = sanitize_data_pandas(macro_china_hk_ppi)
        return macro_china_hk_ppi_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
