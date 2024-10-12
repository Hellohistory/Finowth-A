import akshare as ak
from fastapi import HTTPException, APIRouter

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 集思录-T+0 QDII-欧美市场-欧美指数
@router.get("/qdii_e_index_jsl",
            operation_id="qdii_e_index_jsl")
def qdii_e_index_jsl():
    """
    欧美指数-T+0 QDII 欧美市场-欧美指数

    接口: qdii_e_index_jsl

    目标地址: https://www.jisilu.cn/data/qdii/#qdiia

    描述: 集思录-T+0 QDII-欧美市场-欧美指数

    限量: 单次返回所有数据
    """
    try:
        qdii_e_index_jsl = ak.qdii_e_index_jsl()
        qdii_e_index_jsl_df = sanitize_data_pandas(qdii_e_index_jsl)
        return qdii_e_index_jsl_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 集思录-T+0 QDII-欧美市场-欧美商品
@router.get("/qdii_e_comm_jsl",
            operation_id="qdii_e_comm_jsl")
def qdii_e_comm_jsl():
    """
    欧美指数-T+0 QDII 欧美市场-欧美商品

    接口: qdii_e_comm_jsl

    目标地址: https://www.jisilu.cn/data/qdii/#qdiia

    描述: 集思录-T+0 QDII-欧美市场-欧美商品

    限量: 单次返回所有数据
    """
    try:
        qdii_e_comm_jsl = ak.qdii_e_comm_jsl()
        qdii_e_comm_jsl_df = sanitize_data_pandas(qdii_e_comm_jsl)
        return qdii_e_comm_jsl_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
