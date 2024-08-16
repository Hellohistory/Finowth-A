import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import Field, BaseModel

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class FuturesCzceWarehouseReceipt(BaseModel):
    page: int = Field(..., title="获取指定页数", description="例：5")
    item: str = Field(..., title="处理级别", description="可选择：机关, 本级, 分局本级")
    begin: int = Field(..., title="开始页面", description="例：1")


# 银行数据-银保监分局本级行政处罚
@router.post("/bank_fjcf_table_detail",
             operation_id="bank_fjcf_table_detail")
def bank_fjcf_table_detail(request: FuturesCzceWarehouseReceipt):
    """
    银行数据-银保监分局本级行政处罚

    接口: bank_fjcf_table_detail

    目标地址: https://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId=881574&itemId=4115&generaltype=9

    描述: 首页-政务信息-行政处罚-银保监分局本级-XXXX行政处罚信息公开表, 是信息公开表不是处罚决定书书

    限量: 单次返回银保监分局本级行政处罚中的指定页数的所有表格数据
    """
    try:
        bank_fjcf_table_detail = ak.bank_fjcf_table_detail(
            page=request.page,
            item=request.item,
            begin=request.begin,
        )
        bank_fjcf_table_detail_df = sanitize_data_pandas(bank_fjcf_table_detail)

        return bank_fjcf_table_detail_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
