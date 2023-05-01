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

loaded_model = load_model('best_model.h5')

def sentiment_predict(new_sentence):
  new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣 ]','', new_sentence)
  new_sentence = okt.morphs(new_sentence, stem=True) # 토큰화
  new_sentence = [word for word in new_sentence if not word in stopwords] # 불용어 제거
  encoded = tokenizer.texts_to_sequences([new_sentence]) # 정수 인코딩
  pad_new = pad_sequences(encoded, maxlen = 30) # 패딩
  score = float(loaded_model.predict(pad_new)) # 예측
  if(score > 0.5):
    print("{:.2f}% 확률로 긍정 리뷰입니다.\n".format(score * 100))
  else:
    print("{:.2f}% 확률로 부정 리뷰입니다.\n".format((1 - score) * 100))

print("짜다, 달다 비교")
sentiment_predict('짜다')
sentiment_predict('달다')
sentiment_predict('너무 짜다')
sentiment_predict('너무 달다')
sentiment_predict('짜서 맛있다')
sentiment_predict('달아서 맛있다')

print("긍정, 부정")
print("\nshort positive")
sentiment_predict('항상 믿고 시켜먹습니다. 감사합니다')
sentiment_predict('가족들이 너무좋아해요')
sentiment_predict('간이 심심하니 좋네요 잘먹었습니다')
print("\nshort negative")
sentiment_predict('맛이 아쉽네요')
sentiment_predict('저번이랑 맛이 달라졌어요')
sentiment_predict('머리카락이 나왔네요')

print("\nlong positive")
sentiment_predict('배달분 친절도 하시고 간짜장 야채도 너무 신선하고 우리 애가 너무 맛있게 먹었어요')
sentiment_predict('탕수육 중자 시켰는데 소스 진짜 맛있고 밍밍하지도 않아요 그리고 탕수육도 딱딱하지 않고 너무너무 알맞게 튀겨져서 쫀득하고 맛있었어요 게다가 군만두까지 서비스로 주셨어요 탕수육 먹어 본데 중 절 맛있었어요 앞으로도 쭉 이랬으면 좋겠어요')
sentiment_predict('우거지갈비탕이 재료가 소진돼서 해물된장찌개로 바꿨는데 시원하고 맛있었어요 닭볶음탕도 살도 많고 양념도 맛있어서 좋았고 포장 깔끔하고 반찬도 4가지 주셔서 좋았어요')
print("\nlong negative")
sentiment_predict('주문 요청 사항에 양파는 빼 달라고 요청했는데도 양파를 넣어서 보내셨네요 양파를 못 먹는 사람 있어서 부탁드린 건데 저는 괜찮은데 같이 먹는 사람은 피자를 못 먹었어요 다음부터는 요청사항에 신경 좀 쓰시길')
sentiment_predict('리뷰 순위 보고 주문했습니다 피자 리뷰처럼 치즈 양은 많았으나 피자 전체 양파 향이 강하게 나서 아쉬웠습니다 피자소스 전반적으로 심심해서 다른 소스 만들어서 찍을 정도로 심심한 맛 도우는 깨도 우 괜찮았으면 빠른 배달로 인해 피자는 따뜻했으나 맛은 아쉬웠습니다')
sentiment_predict('피자 토핑도 정말 많고 양도 많고 깔끔했지만 스파게티가 너무 맛이 소스를 다시 생각해 보셔야 될 거 같아요 면도 너무 안 익었는데 퍼지고 스파게티가 실망이었어요')