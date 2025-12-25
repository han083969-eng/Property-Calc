from CoolProp.CoolProp import PropsSI

# 定义温度和压力
T = 373.15  # 100摄氏度
P = 101325  # 1个标准大气压

# 查询焓值
h = PropsSI('H', 'T', T, 'P', P, 'Water')

print("------------------------------------")
print(f"计算结果：100度水蒸气的焓值为 {h} J/kg")
print("------------------------------------")