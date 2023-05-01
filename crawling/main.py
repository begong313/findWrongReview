import time
import requests
import pymysql
import re

#db연결
dbcon=pymysql.connect(host='localhost', user='root',password='!shwhdqls12',db='yogiyocomment', charset='utf8')
cur = dbcon.cursor()

restaurantNum = 1
#10000까지 돌려보기

while restaurantNum<30500:
    try:
        page = 1
        print(restaurantNum)
        while 1:
            # 요기요 댓글 api url
            url ="https://www.yogiyo.co.kr/api/v1/reviews/%s/?count=10&only_photo_review=false&page=%s&sort=time"%(restaurantNum,page)
            response = requests.get(url)
            jsonData = response.json()

            #페이지에 아무 정보없으면 break
            if len(jsonData)==0:
                break

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

                sql = "insert into reviewdata (comment, totalRating, taste, quantity, delivery) values (%s, %s,%s, %s, %s)"
                val = (comment, totalRating,taste, quantity, delivery)
                cur.execute(sql, val)
            page +=1
            time.sleep(0.1)

        dbcon.commit()
        #식당고유번호 1 증가
        restaurantNum += 1
        time.sleep(0.1)
    except:
        restaurantNum += 1
