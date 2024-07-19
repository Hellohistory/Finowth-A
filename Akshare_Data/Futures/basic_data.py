import akshare as ak

# 期货基础数据
# 期货交易费用参照表
"""
接口: futures_fees_info
目标地址: http://openctp.cn/fees.html
描述: openctp 期货交易费用参照表
限量: 单次返回所有数据
"""
futures_fees_info_df = ak.futures_fees_info()
print(futures_fees_info_df)
# 期货手续费与保证金
"""
接口: futures_comm_info
目标地址: https://www.9qihuo.com/qihuoshouxufei
描述: 九期网-期货手续费数据
限量: 单次返回指定 symbol 的所有数据
"""
futures_comm_info_df = ak.futures_comm_info(symbol="所有")
print(futures_comm_info_df)
# 期货规则-交易日历表
"""
接口: futures_rule
目标地址: https://www.gtjaqh.com/pc/calendar.html
描述: 国泰君安期货-交易日历数据表
限量: 单次返回指定交易日所有合约的交易日历数据
"""
futures_rule_df = ak.futures_rule(date="20231205")
print(futures_rule_df)
# 库存数据-99期货网
"""
接口: futures_inventory_99
目标地址: http://www.99qh.com/d/store.aspx
描述: 99 期货网-大宗商品库存数据; 周频率
限量: 单次返回指定 exchange 和指定 symbol 的具体品种的期货库存数据, 仓单日报数据
"""
futures_inventory_99_df = ak.futures_inventory_99(exchange='大连商品交易所', symbol='豆一')
print(futures_inventory_99_df)







































