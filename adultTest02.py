import numpy as np
import pandas as pd

names = ['age','workclass','fnlwgt','education','education-num',
         'marital-status','occupation','relationship','race',
         'sex','capital-gain','capital-loss','hours-per-week','native-country','income']

data = pd.read_csv("../Data/adult.data.txt",header=None, names=names)


data = data[['age','workclass', 'education','sex',
             'hours-per-week', 'occupation', 'income' ]]


#workclass      직업분류
#occupation     직업


#연습) 직업분류의 종류는 모두 몇가지 인지 출력해 봅니다.
# workclass = data['workclass'].unique()
# print(workclass)
# # [' State-gov' ' Self-emp-not-inc' ' Private' ' Federal-gov' ' Local-gov'
# #  ' ?' ' Self-emp-inc' ' Without-pay' ' Never-worked']
# print(len(workclass))
#9


#연습) 직업의 종류는 모두 며가지 인지 출력해 봅니다.
# occupation = data['occupation'].unique()
# print(occupation)
# print(len(occupation))
# [' Adm-clerical' ' Exec-managerial' ' Handlers-cleaners' ' Prof-specialty'
#  ' Other-service' ' Sales' ' Craft-repair' ' Transport-moving'
#  ' Farming-fishing' ' Machine-op-inspct' ' Tech-support' ' ?'
#  ' Protective-serv' ' Armed-Forces' ' Priv-house-serv']
# 15


#연습) 학력의 종류는 모두 몇가지 인지 출력해 봅니다.
# education = data['education'].unique()
# print(education)
# print(len(education))
# [' Bachelors' ' HS-grad' ' 11th' ' Masters' ' 9th' ' Some-college'
#  ' Assoc-acdm' ' Assoc-voc' ' 7th-8th' ' Doctorate' ' Prof-school'
#  ' 5th-6th' ' 10th' ' 1st-4th' ' Preschool' ' 12th']
# 16

#연습) 성별의 종류른 모두 몇가지 인지 출력해 봅니다.
# sex = data['sex'].unique()
# print(sex)
# print(len(sex))
#
# [' Male' ' Female']
# 2

#연습) 수익의 종류는 모두 몇가지 인지 출력해 봅니다.
# income = data['income'].unique()
# print(income)
# print(len(income))
# [' <=50K' ' >50K']
# 2


#연습) 50000달러 이상인 사람은 모두 몇명인가요?
over_50k = data[data['income'] ==  ' >50K']
# print(len(over_50k))
# 7841

#연습) 여자중에 50000달러 이상인 사람은 모두 몇명인가요?
f_over_50k = over_50k[over_50k['sex'] == ' Female']
# print(len(f_over_50k))
# 1179

#연습) 50000달러 이상인 사람들의 평균나이는 몇살인가요?
avg_age_over_50k = over_50k['age'].mean()
# print(avg_age_over_50k)
# 44.24984058155847

#연습) 가장 많은 직업군은 무엇인가요?
wk_count = data.pivot_table(values='income', index='workclass', aggfunc='count')
wk_count = wk_count.sort_values(by='income', ascending=False)
# print(wk_count.head(5))
#                    income
# workclass
#  Private            22696
#  Self-emp-not-inc    2541
#  Local-gov           2093
#  ?                   1836
#  State-gov           1298


#연습) 가장 많은 학력은 무엇인가요?
education_cnt = data.pivot_table(values='income', index='education', aggfunc='count')
education_cnt = education_cnt.sort_values(by='income', ascending=False)
# print(education_cnt.head(1))
#
#            income
# education
#  HS-grad    10501


#연습) 50000달러 이상인 직업중에 주당 일하는 시간이 가장 적은 직업 top5는 무엇인가요?
#       직업(occupation)의 종류별로 주당일하는 시간(hours-per-week)의 평균

avg_hours_over_50k = over_50k.pivot_table(values='hours-per-week', index='occupation', aggfunc='mean')
avg_hours_over_50k = avg_hours_over_50k.sort_values(by='hours-per-week')
print(avg_hours_over_50k.head())
print(avg_hours_over_50k.tail())

# occupation
#  Priv-house-serv       35.000000
#  ?                     36.146597
#  Armed-Forces          40.000000
#  Adm-clerical          40.942801
#  Tech-support          41.427562
#                    hours-per-week
# occupation
#  Protective-serv        45.549763
#  Exec-managerial        47.308435
#  Sales                  47.431333
#  Transport-moving       48.771875
#  Farming-fishing        54.208696


























