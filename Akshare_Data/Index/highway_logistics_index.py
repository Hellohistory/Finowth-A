import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class IndexPriceCflp(BaseModel):
    symbol: str = Field(..., title="时间周期",
                        description="可选择 周指数, 月指数, 季度指数, 年度指数")


# 指数数据-公路物流指数-中国公路物流运价指数
@router.post("/index_price_cflp",
             operation_id="post_index_price_cflp")
def post_index_price_cflp(request: IndexPriceCflp):
    """
    指数数据-公路物流指数-中国公路物流运价指数

    接口: index_price_cflp

    目标地址: http://index.0256.cn/expx.htm

    描述: 获取指定时间周期的中国公路物流运价指数的数据
    """
    try:
        index_price_cflp = ak.index_price_cflp(
            symbol=request.symbol
        )
        index_price_cflp_df = sanitize_data_pandas(index_price_cflp)

        return index_price_cflp_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-公路物流指数-中国公路物流运量指数
@router.post("/index_volume_cflp",
             operation_id="post_index_volume_cflp")
def post_index_volume_cflp(request: IndexPriceCflp):
    """
    指数数据-公路物流指数-中国公路物流运量指数

    接口: index_volume_cflp

    目标地址: http://index.0256.cn/expx.htm

    描述: 获取指定时间周期的中国公路物流运价指数的数据
    """
    try:
        index_volume_cflp = ak.index_volume_cflp(
            symbol=request.symbol
        )
        index_volume_cflp_df = sanitize_data_pandas(index_volume_cflp)

        return index_volume_cflp_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
