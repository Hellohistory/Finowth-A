import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class DateRequest(BaseModel):
    date: str = Field(..., title="开始查询的时间", description="例：20230808")


# 东方财富-数据中心-特色数据-机构调研-机构调研统计
@router.post("/stock_jgdy_tj_em", operation_id="stock_jgdy_tj_em")
async def stock_jgdy_tj_em(request: DateRequest):
    """
    东方财富-机构调研-机构调研统计

    接口: stock_jgdy_tj_em

    目标地址: http://data.eastmoney.com/jgdy/tj.html

    描述: 东方财富-数据中心-特色数据-机构调研-机构调研统计

    限量: 单次返回所有历史数据
    """
    try:
        stock_jgdy_tj_em = ak.stock_jgdy_tj_em(date=request.date)

        stock_jgdy_tj_em_df = sanitize_data_pandas(stock_jgdy_tj_em)

        return stock_jgdy_tj_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 东方财富-数据中心-特色数据-机构调研-机构调研详细
@router.post("/stock_jgdy_detail_em", operation_id="stock_jgdy_detail_em")
async def stock_jgdy_detail_em(request: DateRequest):
    """
    东方财富-机构调研-机构调研详细

    接口: stock_jgdy_detail_em

    目标地址: http://data.eastmoney.com/jgdy/xx.html

    描述: 东方财富-数据中心-特色数据-机构调研-机构调研详细

    限量: 单次所有历史数据, 由于数据量比较大需要等待一定时间
    """
    try:
        stock_jgdy_detail_em = ak.stock_jgdy_detail_em(date=request.date)

        stock_jgdy_detail_em_df = sanitize_data_pandas(stock_jgdy_detail_em)

        return stock_jgdy_detail_em_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
