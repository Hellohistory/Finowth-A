import warnings

import akshare as ak
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from Akshare_Data.utility_function import sanitize_data_pandas

router = APIRouter()


class OptionCommodityContractSina(BaseModel):
    symbol: str = Field(..., title="期权名称", description="例：玉米期权")
    contract: str = Field(..., title="合约时间",
                          description="例：au2204，可通过 option_commodity_contract_sina 获取")


# 期权-商品期权-新浪财经-当前合约- T 型报价表
@router.post("/option_commodity_contract_table_sina",
             operation_id="option_commodity_contract_table_sina")
def option_commodity_contract_table_sina(request: OptionCommodityContractSina):
    """
    期权-商品期权-新浪财经-当前合约- T 型报价表

    接口: option_commodity_contract_table_sina

    目标地址: https://stock.finance.sina.com.cn/futures/view/optionsDP.php

    描述: 新浪财经-商品期权的 T 型报价表

    限量: 单次返回指定 symbol 和 contract 的所有数据
    """
    try:
        option_commodity_contract_table_sina = ak.option_commodity_contract_table_sina(
            symbol=request.symbol,
            contract=request.contract
        )
        option_commodity_contract_table_sina_df = sanitize_data_pandas(option_commodity_contract_table_sina)

        return option_commodity_contract_table_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionCommInfo(BaseModel):
    symbol: str = Field(..., title="期权名称",
                        description="例：工业硅期权，可使用 option_comm_symbol 获取")


# 期权-商品期权-新浪财经-当前合约
@router.post("/option_comm_info",
             operation_id="option_comm_info")
def option_comm_info(request: OptionCommodityContractSina):
    """
    期权-商品期权-新浪财经-当前合约

    接口: option_comm_info

    目标地址: https://www.9qihuo.com/qiquanshouxufei

    描述: 九期网-商品期权手续费数据

    限量: 单次返回指定期权的所有数据
    """
    try:
        option_commodity_contract_sina = ak.option_commodity_contract_sina(
            symbol=request.symbol
        )
        option_commodity_contract_sina_df = sanitize_data_pandas(option_commodity_contract_sina)

        return option_commodity_contract_sina_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionShfeDaily(BaseModel):
    symbol: str = Field(..., title="期权名称",
                        description="例：铜期权，可通过options_of_the_previous_stock_exchange获取相对应的商品期权品种以及对于的上市时间")
    trade_date: str = Field(..., title="选择时间",
                            description="例：20191017，时间需要在商品上市后")


# 期权-商品期权-上海期货交易所-商品期权数据
@router.post("/option_shfe_daily",
             operation_id="option_shfe_daily")
def option_shfe_daily(request: OptionShfeDaily):
    """
    期权-商品期权-上海期货交易所-商品期权数据

    接口: option_shfe_daily

    目标地址: http://tsite.shfe.com.cn/statements/dataview.html?paramid=kxQ

    描述: 上海期货交易所-商品期权数据，可通过options_of_the_previous_stock_exchange获取相对应的商品期权品种以及对于的上市时间

    限量: 单次返回指定品种和时间的期权行情数据

    注:

    (1)期权报价单位: 铜、天然橡胶为元/吨.

    (2)期权交易单位: 铜为 5 吨/手；天然橡胶为 10 吨/手.

    (3)成交量、持仓量、持仓量变化单位为手, 双边计算；成交额双边计算.

    (4)涨跌1=收盘价-前结算价, 涨跌2=结算价-前结算价.

    (5)合约系列: 具有相同月份标的期货合约的所有期权合约的统称.

    (6)隐含波动率: 根据期权市场交易价格, 利用期权定价模型计算出来的标的期货合约的价格波动率数值.
    """
    try:
        option_shfe_daily = ak.option_shfe_daily(
            symbol=request.symbol
        )
        option_shfe_daily_df = sanitize_data_pandas(option_shfe_daily)

        return option_shfe_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionDceDaily(BaseModel):
    symbol: str = Field(..., title="期权名称",
                        description="例：玉米期权，可通过 options_dalian_commodity_exchange 获取相对应的商品期权品种以及对于的上市时间")
    trade_date: str = Field(..., title="选择时间",
                            description="例：20191017，时间需要在商品上市后")


# 期权-商品期权-大连商品交易所-商品期权数据
@router.post("/option_dce_daily",
             operation_id="option_dce_daily")
def option_dce_daily(request: OptionDceDaily):
    """
    期权-商品期权-大连商品交易所-商品期权数据

    接口: option_dce_daily

    目标地址: http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rxq/index.html

    描述: 大连商品交易所-商品期权数据

    限量: 单次返回指定品种和时间的期权行情数据

    说明:

    (1)价格: 元/吨, 鸡蛋为元/500千克, 纤维板、胶合板为元/张

    (2)成交量、持仓量: 手(按双边计算)

    (3)成交额: 万元(按双边计算)

    (4)涨跌＝收盘价－前结算价

    (5)涨跌1=今结算价-前结算价

    (6)合约系列: 具有相同月份标的期货合约的所有期权合约的统称

    (7)隐含波动率: 根据期权市场价格, 利用期权定价模型计算的标的期货合约价格波动率

    """
    try:
        option_dce_daily = ak.option_dce_daily(
            symbol=request.symbol,
            trade_date=request.trade_date
        )
        option_dce_daily_df = sanitize_data_pandas(option_dce_daily)

        return option_dce_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionCzceDaily(BaseModel):
    symbol: str = Field(..., title="期权名称",
                        description="例：白糖期权，可通过 options_zhengzhou_commodity_exchange 获取相对应的商品期权品种以及对于的上市时间")
    trade_date: str = Field(..., title="选择时间",
                            description="例：20191017，时间需要在商品上市后")


# 期权-商品期权-郑州商品交易所-商品期权数据
@router.post("/option_czce_daily",
             operation_id="option_czce_daily")
def option_czce_daily(request: OptionCzceDaily):
    """
    期权-商品期权-郑州商品交易所-商品期权数据

    接口: option_czce_daily

    目标地址: http://www.czce.com.cn/cn/jysj/mrhq/H770301index_1.htm

    描述: 郑州商品交易所-商品期权数据

    限量: 单次返回指定品种和时间的期权行情数据

    说明:

    (1)价格: 元/吨

    (2)成交量、空盘量: 手

    (3)成交额: 万元

    (4)涨跌一: 今收盘-昨结算

    (5)涨跌二: 今结算-昨结算

    (6)隐含波动率: 将当日期权合约的结算价代入期权定价模型, 反推出来的波动率数值
    """
    try:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            option_czce_daily = ak.option_czce_daily(
                symbol=request.symbol,
                trade_date=request.trade_date
            )
            option_czce_daily_df = sanitize_data_pandas(option_czce_daily)

            # 筛选警告信息，提取包含“非交易日”的信息
            warning_msgs = [str(warn.message) for warn in w if "非交易日" in str(warn.message)]

            # 如果 data 为空，并且有警告信息，则只返回警告信息
            if option_czce_daily_df.empty and warning_msgs:
                return {"warnings": warning_msgs}
            elif warning_msgs:
                return {"data": option_czce_daily_df.to_dict(orient="records"), "warnings": warning_msgs}
            else:
                return option_czce_daily_df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionCzceHist(BaseModel):
    symbol: str = Field(..., title="期权名称",
                        description="例：SR，可通过 options_zhengzhou_commodity_exchange 获取相对应的商品期权品种代码以及对于的上市时间")
    year: str = Field(..., title="选择时间",
                      description="例：2019，时间需要在商品上市后")


# 期权-商品期权-郑州商品交易所-商品期权数据
@router.post("/option_czce_hist",
             operation_id="option_czce_hist")
def option_czce_hist(request: OptionCzceHist):
    """
    期权-商品期权-郑州商品交易所-商品期权数据

    接口: option_czce_hist

    目标地址: http://www.czce.com.cn/cn/jysj/lshqxz/H770319index_1.htm

    描述: 郑州商品交易所的商品期权历史行情数据

    限量: 单次返回指定年份指定品种期权历史行情数据
    """
    try:
        option_czce_hist = ak.option_czce_hist(
            symbol=request.symbol,
            year=request.year
        )
        option_czce_hist_df = sanitize_data_pandas(option_czce_hist)

        return option_czce_hist_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class OptionGfexDaily(BaseModel):
    symbol: str = Field(..., title="期权名称",
                        description="例：工业硅，可通过 options_guangzhou_commodity_exchange 获取相对应的商品期权品种以及对于的上市时间")
    trade_date: str = Field(..., title="选择时间",
                            description="例：20191017，时间需要在商品上市后")


# 期权-商品期权-广州商品交易所-商品期权数据
@router.post("/option_gfex_daily",
             operation_id="option_gfex_daily")
def option_gfex_daily(request: OptionGfexDaily):
    """
    期权-商品期权-广州商品交易所-商品期权数据

    接口: option_gfex_daily

    目标地址: http://www.gfex.com.cn/gfex/rihq/hqsj_tjsj.shtml

    描述: 广州期货交易所-商品期权数据

    限量: 单次返回指定品种和时间的期权行情数据

    说明:

    (1)价格: 元/吨

    (2)成交量、空盘量: 手

    (3)成交额: 万元

    (4)涨跌一: 今收盘-昨结算

    (5)涨跌二: 今结算-昨结算

    (6)隐含波动率: 将当日期权合约的结算价代入期权定价模型, 反推出来的波动率数值
    """
    try:
        option_gfex_daily = ak.option_gfex_daily(
            symbol=request.symbol,
            trade_date=request.trade_date
        )
        option_gfex_daily_df = sanitize_data_pandas(option_gfex_daily)

        return option_gfex_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 期权-商品期权-广州商品交易所-隐含波动参考值
@router.post("/option_gfex_vol_daily",
             operation_id="option_gfex_vol_daily")
def option_gfex_vol_daily(request: OptionGfexDaily):
    """
    期权-商品期权-广州商品交易所-隐含波动参考值

    接口: option_gfex_vol_daily

    目标地址: http://www.gfex.com.cn/gfex/rihq/hqsj_tjsj.shtml

    描述: 广州期货交易所-商品期权数据-隐含波动参考值

    限量: 单次返回指定品种和时间的期权行情数据

    说明:

    (1)价格: 元/吨

    (2)成交量、空盘量: 手

    (3)成交额: 万元

    (4)涨跌一: 今收盘-昨结算

    (5)涨跌二: 今结算-昨结算

    (6)隐含波动率: 将当日期权合约的结算价代入期权定价模型, 反推出来的波动率数值
    """
    try:
        option_gfex_vol_daily = ak.option_gfex_vol_daily(
            symbol=request.symbol,
            trade_date=request.trade_date
        )
        option_gfex_vol_daily_df = sanitize_data_pandas(option_gfex_vol_daily)

        return option_gfex_vol_daily_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(router, host="0.0.0.0", port=36925)
