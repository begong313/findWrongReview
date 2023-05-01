"""
요기요 review api url을 활용해 반복문으로 리뷰를 크롤링함.
요기요 리뷰는 json의 형태로 넘어오며, comment,별점등의 정보 이외에도 많은 정보가 있음.
현재의 코드는 데이터 중, 각종별점과 comment만 추출함

"""


import time
import requests
import pymysql
import re

#db연결
#user,password,db의 값 수정해서 사용바람
dbcon=pymysql.connect(host='localhost', user='root',password='password',db='dbname', charset='utf8')
cur = dbcon.cursor()

#api url에 들어가는 식당 고유번호, 고유번호에 해당되는 식당이 없을 수 있음.
restaurantNum = 1

#임시로 횟수 제한, 무한반복으로 원하는 만큼 데이터 추출가능.
while restaurantNum<30500:
    try:
        page = 1
        #어디까지 진행되었는지 확인하기 위함
        print(restaurantNum)


        while 1:
            # 요기요 댓글 api url
            # 리뷰가 한페이지에 10개씩 존재, 리뷰가 더이상 없다면 json객체가 빈 객체로 넘어옴.
            url ="https://www.yogiyo.co.kr/api/v1/reviews/%s/?count=10&only_photo_review=false&page=%s&sort=time"%(restaurantNum,page)
            response = requests.get(url)
            jsonData = response.json()

            #페이지에 아무 정보없으면 break
            if len(jsonData)==0:
                break

            #반복문으로 필요한 데이터만 추출.
            for i in range(len(jsonData)):
                #특수문자 제거
                comment = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", str(jsonData[i]['comment']))
                comment = comment.replace("\n"," ")
                comment = comment.replace('\r',"")
                totalRating = int(jsonData[i]['rating'])
                taste = int(jsonData[i]['rating_taste'])
                quantity = int(jsonData[i]['rating_quantity'])
                delivery = int(jsonData[i]['rating_delivery'])
                print(comment, totalRating, delivery, taste)

                #EXECUTE 하는 코드
                sql = "insert into reviewdata (comment, totalRating, taste, quantity, delivery) values (%s, %s,%s, %s, %s)"
                val = (comment, totalRating,taste, quantity, delivery)
                cur.execute(sql, val)

            #페이지 변환
            page +=1

            #혹시모를 서버 과부하를 막기위해 넣어 둔 코드.
            time.sleep(0.1)

        #해당 식당의 리뷰가 더이상 존재하지 않을 때 DB에 반영
        dbcon.commit()

        #식당고유번호 1 증가
        restaurantNum += 1

        #혹시모를 서버 과부하 방지
        time.sleep(0.1)
    except:
        restaurantNum += 1
