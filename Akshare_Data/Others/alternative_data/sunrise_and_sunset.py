import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class Sunrise(BaseModel):
    date: str = Field(..., title="指定时间",
                      description="例：20240428")
    city: str = Field(..., title="指定城市",
                      description="例：beijing; 注意输入的城市的拼音 ")


# 另类数据-日出和日落-日出和日落-天
@router.post("/sunrise_daily",
             operation_id="sunrise_daily")
def sunrise_daily(request: Sunrise):
    """
    另类数据-日出和日落-日出和日落-天

    接口: sunrise_daily

    目标地址: https://www.timeanddate.com/sun/china/

    描述: 中国各大城市-日出和日落时间, 数据区间从 19990101-至今, 推荐使用代理访问

    限量: 单次返回指定日期和指定城市的数据
    """
    try:
        sunrise_daily = ak.sunrise_daily(
            date=request.date,
            city=request.city
        )
        sunrise_daily_df = sanitize_data_pandas(sunrise_daily)

        return sunrise_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 另类数据-日出和日落-日出和日落-月
@router.post("/sunrise_monthly",
             operation_id="sunrise_monthly")
def sunrise_monthly(request: Sunrise):
    """
    另类数据-日出和日落-日出和日落-月

    接口: sunrise_monthly

    目标地址: https://www.timeanddate.com/sun/china/

    描述: 中国各大城市-日出和日落时间, 数据区间从 19990101-至今, 推荐使用代理访问

    限量: 单次返回指定日期所在月份每天的数据, 如果是未来日期则为预测值
    """
    try:
        sunrise_monthly = ak.sunrise_monthly(
            date=request.date,
            city=request.city
        )
        sunrise_monthly_df = sanitize_data_pandas(sunrise_monthly)

        return sunrise_monthly_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
