import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FuturesCzceWarehouseReceipt(BaseModel):
    date: str = Field(..., title="指定交易日", description="例：20200702")


# 期货数据-仓单日报-仓单日报-郑州商品交易所
@router.post("/futures_czce_warehouse_receipt",
             operation_id="post_futures_czce_warehouse_receipt")
def post_futures_czce_warehouse_receipt(request: FuturesCzceWarehouseReceipt):
    """
    期货数据-仓单日报-仓单日报-郑州商品交易所

    接口: futures_czce_warehouse_receipt

    目标地址: http://www.czce.com.cn/cn/jysj/cdrb/H770310index_1.htm

    描述: 郑州商品交易所-交易数据-仓单日报

    限量: 单次返回当前交易日的所有仓单日报数据
    """
    try:
        futures_czce_warehouse_receipt = ak.futures_czce_warehouse_receipt(
            date=request.date)
        futures_czce_warehouse_receipt_df = sanitize_data_pandas(futures_czce_warehouse_receipt)

        return futures_czce_warehouse_receipt_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
