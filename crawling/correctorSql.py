"""
sql에 있는데이터를 가져와 맞춤법 검사 후 다시 반환
별점과 연계하여 데이터를 추출하기 위해 만들었음.
"""


import pymysql
from hanspell import spell_checker


dbcon=pymysql.connect(host='localhost', user='root',password='!shwhdqls12',db='yogiyocomment', charset='utf8')
cur = dbcon.cursor()
loadingQuery = "select comment from yogiyocomment.reviewdatanew where num=%s"
updateQuery = "UPDATE yogiyocomment.reviewdatanew set comment = %s where num=%s"

c = open("errlog.txt","a",encoding="utf-8")

i=179588
while i <1000000:
    try:
        cur.execute(loadingQuery,i)
        rs = cur.fetchone()
        if rs==None:
            i+=1
            continue

        result = spell_checker.check(rs[0])
        result.as_dict()

        cur.execute(updateQuery,(result[2],i))
        dbcon.commit()

        print(i)
        i+=1
    except:
        #에러시 그부분 다시실행
        c.writelines("error : "+ str(i)+"\n")
        i+=1
        continue



