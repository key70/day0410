import numpy as np
import pandas as pd
import xlrd

df = pd.read_excel("../world-series/MLB World Series Champions_ 1903-2016.xlsx")
print(df.head())

# 최다챔피언한  5위안에 드는 팀을 출력하고 싶어요
# 우승한 횟수가 동일한 팀여 여러팀인 경우 모두 출력해 주세요.
win_count  = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
sorted_win_count = win_count.sort_values(by='Wins', ascending=False)
# print(sorted_win_count)

# 우승한 회수를 중복이 되지 않도록 뽑아와요       ==> r
r = sorted_win_count['Wins'].unique()


# 그중에 5번째 값을 뽑아와요(r중에 5번째 위치한 값을 뽑아옴)   ==> min
min = r[4]
# print(min)

# sorted_win_count 의 Wins가 그 5번째 값 이상   ==> Wins가 min이상 되는 데이터를 출력
# a = sorted_win_count['Wins'] >= min
top_5 = sorted_win_count[ sorted_win_count['Wins'] >= min   ]
print(top_5)









# #연습) 월드시리즈가 열리지 않는 연도를 출력해 봅니다.
# all_Year = np.arange(1903, 2017)
# g_Year =  np.array(df['Year'])
# # print(type(all_Year))
# # print(type(g_Year))
#
# not_year = np.setdiff1d(all_Year, g_Year)
# # not_year = np.setdiff1d(g_Year, all_Year)
#
# print(not_year)


#연습) 월드시리즈가 열리지 않는 연도를 출력해 봅니다.
# not_Year = []
# g_Year = df['Year']
#
# for i in range(len(g_Year)-1):
#     if g_Year[i+1] - g_Year[i] > 1:
#         not_Year.append(g_Year[i]+1)
#
# print(not_Year)


#연습) 월드시리즈가 열리지 않는 연도를 출력해 봅니다.
# not_Year = []
# all_Year = np.arange(1903, 2017)
# g_Year = df['Year']
# print(len(all_Year))
# print(len(g_Year))
#
# i = 0
# for y in all_Year:
#     yy = g_Year[i]
#     if y != yy:
#         not_Year.append(y)
#         continue
#     i = i + 1
# print(not_Year)
# [1904, 1994]







# #연습) New York Yankees 팀이 처음 우승한 연도와 마지막으로 우승한 연도를 출력해 봅니다.
#
# df_nyy = df[df['Champion'] == 'New York Yankees']
# firstYear, lastYear = df_nyy['Year'].min(), df_nyy['Year'].max()
# # sorted_df_nyy = df_nyy.sort_values(by='Year')
# # firstYear, lastYear = sorted_df_nyy.iloc[0]['Year'],sorted_df_nyy.iloc[-1]['Year']
# # # firstYear, lastYear = sorted_df_nyy.head(1)['Year'],sorted_df_nyy.tail(1)['Year']
# print(firstYear,lastYear)
# print(type(firstYear))

# print(sorted_df_nyy.iloc[0]['Year'])




#연습)우승한 횟수가 100승이상인 팀을 출력해 주세요.
# print(df.head())
# df_100 = df[ df['Wins'] >= 100]
# df_100_team= df_100['Champion'].unique()
# print(df_100_team)
# print(len(df_100_team))






# print(df.head())
# print(df.columns)
# print(df)

# champion_count = df.pivot_table(values='Wins', index='Champion', aggfunc='count')
# print(champion_count)
# print(type(champion_count))


# 연습) 팀별로 평균승률을 출력해 봅니다.
# winratio_mean = df.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
# # print(winratio_mean)
#
# # 연습) 평균승률이 높은 상위 5개의 팀을 출력해 봅니다.
# sorted_winratio = winratio_mean.sort_values(by='WinRatio', ascending=False)
# print(sorted_winratio.head(3))
#
#
# #연습) 2000년이후의 데이터 중에 평균승률이 가장 높은 상위 5개의 팀을 알려주세요.
# df_2000 = df[ df['Year'] >= 2000 ]
# winratio_mean = df_2000.pivot_table(values='WinRatio', index='Champion', aggfunc='mean')
# sorted_winratio = winratio_mean.sort_values(by='WinRatio', ascending=False)
# print(sorted_winratio.head(3))
#





