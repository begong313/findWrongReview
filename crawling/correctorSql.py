"""
sql에 있는데이터를 가져와 맞춤법 검사 후 다시 반환
별점과 연계하여 데이터를 추출하기 위해 만들었음.
hanspell을 설치해도 실행이 잘 안될 경우, GITHUB에서 hanspell을 받아 폴더를 추가해줘야 함.

REVIEW의 INDEX값을 사용하여 데이터들을 가지고 옮으로 INDEX로 나눠 병렬로 실행 가능.
"""
import pymysql
from hanspell import spell_checker

#db연결 및 데이터 가져오기. 지정한 db명, 테이블이름에 따라 수정
dbcon=pymysql.connect(host='localhost', user='root',password='password',db='dbname', charset='utf8')
cur = dbcon.cursor()
loadingQuery = "select comment from yogiyocomment.reviewdatanew where num=%s"
updateQuery = "UPDATE yogiyocomment.reviewdatanew set comment = %s where num=%s"

#맞춤법 검사기를 돌릴 수 없는 문장("맞춤법검사 결과가 나오지 않는 문장")시  error파일에 기록 =>수동으로 삭제 또는 수정
c = open("errlog.txt","a",encoding="utf-8")

#검사를 시작할 INDEX
i=1
while i <1000000:
    try:
        cur.execute(loadingQuery,i)
        rs = cur.fetchone()

        #혹시모를 comment가 공백인 review 검사
        if rs==None:
            i+=1
            continue

        #맞춤법 검사후 결과 받아오기
        result = spell_checker.check(rs[0])
        result.as_dict()

        #맞춤법 검사가 완료된 comment 다시 탑제
        cur.execute(updateQuery,(result[2],i))
        dbcon.commit()

        print(i)
        i+=1

    except:
        #에러시 로그에 기록 후 다음 문장 검사 실행
        c.writelines("error : "+ str(i)+"\n")
        i+=1
        continue



