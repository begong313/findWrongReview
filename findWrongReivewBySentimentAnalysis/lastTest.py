"""
생성된 모델로 기존의 리뷰를 재검사하는 코드.
램 누수 발생해서 계속 꺼진다.
어디서 발생하는지 잘 모르겠음
"""
import traceback
import pickle
import re

import pymysql
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
okt = Okt()
X_test = []

with open('tokenizer2.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

#db불러오기
dbcon=pymysql.connect(host='localhost', user='root',password='!shwhdqls12',db='yogiyocomment', charset='utf8')
cur = dbcon.cursor()
loadingQuery = "select comment from yogiyocomment.reviewdatanew where num=%s and (isnull(PosOrNe))"
updateQuery = "UPDATE yogiyocomment.reviewdatanew set PosOrNe=%s where num=%s"

loaded_model = load_model('best_model.h5')

def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = 30) # 패딩


  try:
    score = float(loaded_model.predict(pad_new)) # 예측
  except:
      return 2
  if(score > 0.5):
    return True
  else:
    return False


i=1
while i<4047405:
    try:
        cur.execute(loadingQuery,i)
        rs = cur.fetchone()
        if rs == None:
            i += 1
            continue
        print(rs)
        #맞춤법 검사가 완료된 comment 다시 탑제
        cur.execute(updateQuery,(sentiment_predict(rs[0]),i))


        dbcon.commit()
        print(i)
        i += 1


    except :
        traceback.print_exc()
        i+=1
