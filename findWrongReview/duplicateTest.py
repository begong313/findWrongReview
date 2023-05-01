import numpy as np
import pandas as pd

train5 = pd.read_table('./reviewTrain/review4.txt')
train1 = pd.read_table('./reviewTrain/review2.txt')

print('train4:', len(train5)) # 훈련용 리뷰 개수 출력
print('train2 :', len(train1)) # 테스트용 리뷰 개수 출력

# document 열의 중복 제거
train5.drop_duplicates(subset = ['document'], inplace=True) # document 열에서 중복인 내용이 있다면 중복 제거
train5['document'] = train1['document'].replace(to_replace="[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", value="", regex=True) # 정규 표현식 수행
train5['document'] = train1['document'].replace(to_replace="^ +", value="", regex=True) # 공백은 empty 값으로 변경
train5['document'].replace('', np.nan, inplace=True) # 공백은 Null 값으로 변경
train5 = train5.dropna(how='any') # Null 값 제거
print('전처리 후 train5 :', len(train5))

train1.drop_duplicates(subset = ['document'], inplace=True) # document 열에서 중복인 내용이 있다면 중복 제거
train1['document'] = train1['document'].replace(to_replace="[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", value="", regex=True) # 정규 표현식 수행
train1['document'] = train1['document'].replace(to_replace="^ +", value="", regex=True) # 공백은 empty 값으로 변경
train1['document'].replace('', np.nan, inplace=True) # 공백은 Null 값으로 변경
train1 = train1.dropna(how='any') # Null 값 제거
print('전처리 후 train135 :', len(train1))