# -*- coding:utf-8 -*-

'''
#等额本金 每月还的本金是一样多
#每月应缴 =（总金额-（还款月数 - 1）* (贷款本金/还款月数)）* 月利率
for n in range(1,13):    #将13改成你需要的月数+1
    def p(cash, month, rate, n):
        capital_per_month = cash / month
        interest = (cash - (n - 1) * capital_per_month) * rate
        return capital_per_month + interest
    print('第' + str(n) + '月月供:' + str(round (p(100000,24, 0.004083, n),4)) + '元。')  #（p（钱数、月数、月利率、n不用改），保留小数点）
只要改两个地方


# 等额本息 每月还款额计算公式如下：
# =(贷款本金*月利率*(1+月利率)^还款月数)/((1+月利率)^还款月数－1)
'''
def p(cash, month, rate):
    common = (1+rate) ** month
    return cash * common * rate / (common - 1)
print('需还款' + str(24) + '个月，平均每月月供：' + str(round (p(100000, 24, 0.004083), 4)))

#改两个地方 1.str（月份数） 2. p(钱数,月份, 利率), 保留小数点数)