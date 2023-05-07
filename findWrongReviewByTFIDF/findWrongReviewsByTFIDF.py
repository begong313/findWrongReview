file1 = 'comments_rating5_preprocessing.txt'
file2 = 'comments_rating1_preprocessing.txt'

f1 = open(file1, "r", encoding='utf-8')
rating5 = f1.readlines()
f1.close()

f2 = open(file2, "r", encoding='utf-8')
rating1 = f2.readlines()
f2.close()


# 키워드가 리뷰에서 등장하는 빈도 조사

# 5점 리뷰 키워드
rating5Keywords = ['좋고', '잘먹었습니다', '맛나요', '맛잇어요', '맛있고', '항상', '맛있습니다', '좋아요', '맛있네요', '맛있었습니다', '먹었네요', '굿', '잘먹었어요', '좋았어요', '맛있어용', '많고', '많아서', '오랜만에', '맛있게', '언제나', '맛있었어요', '맛있음', '좋습니다', '좋았습니다', '맛있어서', '빨리', '먹었습니다', '맛나게', '맛있는', '맛있어요', '빠르고', '감사합니다', '좋네요', '매번', '번창하세요', '최고', '먹었어요']

# 1점 리뷰 키워드
rating1Keywords = ['최악', '별로네요', '맛없어요', '딱딱하고',  '한시간', '어떻게', '아니고', '다시', '이런', '제대로', '이렇게', '다시는', '다신', '거의', '해서', '맛없음', '절대', '없고', '했는데', '없네요', '먹다가', '이제', '이게', '왔네요', '식어서', '전화했더니', '없어요', '제가', '불어서', '별로', '원래', '별', '무슨', '이건', '않고', '하나도', '1시간']

# 리뷰에서 키워드가 몇 번 나왔는지 세주는 함수
def keywordCount(review, keywordList):
    cnt = 0
    for word in review.split():
        if word in keywordList:
            cnt += 1

    return cnt

strangeRating5Review = []
strangeRating1Review = []

# 5점 리뷰 키워드와 1점 리뷰 키워드 비교
for review in rating5:
    rating1keywordCount = 0
    rating5keywordCount = 0
    rating1keywordCount = keywordCount(review, rating1Keywords)
    rating5keywordCount = keywordCount(review, rating5Keywords)
    if (rating1keywordCount > rating5keywordCount) & (rating1keywordCount > 1):
        strangeRating5Review.append(review)

for review in rating1:
    rating1keywordCount = 0
    rating5keywordCount = 0
    rating1keywordCount = keywordCount(review, rating1Keywords)
    rating5keywordCount = keywordCount(review, rating5Keywords)
    if (rating1keywordCount < rating5keywordCount) & (rating5keywordCount > 1):
        strangeRating1Review.append(review)

for review in strangeRating5Review:
    print(review)

print(len(strangeRating5Review), '개의 별점이 5점인 모순된 리뷰를 찾았습니다')

# for review in strangeRating1Review:
#     print(review)

# print(len(strangeRating1Review), '개의 별점이 1점인 모순된 리뷰를 찾았습니다')