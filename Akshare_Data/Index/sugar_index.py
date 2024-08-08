import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-沐甜科技数据中心-中国食糖指数
@router.get("/index_sugar_msweet",
            operation_id="get_index_sugar_msweet")
def get_index_sugar_msweet():
    """
    指数数据-沐甜科技数据中心-中国食糖指数

    接口: index_sugar_msweet

    目标地址: http://www.msweet.com.cn/mtkj/sjzx13/index.html

    描述: 沐甜科技数据中心-中国食糖指数
    """
    try:
        index_sugar_msweet = ak.index_sugar_msweet()
        data = index_sugar_msweet.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-沐甜科技数据中心-配额内进口糖估算指数
@router.get("/index_inner_quote_sugar_msweet",
            operation_id="get_index_inner_quote_sugar_msweet")
def get_index_inner_quote_sugar_msweet():
    """
    指数数据-沐甜科技数据中心-配额内进口糖估算指数

    接口: index_inner_quote_sugar_msweet

    目标地址: http://www.msweet.com.cn/mtkj/sjzx13/index.html

    描述: 沐甜科技数据中心-配额内进口糖估算指数
    """
    try:
        index_inner_quote_sugar_msweet = ak.index_inner_quote_sugar_msweet()
        data = index_inner_quote_sugar_msweet.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-沐甜科技数据中心-配额外进口糖估算指数
@router.get("/index_outer_quote_sugar_msweet",
            operation_id="get_index_outer_quote_sugar_msweet")
def get_index_outer_quote_sugar_msweet():
    """
    指数数据-沐甜科技数据中心-配额外进口糖估算指数

    接口: index_outer_quote_sugar_msweet

    目标地址: http://www.msweet.com.cn/mtkj/sjzx13/index.html

    描述: 沐甜科技数据中心-配额外进口糖估算指数
    """
    try:
        index_outer_quote_sugar_msweet = ak.index_outer_quote_sugar_msweet()
        data = index_outer_quote_sugar_msweet.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
