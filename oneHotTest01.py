from  sklearn import preprocessing
import numpy as np


age = [28,20,28,29]
addr = ['서울','마산','서울','대전','광주']


# b_age = preprocessing.Binarizer().fit_transform(age)
# b_addr= preprocessing.Binarizer().fit_transform(addr)

# b_age = preprocessing.LabelBinarizer().fit_transform(age)
# print(b_age)
# age = [28,20,28,29]
#   20   28  29
# [[0   1   0]              28
#  [1   0   0]              20
#  [0   1   0]              28
#  [0   0   1]]             29


b_addr = preprocessing.LabelBinarizer().fit_transform(addr)
print(b_addr)
# addr = ['서울','마산','서울','대전','광주']
#   광주   대전    마산 서울
# [[0   0   0   1]        서울
#  [0   0   1   0]        마산
#  [0   0   0   1]        서울
#  [0   1   0   0]        대전
#  [1   0   0   0]]       광주

# 값의 종류의 수 만큼 feature가 생성하고
# 해당 feature에 불을 켜고(1) 나머지는 불을 끈다(0)




