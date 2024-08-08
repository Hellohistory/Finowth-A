import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


# 指数数据-国证指数-全部指数
@router.get("/index_all_cni",
            operation_id="get_index_all_cni")
def get_index_all_cni():
    """
    指数数据-国证指数-全部指数

    接口: index_all_cni

    目标地址: http://www.cnindex.com.cn/zh_indices/sese/index.html?act_menu=1&index_type=-1

    描述: 国证指数-最近交易日的所有指数的代码和基本信息
    """
    try:
        index_all_cni = ak.index_all_cni()
        data = index_all_cni.to_dict(orient="records")
        sanitized_data = sanitize_data_pandas(data)

        return sanitized_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexHistCNI(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：399005，可通过 index_all_cni 获取一览表")
    start_date: str = Field(..., title="开始时间",
                            description="例：20200102")
    end_date: str = Field(..., title="结束时间",
                          description="例：20240114")


# 指数数据-国证指数-指数行情
@router.post("/index_hist_cni",
             operation_id="post_index_hist_cni")
def post_index_hist_cni(request: IndexHistCNI):
    """
    指数数据-国证指数-指数行情

    接口: index_hist_cni

    目标地址: http://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001

    描述: 国证指数-具体指数的日频率行情数据
    """
    try:
        index_hist_cni = ak.index_hist_cni(
            symbol=request.symbol,
            start_date=request.start_date,
            end_date=request.end_date,
        )
        index_hist_cni_df = sanitize_data_pandas(index_hist_cni)

        return index_hist_cni_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexHistCNI(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：399005，可通过 index_all_cni 获取一览表")
    date: str = Field(..., title="指定年月",
                      description="例：202404")


# 指数数据-国证指数-指数样本详情
@router.post("/index_detail_cni",
             operation_id="post_index_detail_cni")
def post_index_detail_cni(request: IndexHistCNI):
    """
    指数数据-国证指数-指数样本详情

    接口: index_detail_cni

    目标地址: http://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001

    描述: 国证指数-指数样本详情数据
    """
    try:
        index_detail_cni = ak.index_detail_cni(
            symbol=request.symbol,
            date=request.date
        )
        index_detail_cni_df = sanitize_data_pandas(index_detail_cni)

        return index_detail_cni_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 指数数据-国证指数-历史样本
@router.post("/index_detail_hist_cni",
             operation_id="post_index_detail_hist_cni")
def post_index_detail_hist_cni(request: IndexHistCNI):
    """
    指数数据-国证指数-历史样本

    接口: index_detail_hist_cni

    目标地址: http://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001

    描述: 国证指数-历史样本数据
    """
    try:
        index_detail_hist_cni = ak.index_detail_hist_cni(
            symbol=request.symbol,
            date=request.date
        )
        index_detail_hist_cni_df = sanitize_data_pandas(index_detail_hist_cni)

        return index_detail_hist_cni_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexDetailHistAdjustCNI(BaseModel):
    symbol: str = Field(..., title="指数代码",
                        description="例：399005，可通过 index_all_cni 获取一览表")


# 指数数据-国证指数-历史调样
@router.post("/index_detail_hist_adjust_cni",
             operation_id="post_index_detail_hist_adjust_cni")
def post_index_detail_hist_adjust_cni(request: IndexDetailHistAdjustCNI):
    """
    指数数据-国证指数-历史调样

    接口: index_detail_hist_adjust_cni

    目标地址: http://www.cnindex.com.cn/module/index-detail.html?act_menu=1&indexCode=399001

    描述: 国证指数-样本详情-历史调样
    """
    try:
        index_detail_hist_adjust_cni = ak.index_detail_hist_adjust_cni(
            symbol=request.symbol,
        )
        index_detail_hist_adjust_cni_df = sanitize_data_pandas(index_detail_hist_adjust_cni)

        return index_detail_hist_adjust_cni_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
