import akshare as ak
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class BondSymbolSpot(BaseModel):
    symbol: str = Field(..., title="带市场标识的转债代码",
                        description="例：sz128039")


# 债券-沪深可转债-可转债-详情资料
@router.post("/bond_cb_profile_sina",
             operation_id="post_bond_cb_profile_sina")
async def post_bond_cb_profile_sina(request: BondSymbolSpot):
    """
    债券-沪深可转债-可转债-详情资料

    接口: bond_cb_profile_sina

    目标地址: https://money.finance.sina.com.cn/bond/info/sz128039.html

    描述: 新浪财经-债券-可转债-详情资料

    限量: 单次返回指定带市场标识的转债代码的可转债-详情资料数据
    """
    try:
        bond_cb_profile_sina = ak.bond_cb_profile_sina(symbol=request.symbol)
        bond_cb_profile_sina_df = sanitize_data_pandas(bond_cb_profile_sina)

        return bond_cb_profile_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-沪深可转债-实时行情数据
@router.get("/bond_zh_hs_cov_spot",
            operation_id="get_bond_zh_hs_cov_spot")
async def get_bond_zh_hs_cov_spot():
    """
    债券-沪深可转债-实时行情数据

    接口: bond_zh_hs_cov_spot

    目标地址: https://vip.stock.finance.sina.com.cn/mkt/#hskzz_z

    描述: 新浪财经-沪深可转债数据

    限量: 单次返回所有沪深可转债的实时行情数据
    """
    try:
        bond_zh_hs_cov_spot = ak.bond_zh_hs_cov_spot()
        bond_zh_hs_cov_spot_df = sanitize_data_pandas(bond_zh_hs_cov_spot)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_zh_hs_cov_spot_df.to_dict(orient="records")


# 债券-沪深可转债-可转债-详情资料
@router.post("/bond_zh_hs_cov_daily",
             operation_id="post_bond_zh_hs_cov_daily")
async def post_bond_zh_hs_cov_daily(request: BondSymbolSpot):
    """
    债券-沪深可转债-历史行情数据-日频

    接口: bond_zh_hs_cov_daily

    目标地址: https://biz.finance.sina.com.cn/suggest/lookup_n.php?q=sh110048

    描述: 新浪财经-历史行情数据，日频率更新, 新上的标的需要次日更新数据

    限量: 单次返回具体某个沪深可转债的所有历史行情数据
    """
    try:
        bond_zh_hs_cov_daily = ak.bond_zh_hs_cov_daily(symbol=request.symbol)
        bond_zh_hs_cov_daily_df = sanitize_data_pandas(bond_zh_hs_cov_daily)

        return bond_zh_hs_cov_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BondZHSCovMin(BaseModel):
    symbol: str = Field(..., title="带市场标识的转债代码", description="例：sz128039")
    period: str = Field(..., title="数据周期",
                        description="可选择：1分钟:1, 5分钟:5, 15分钟:15, 30分钟:30, 60分钟：60")
    adjust: str = Field(..., title="复权类型",
                        description="默认为空则为不复权，可选择：前复权：qfq, 后复权：hfq")
    start_date: str = Field(..., title="开始日期", description="例：1979-09-01 09:32:00")
    end_date: str = Field(..., title="结束日期", description="例：2222-01-01 09:32:00")


# 债券-沪深可转债-可转债-详情资料
@router.post("/bond_zh_hs_cov_min",
             operation_id="post_bond_zh_hs_cov_min")
async def post_bond_zh_hs_cov_min(request: BondZHSCovMin):
    """
    债券-沪深可转债-可转债-详情资料

    接口: bond_zh_hs_cov_min

    目标地址: https://quote.eastmoney.com/concept/sz128039.html

    描述: 东方财富网-可转债-分时行情

    限量: 单次返回指定可转债、指定频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 1 个交易日数据且不复权;
    其余数据周期只能获取近期的数据
    """
    try:
        bond_cb_profile_sina = ak.bond_cb_profile_sina(symbol=request.symbol)
        bond_cb_profile_sina_df = sanitize_data_pandas(bond_cb_profile_sina)

        return bond_cb_profile_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-沪深可转债-历史行情数据-盘前分时
@router.get("/bond_zh_hs_cov_pre_min",
            operation_id="get_bond_zh_hs_cov_pre_min")
async def get_bond_zh_hs_cov_pre_min():
    """
    债券-沪深可转债-实时行情数据

    接口: bond_zh_hs_cov_pre_min

    目标地址: https://quote.eastmoney.com/concept/sz128039.html

    描述: 东方财富网-可转债-分时行情-盘前分时

    限量: 单次返回指定可转债在最近一个交易日的盘前分时数据
    """
    try:
        bond_zh_hs_cov_pre_min = ak.bond_zh_hs_cov_pre_min()
        bond_zh_hs_cov_pre_min_df = sanitize_data_pandas(bond_zh_hs_cov_pre_min)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_zh_hs_cov_pre_min_df.to_dict(orient="records")


# 债券-沪深可转债-可转债数据一览表
@router.get("/bond_zh_cov", operation_id="get_bond_zh_cov")
async def get_bond_zh_cov():
    """
    债券-沪深可转债-可转债数据一览表

    接口: bond_zh_cov

    目标地址: https://data.eastmoney.com/kzz/default.html

    描述: 东方财富网-数据中心-新股数据-可转债数据一览表

    限量: 单次返回当前交易时刻的所有可转债数据
    """
    try:
        bond_zh_cov = ak.bond_zh_cov()
        bond_zh_cov_df = sanitize_data_pandas(bond_zh_cov)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_zh_cov_df.to_dict(orient="records")
