# 별점과 comment가 일치하지 않는 리뷰 찾기 
###### 2023-1 빅데이터 최신기술 중간 프로젝트

#### 20180891 노종빈 (begong313)
#### 20191557 김민제 ()

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

<Br>
https://wikidocs.net/44249 의 코드를 활용하여 감정분석 모델 생성 및 리뷰 재검사


<br>

## sql 구조
#### sql 구조 생성파일은 없으니 직접 생성해서 사용바람
* 현재 sql
    * num (int) : index
    * comment (text ) : 리뷰 내용
    * quantity (tinyInt) : 양 관련 별점 (본 연구에서는 사용 x)
    * delivery (tinyint) : 배달 관련 별점 (본 연구에서는 사용 x)
    * totalRating (tinyint) : 총 별점
    * PosOrNe (tinyint) : 재 검사한 긍정 부정 여부 (1 : 긍정, 0 : 부정 , 2:판단불가)
