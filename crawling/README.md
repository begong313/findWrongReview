# 요기요 api url을 활용한 식당 review crawling



----------
### 특징
#### 두 파일 모두 mysql로 데이터 관리 
#### 데이터 수집과 맞춤법 검사를 동시에 할 수 있으나, 속도를 위해서 따로 분리함.
#### 데이터 수집 및 맞춤법 검사 모두 index를 활용하여 코드가 동작하기에, 병렬로 실행 가능.

-------
## crawlingReview.py
### contributor 
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 노종빈 | 20180891 | begong313 |
<br>

### 리뷰 데이터 크롤링

요기요 리뷰 api url이 식당코드와, pageNum을 인자로 받아 데이터를 전송해줌.
반복문을 활용하여 데이터 수집.
별점과 같은 데이터를 함께 사용하기 위해 sql을 사용하였음.

전처리 : api에서 데이터를 받아올 때 정규식을 이용해 특수문자 제거.

<br>

혹시모를 서버 과부화 방지위해 sleep 적용

## correctorSQL.py
### contributor 
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 노종빈 | 20180891 | begong313 |
<br>

### 리뷰 데이터 맞춤법 검사
#### hanspell 라이브러리 사용 

맞춤법 검사 및 불필요한 공백 제거<br>
sql에 저장된 데이터를 가져와 맞춤법 검사 후 다시 sql에 넣음.<br>
별점과 같은 추가 데이터와 함께 이용하기 위해 sql에 다시 넣음.
<br>

## removeSpace.py
### contributor 
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 김민제 | 20191557 | kevinmj12 |
<br>
리뷰 내에 존재하는 두 칸 이상의 공백을 모두 한 칸으로 바꿈<br>
python의 re모듈을 사용함

<Br>

## removeReply.py
### contributor 
| 이름  | 학번       | gitHub    |
|-----|----------|-----------|
| 김민제 | 20191557 | kevinmj12 |
<br>
리뷰 내에 존재하는 사장님의 답글 삭제<br>
대부분의 사장님의 답글에는 '고객님'이라는 단어가 등장하였고 <br>
'고객님'이 들어간 리뷰는 모두 삭제함


## 모든 리뷰데이터에 관한 권리는 '요기요'에 있습니다.

