from datetime import datetime

import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DateRequest(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20230808")


# 东方财富-数据中心-股市日历-公司动态
@router.post("/stock_gsrl_gsdt_em", operation_id="stock_gsrl_gsdt_em")
async def stock_gsrl_gsdt_em(request: DateRequest):
    """
    东方财富-股市日历-公司动态

    接口: stock_gsrl_gsdt_em

    目标地址: https://data.eastmoney.com/gsrl/gsdt.html

    描述: 东方财富-数据中心-股市日历-公司动态

    限量: 单次返回指定交易日的数据
    """
    try:
        stock_gsrl_gsdt_em = ak.stock_gsrl_gsdt_em(date=request.date)
        stock_gsrl_gsdt_em_df = sanitize_data_pandas(stock_gsrl_gsdt_em)
        return stock_gsrl_gsdt_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-行情中心-沪深个股-风险警示板
@router.get("/stock_zh_a_st_em", operation_id="stock_zh_a_st_em")
def stock_zh_a_st_em():
    """
    东方财富-沪深个股-风险警示板

    接口: stock_zh_a_st_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#st_board

    描述: 东方财富-行情中心-沪深个股-风险警示板

    限量: 单次返回当前交易日风险警示板的所有股票的行情数据
    """
    try:
        stock_zh_a_st_em = ak.stock_zh_a_st_em()
        stock_zh_a_st_em_df = sanitize_data_pandas(stock_zh_a_st_em)
        return stock_zh_a_st_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-行情中心-沪深个股-新股
@router.get("/stock_zh_a_new_em", operation_id="stock_zh_a_new_em")
def stock_zh_a_new_em():
    """
    东方财富-沪深个股-新股

    接口: stock_zh_a_new_em

    目标地址: https://quote.eastmoney.com/center/gridlist.html#newshares

    描述: 东方财富-行情中心-沪深个股-新股

    限量: 单次返回当前交易日新股板块的所有股票的行情数据
    """
    try:
        stock_zh_a_new_em = ak.stock_zh_a_new_em()
        stock_zh_a_new_em_df = sanitize_data_pandas(stock_zh_a_new_em)

        current_date = datetime.now().strftime("%Y-%m-%d")
        for record in stock_zh_a_new_em_df:
            temp_record = record.copy()
            record.clear()
            record["序号"] = temp_record["序号"]
            record["日期"] = current_date
            for key, value in temp_record.items():
                if key != "序号":
                    record[key] = value

        return stock_zh_a_new_em_df
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 同花顺-数据中心-新股数据-IPO受益股
@router.get("/stock_ipo_benefit_ths", operation_id="stock_ipo_benefit_ths")
def stock_ipo_benefit_ths():
    """
    同花顺-新股数据-IPO受益股

    接口: stock_ipo_benefit_ths

    目标地址: https://data.10jqka.com.cn/ipo/syg/

    描述: 同花顺-数据中心-新股数据-IPO受益股

    限量: 单次返回当前交易日的所有数据; 该数据每周更新一次, 返回最近一周的数据 ，对于本周没有IPO信息时会返回提示信息
    """
    try:
        result = ak.stock_ipo_benefit_ths()
        if isinstance(result, str) and result == "当前没有数据，请稍后再试。":
            return {"message": result}
        return result.to_dict(orient="records")
    except AttributeError as e:
        if "'NoneType' object has no attribute 'text'" in str(e):
            return {"message": "当前没有数据，请稍后再试。"}
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-行情中心-沪深个股-两网及退市
@router.get("/stock_zh_a_stop_em", operation_id="stock_zh_a_stop_em")
def stock_zh_a_stop_em():
    """
    东方财富-沪深个股-两网及退市

    接口: stock_zh_a_stop_em

    目标地址: http://quote.eastmoney.com/center/gridlist.html#staq_net_board

    描述: 东方财富-行情中心-沪深个股-两网及退市

    限量: 单次返回当前交易日两网及退市的所有股票的行情数据
    """
    try:
        stock_zh_a_stop_em = ak.stock_zh_a_stop_em()
        stock_zh_a_stop_em_df = sanitize_data_pandas(stock_zh_a_stop_em)

        current_date = datetime.now().strftime("%Y-%m-%d")

        for record in stock_zh_a_stop_em_df:
            temp_record = record.copy()
            record.clear()
            for key, value in temp_record.items():
                record[key] = value
                if key == "序号":
                    record["日期"] = current_date

        return stock_zh_a_stop_em_df
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
