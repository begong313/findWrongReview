"""
생성된 모델로 기존의 리뷰를 재검사하는 코드.
"""

import pickle
import re
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
okt = Okt()
X_test = []

with open('tokenizer2.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#test 리뷰 불러오기

f=open("last_Test_data.txt",'r',encoding="utf8")
txt=f.readlines()
f.close()

loaded_model = load_model('best_model.h5')

def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = 30) # 패딩
  score = float(loaded_model.predict(pad_new)) # 예측
  if(score > 0.5):
    return True
  else:
    return False


postive = 0
negative =0
for i in txt:
    try:
        if sentiment_predict(i):
            postive+=1
        else :
            negative+=1
    except:
        pass
    print("positive count : ", postive)
    print("negative count : ", negative)