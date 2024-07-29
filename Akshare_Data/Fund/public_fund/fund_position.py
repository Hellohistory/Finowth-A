import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 公募基金数据-乐咕乐股-基金仓位-股票型基金仓位
@router.get("/fund_stock_position_lg",
            operation_id="get_fund_stock_position_lg")
async def get_fund_stock_position_lg():
    """
    公募基金数据-乐咕乐股-基金仓位-股票型基金仓位

    接口: fund_stock_position_lg

    目标地址: https://legulegu.com/stockdata/fund-position/pos-stock

    描述: 乐咕乐股-基金仓位-股票型基金仓位

    限量: 返回所有历史数据
    """
    try:
        fund_scale_change_em = ak.fund_scale_change_em()
        fund_scale_change_em_df = sanitize_data_pandas(fund_scale_change_em)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_scale_change_em_df.to_dict(orient="records")


# 公募基金数据-乐咕乐股-基金仓位-平衡混合型基金仓位
@router.get("/fund_balance_position_lg",
            operation_id="get_fund_balance_position_lg")
async def get_fund_balance_position_lg():
    """
    公募基金数据-乐咕乐股-基金仓位-平衡混合型基金仓位

    接口: fund_balance_position_lg

    目标地址: https://legulegu.com/stockdata/fund-position/pos-pingheng

    描述: 乐咕乐股-基金仓位-平衡混合型基金仓位

    限量: 返回所有历史数据
    """
    try:
        fund_balance_position_lg = ak.fund_balance_position_lg()
        fund_balance_position_lg_df = sanitize_data_pandas(fund_balance_position_lg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_balance_position_lg_df.to_dict(orient="records")


# 公募基金数据-乐咕乐股-基金仓位-灵活配置型基金仓位
@router.get("/fund_linghuo_position_lg",
            operation_id="get_fund_linghuo_position_lg")
async def get_fund_linghuo_position_lg():
    """
    公募基金数据-乐咕乐股-基金仓位-灵活配置型基金仓位

    接口: fund_linghuo_position_lg

    目标地址: https://legulegu.com/stockdata/fund-position/pos-linghuo

    描述: 乐咕乐股-基金仓位-灵活配置型基金仓位

    限量: 返回所有历史数据
    """
    try:
        fund_linghuo_position_lg = ak.fund_linghuo_position_lg()
        fund_linghuo_position_lg_df = sanitize_data_pandas(fund_linghuo_position_lg)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return fund_linghuo_position_lg_df.to_dict(orient="records")
