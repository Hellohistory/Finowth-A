import akshare as ak
from fastapi import APIRouter, HTTPException

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-申万一级行业信息
@router.get("/sw_index_first_info", operation_id="sw_index_first_info")
def sw_index_first_info():
    """
    指数数据-申万一级行业信息

    接口: sw_index_first_info

    目标地址: https://legulegu.com/stockdata/sw-industry-overview#level1

    描述: 申万一级行业信息
    """
    try:
        sw_index_first_info = ak.sw_index_first_info()
        data = sw_index_first_info.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-申万二级行业信息
@router.get("/sw_index_second_info", operation_id="sw_index_second_info")
def sw_index_second_info():
    """
    指数数据-申万二级行业信息

    接口: sw_index_second_info

    目标地址: https://legulegu.com/stockdata/sw-industry-overview#level1

    描述: 申万二级行业信息
    """
    try:
        sw_index_second_info = ak.sw_index_second_info()
        data = sw_index_second_info.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-申万三级行业信息
@router.get("/sw_index_third_info", operation_id="sw_index_third_info")
def sw_index_third_info():
    """
    指数数据-申万三级行业信息

    接口: sw_index_third_info

    目标地址: https://legulegu.com/stockdata/sw-industry-overview#level1

    描述: 申万三级行业信息
    """
    try:
        sw_index_third_info = ak.sw_index_third_info()
        data = sw_index_third_info.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-申万三级行业信息
@router.get("/sw_index_third_cons", operation_id="sw_index_third_cons")
def sw_index_third_cons():
    """
    指数数据-申万三级行业信息

    接口: sw_index_third_cons

    目标地址: https://legulegu.com/stockdata/index-composition?industryCode=851921.SI

    描述: 申万三级行业成份
    """
    try:
        sw_index_third_cons = ak.sw_index_third_cons()
        data = sw_index_third_cons.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
