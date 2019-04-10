import numpy as np
import pandas as pd

# pandas의 get_dummies는
# 만약 1차원 배열을 매개변수로 받으면 그것이 숫자이던, 문자이던
# one-hot 인코딩을 해 줍니다.
# 그런데 만약 DataFrame을 매개변수로 받으면
#       기본적으로 숫자데이터는 제외하고 one-hot 인코딩을 합니다.
#       만약 숫자도 포함하여 hot-encoding을 하려면
#       DataFrame의 숫자의 속성을 문자로 변경한후 해야 합니다.
#       데이터프레임['속성명']= 데이터프레임['속성명'].astype(str)

member = pd.read_csv("../Data/member.dat")
member['age'] = member['age'].astype(str)
# print(member)
# print(member.columns)

b_member = pd.get_dummies(member)
print(b_member)


#연습 addr컬럼과 age 칼럼을 각각 one-hot 테이블을 생성해 봅니다.
# b_age = pd.get_dummies(member['age'])
# print(b_age)
#
# b_addr = pd.get_dummies(member['addr'])
# print(b_addr)
# print(b_member.columns)

# help(pd.get_dummies)
