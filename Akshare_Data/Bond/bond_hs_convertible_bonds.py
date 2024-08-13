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
             operation_id="bond_cb_profile_sina")
async def bond_cb_profile_sina(request: BondSymbolSpot):
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
            operation_id="bond_zh_hs_cov_spot")
async def bond_zh_hs_cov_spot():
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
             operation_id="bond_zh_hs_cov_daily")
async def bond_zh_hs_cov_daily(request: BondSymbolSpot):
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
             operation_id="bond_zh_hs_cov_min")
async def bond_zh_hs_cov_min(request: BondZHSCovMin):
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
            operation_id="bond_zh_hs_cov_pre_min")
async def bond_zh_hs_cov_pre_min():
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
@router.get("/bond_zh_cov", operation_id="bond_zh_cov")
async def bond_zh_cov():
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


class BondZHSCovInfo(BaseModel):
    symbol: str = Field(..., title="可转债代码", description="例：123121")
    indicator: str = Field(..., title="数据周期",
                           description="可选择：基本信息, 中签号, 筹资用途, 重要日期, 其 可转债重要条款 在 基本信息中")


# 债券-沪深可转债-可转债详情
@router.post("/bond_zh_cov_info",
             operation_id="bond_zh_cov_info")
async def bond_zh_cov_info(request: BondZHSCovInfo):
    """
    债券-沪深可转债-可转债详情

    接口: bond_zh_cov_info

    目标地址: https://data.eastmoney.com/kzz/detail/123121.html

    描述: 东方财富网-数据中心-新股数据-可转债详情

    限量: 单次返回指定 symbol 的可转债详情数据
    """
    try:
        bond_zh_cov_info = ak.bond_zh_cov_info(
            symbol=request.symbol,
            indicator=request.indicator
        )
        bond_zh_cov_info_df = sanitize_data_pandas(bond_zh_cov_info)

        return bond_zh_cov_info_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-沪深可转债-可转债详情-同花顺
@router.get("/bond_zh_cov_info_ths", operation_id="bond_zh_cov_info_ths")
async def bond_zh_cov_info_ths():
    """
    债券-沪深可转债-可转债数据一览表

    接口: bond_zh_cov_info_ths

    目标地址: http://data.10jqka.com.cn/ipo/bond/

    描述: 同花顺-数据中心-可转债

    限量: 单次返回所有数据
    """
    try:
        bond_zh_cov_info_ths = ak.bond_zh_cov_info_ths()
        bond_zh_cov_info_ths_df = sanitize_data_pandas(bond_zh_cov_info_ths)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_zh_cov_info_ths_df.to_dict(orient="records")


# 债券-沪深可转债-可转债比价表
@router.get("/bond_cov_comparison", operation_id="bond_cov_comparison")
async def bond_cov_comparison():
    """
    债券-沪深可转债-可转债比价表

    接口: bond_cov_comparison

    目标地址: https://quote.eastmoney.com/center/fullscreenlist.html#convertible_comparison

    描述: 东方财富网-行情中心-债券市场-可转债比价表

    限量: 单次返回当前交易时刻的所有可转债比价数据
    """
    try:
        bond_cov_comparison = ak.bond_cov_comparison()
        bond_cov_comparison_df = sanitize_data_pandas(bond_cov_comparison)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_cov_comparison_df.to_dict(orient="records")


class BondZHSCoValueAnalysis(BaseModel):
    symbol: str = Field(..., title="可转债代码", description="例：113527")


# 债券-沪深可转债-可转债价值分析
@router.post("/bond_zh_cov_value_analysis",
             operation_id="bond_zh_cov_value_analysis")
async def bond_zh_cov_value_analysis(request: BondZHSCoValueAnalysis):
    """
    债券-沪深可转债-可转债价值分析

    接口: bond_zh_cov_value_analysis

    目标地址: https://data.eastmoney.com/kzz/detail/113527.html

    描述: 东方财富网-行情中心-新股数据-可转债数据-可转债价值分析

    限量: 单次返回所有可转债价值分析数据
    """
    try:
        bond_zh_cov_value_analysis = ak.bond_zh_cov_value_analysis(
            symbol=request.symbol
        )
        bond_zh_cov_value_analysis_df = sanitize_data_pandas(bond_zh_cov_value_analysis)

        return bond_zh_cov_value_analysis_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BondCBJsl(BaseModel):
    cookie: str = Field(..., title="您的集思录 cookie",
                        description="此处输入您的集思录 cookie 就可以获取完整数据，否则只能返回前 30 条")


# 债券-沪深可转债-可转债实时数据-集思录
@router.post("/bond_cb_jsl",
             operation_id="bond_cb_jsl")
async def bond_cb_jsl(request: BondCBJsl):
    """
    债券-沪深可转债-可转债实时数据-集思录

    接口: bond_cb_jsl

    目标地址: https://app.jisilu.cn/data/cbnew/#cb

    描述: 集思录可转债实时数据，包含行情数据（涨跌幅，成交量和换手率等）及可转债基本信息（转股价，溢价率和到期收益率等）

    限量: 单次返回当前交易时刻的所有数据
    """
    try:
        bond_cb_jsl = ak.bond_cb_jsl(
            cookie=request.cookie
        )
        bond_zh_cov_value_analysis_df = sanitize_data_pandas(bond_cb_jsl)

        return bond_zh_cov_value_analysis_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 债券-沪深可转债-可转债强赎
@router.get("/bond_cb_redeem_jsl", operation_id="bond_cb_redeem_jsl")
async def bond_cb_redeem_jsl():
    """
    债券-沪深可转债-可转债强赎

    接口: bond_cb_redeem_jsl

    目标地址: https://www.jisilu.cn/data/cbnew/#redeem

    描述: 集思录可转债-强赎

    限量: 单次返回所有数据
    """
    try:
        bond_cb_redeem_jsl = ak.bond_cb_redeem_jsl()
        bond_cb_redeem_jsl_df = sanitize_data_pandas(bond_cb_redeem_jsl)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_cb_redeem_jsl_df.to_dict(orient="records")


# 债券-沪深可转债-集思录可转债等权指数
@router.get("/bond_cb_index_jsl", operation_id="bond_cb_index_jsl")
async def bond_cb_index_jsl():
    """
    债券-沪深可转债-集思录可转债等权指数

    接口: bond_cb_index_jsl

    目标地址: https://www.jisilu.cn/web/data/cb/index

    描述: 可转债-集思录可转债等权指数

    限量: 单次返回所有历史数据数据
    """
    try:
        bond_cb_index_jsl = ak.bond_cb_index_jsl()
        bond_cb_index_jsl_df = sanitize_data_pandas(bond_cb_index_jsl)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取数据失败: {str(e)}")

    return bond_cb_index_jsl_df.to_dict(orient="records")


# 债券-沪深可转债-可转债转股价格调整记录-集思录
@router.post("/bond_cb_adj_logs_jsl",
             operation_id="bond_cb_adj_logs_jsl")
async def bond_cb_adj_logs_jsl(request: BondZHSCoValueAnalysis):
    """
    债券-沪深可转债-可转债转股价格调整记录-集思录

    接口: bond_cb_adj_logs_jsl

    目标地址: https://app.jisilu.cn/data/cbnew/#cb; 点击带红色星号的转股价会弹出转股价调整记录

    描述: 集思录-单个可转债的转股价格-调整记录

    限量: 返回当前时刻该可转债的所有转股价格调整记录
    """
    try:
        bond_cb_adj_logs_jsl = ak.bond_cb_adj_logs_jsl(
            symbol=request.symbol
        )
        bond_cb_adj_logs_jsl_df = sanitize_data_pandas(bond_cb_adj_logs_jsl)

        return bond_cb_adj_logs_jsl_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class FuturesDeliverableCoupons(BaseModel):
    symbol: str = Field(..., title="查询债券名称",
                        description="例：政策性金融债(进出口行)，可通过bond_china_close_return_map获取")
    period: str = Field(..., title="期限间隔", description="可选择'0.1', '0.5', '1'")
    start_date: str = Field(..., title="开始日期", description="结束日期和开始日期不要超过 1 个月")
    end_date: str = Field(..., title="结束日期", description="结束日期和开始日期不要超过 1 个月")


# 债券-沪深可转债-国债期货可交割券相关指标
@router.post("/bond_china_close_return",
             operation_id="bond_china_close_return")
async def bond_china_close_return(request: FuturesDeliverableCoupons):
    """
    债券-沪深可转债-国债期货可交割券相关指标

    接口: bond_china_close_return

    目标地址: https://www.chinamoney.com.cn/chinese/bkcurvclosedyhis/?bondType=CYCC000&reference=1

    描述: 收盘收益率曲线历史数据, 该接口只能获取近 3 个月的数据，且每次获取的数据不超过 1 个月
    """
    try:
        bond_china_close_return = ak.bond_china_close_return(
            symbol=request.symbol,
            period=request.period,
            start_date=request.start_date,
            end_date=request.end_date
        )
        bond_china_close_return_df = sanitize_data_pandas(bond_china_close_return)

        return bond_china_close_return_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class BondZHUSRate(BaseModel):
    start_date: str = Field(..., title="需查询起始日期", description="例：20200922")


# 债券-沪深可转债-中美国债收益率
@router.post("/bond_zh_us_rate",
             operation_id="bond_zh_us_rate")
async def bond_zh_us_rate(request: BondZHUSRate):
    """
    债券-沪深可转债-中美国债收益率

    接口: bond_zh_us_rate

    目标地址: https://data.eastmoney.com/cjsj/zmgzsyl.html

    描述: 东方财富网-数据中心-经济数据-中美国债收益率历史数据

    限量: 返回 start_date 开始后的所有交易日的数据; 数据从 19901219 开始
    """
    try:
        bond_zh_us_rate = ak.bond_zh_us_rate(
            start_date=request.start_date
        )
        bond_zh_us_rate_df = sanitize_data_pandas(bond_zh_us_rate)

        return bond_zh_us_rate_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
