# 별점과 comment가 일치하지 않는 리뷰 찾기 
###### 2023-1 빅데이터 최신기술 중간 프로젝트

#### 20180891 노종빈 (begong313)
#### 20191557 김민제 (kevinmj12)

<br>

## crawling
### contributor 
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 노종빈 | 20180891 | begong313 |

<Br>

요기요 api url을 사용해 리뷰 크롤링
###### 리뷰에 대한 모든 권리는 '요기요'에 있습니다.
크롤링한 데이터를 mysql db에 넣어 보관<br>
hanspell 라이브러리를 이용하여 맞춤법검사 및 전처리

<BR>

## findWrongReivewBySentimentAnalysis
### contributor 
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 노종빈 | 20180891 | begong313 |
| 김민제 | 20191557 | kevinmj12 |

<Br>
https://wikidocs.net/44249 의 코드를 활용하여 감정분석 모델 생성 및 리뷰 재검사


<br>

<Br>

## findWrodReviewByTFIDF
### contributor
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 김민제 | 20191557 | kevinmj12 |

<Br>
TF-IDF를 통한 키워드 추출 및 활용을 통한 모순된 리뷰 검사


