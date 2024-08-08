import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 国民经济运行状况-金融报告-深圳融资融券报告
@router.get("/macro_china_market_margin_sz",
            operation_id="get_macro_china_market_margin_sz")
async def get_macro_china_market_margin_sz():
    """
    国民经济运行状况-融资融券报告-深圳融资融券报告

    接口: macro_china_market_margin_sz

    目标地址: https://datacenter.jin10.com/reportType/dc_market_margin_sz

    描述: 深圳融资融券报告, 数据区间从 20100331-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_market_margin_sz = ak.macro_china_market_margin_sz()
        macro_china_market_margin_sz_df = sanitize_data_pandas(macro_china_market_margin_sz)
        return macro_china_market_margin_sz_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融报告-上海融资融券报告
@router.get("/macro_china_market_margin_sh",
            operation_id="get_macro_china_market_margin_sh")
async def get_macro_china_market_margin_sh():
    """
    国民经济运行状况-融资融券报告-上海融资融券报告

    接口: macro_china_market_margin_sh

    目标地址: https://datacenter.jin10.com/reportType/dc_market_margin_sse

    描述: 上海融资融券报告, 数据区间从 20100331-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_market_margin_sh = ak.macro_china_market_margin_sh()
        macro_china_market_margin_sh_df = sanitize_data_pandas(macro_china_market_margin_sh)
        return macro_china_market_margin_sh_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 国民经济运行状况-金融报告-上海黄金交易所报告
@router.get("/macro_china_au_report",
            operation_id="get_macro_china_au_report")
async def get_macro_china_au_report():
    """
    国民经济运行状况-融资融券报告-上海黄金交易所报告

    接口: macro_china_market_margin_sh

    目标地址: https://datacenter.jin10.com/reportType/dc_market_margin_sse

    描述: 上海融资融券报告, 数据区间从 20100331-至今

    限量: 单次返回所有历史数据
    """
    try:
        macro_china_au_report = ak.macro_china_au_report()
        macro_china_au_report_df = sanitize_data_pandas(macro_china_au_report)
        return macro_china_au_report_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
