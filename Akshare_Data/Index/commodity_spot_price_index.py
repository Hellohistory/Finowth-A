import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class StockGoods(BaseModel):
    symbol: str = Field(..., title="现货指数参数",
                        description="可选择 波罗的海干散货指数，钢坯价格指数，澳大利亚粉矿价格")


# 指数数据-新浪财经-商品现货价格指数
@router.post("/spot_goods", operation_id="post_spot_goods")
def post_spot_goods(request: StockGoods):
    """
    指数数据-新浪财经-商品现货价格指数

    接口: spot_goods

    目标地址: http://finance.sina.com.cn/futuremarket/spotprice.shtml#titlePos_0

    描述: 新浪财经-商品现货价格指数
    """
    try:
        spot_goods = ak.spot_goods(
            symbol=request.symbol
        )
        spot_goods_df = sanitize_data_pandas(spot_goods)

        return spot_goods_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexYW(BaseModel):
    symbol: str = Field(..., title="指数参数",
                        description="可选择 周价格指数, 月价格指数, 月景气指数")


# 指数数据-义乌小商品指数
@router.post("/index_yw", operation_id="post_index_yw")
def post_index_yw(request: IndexYW):
    """
    指数数据-义乌小商品指数

    接口: index_yw

    目标地址: https://www.ywindex.com/Home/Product/index/

    描述: 指定参数类型的义乌小商品指数的近期历史数据
    """
    try:
        index_yw = ak.index_yw(
            symbol=request.symbol
        )
        index_yw_df = sanitize_data_pandas(index_yw)

        return index_yw_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexKQFZ(BaseModel):
    symbol: str = Field(..., title="指数参数",
                        description="可选择 价格指数, 景气指数, 外贸指数")


# 指数数据-柯桥纺织品指数
@router.post("/index_kq_fz", operation_id="post_index_kq_fz")
def post_index_kq_fz(request: IndexKQFZ):
    """
    指数数据-柯桥纺织品指数

    接口: index_kq_fz

    目标地址: http://www.kqindex.cn/flzs/jiage

    描述: 指定 symbol 的柯桥纺织品指数的所有历史数据
    """
    try:
        index_kq_fz = ak.index_kq_fz(
            symbol=request.symbol
        )
        index_kq_fz_df = sanitize_data_pandas(index_kq_fz)

        return index_kq_fz_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class IndexKQFashion(BaseModel):
    symbol: str = Field(..., title="指数参数",
                        description="可选择 柯桥时尚指数, 时尚创意指数, 时尚设计人才数, 新花型推出数, "
                                    "创意产品成交数, 创意企业数量, 时尚活跃度指数, 电商运行数, 时尚平台拓展数, "
                                    "新产品销售额占比, 企业合作占比, 品牌传播费用, 时尚推广度指数, 国际交流合作次数, "
                                    "企业参展次数, 外商驻点数量变化, 时尚评价指数")


# 指数数据-柯桥纺织品指数
@router.post("/index_kq_fz", operation_id="IndexKQFashion")
def post_index_kq_fz(request: IndexKQFZ):
    """
    指数数据-柯桥纺织品指数

    接口: index_kq_fz

    目标地址: http://www.kqindex.cn/flzs/jiage

    描述: 指定 symbol 的柯桥纺织品指数的所有历史数据
    """
    try:
        index_kq_fz = ak.index_kq_fz(
            symbol=request.symbol
        )
        index_kq_fz_df = sanitize_data_pandas(index_kq_fz)

        return index_kq_fz_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
