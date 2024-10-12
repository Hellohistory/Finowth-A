import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 集思录-T+0 QDII-亚洲指数-亚洲指数
@router.get("/qdii_a_index_jsl",
            operation_id="qdii_a_index_jsl")
def qdii_a_index_jsl():
    """
    亚洲指数-T+0 QDII 亚洲指数-亚洲指数

    接口: qdii_a_index_jsl

    目标地址: https://www.jisilu.cn/data/qdii/#qdiia

    描述: 集思录-T+0 QDII-亚洲市场-亚洲指数

    限量: 单次返回所有数据
    """
    try:
        qdii_a_index_jsl = ak.qdii_a_index_jsl()
        qdii_a_index_jsl_df = sanitize_data_pandas(qdii_a_index_jsl)
        return qdii_a_index_jsl_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
