# 연습)baseball2.txt파일을 읽어 들여
# 팀별로 챔피언한 횟수를 출력해 봅니다.

import numpy as np
import pandas as pd

df = pd.read_csv("../world-series/baseball2.txt")
# print(df)
# Index(['Year', 'Champion', 'Wins', 'Losses', 'Ties', 'WinRatio'], dtype='object')


#select Chamption, count(Wins) from df group by Chamption
champion_count = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
print(champion_count)



# df2 = pd.read_csv("../world-series/baseball.txt")
# # print(df2)
#
# print(df.columns)
# print(df2.columns)





