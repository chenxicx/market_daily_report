import datetime
import akshare as ak

# 获取当前年份的第一个交易日日期（第一个周一算交易日，不考虑特殊情况）
current_year = datetime.date.today().year
first_monday = datetime.date(current_year, 1, 1) + datetime.timedelta(
    days=(0 - datetime.date(current_year, 1, 1).weekday() + 7) % 7 + 1)
first_monday = first_monday.strftime('%Y%m%d')

# 获取当日日期，格式：yymmdd 例如：20230323
current_date = datetime.date.today().strftime('%Y%m%d')

#获取上证指数1月1日开盘价
year_start_sz = ak.index_zh_a_hist("000001","daily", first_monday, first_monday)
sz00_index = year_start_sz["开盘"][0]

#获取上证指数当日收盘价
current_date_sz = ak.index_zh_a_hist("000001","daily", current_date, current_date)
sz01_index = current_date_sz["收盘"][0]

#计算年初至今涨跌幅，单位1. 例如年初至20230323涨幅为6.4%，则sz01_ytd=0.064 = 6.4%
sz01_ytd = (sz01_index - sz00_index) / sz00_index

#当日涨跌幅，单位0.01. 例如：20230323当日涨幅为0.64%，则sz01=0.64
sz01 = current_date_sz["涨跌幅"][0]

print(sz01_ytd)
print(sz01)