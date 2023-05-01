"""
txt파일을 불러와 hansel lib을 이용해 맞춤법 검사후 , 새로운 txt파일에 쓰기


"""


from hanspell import spell_checker

f=open("dot.txt",'r',encoding="utf8")
txt=f.readlines()
f.close()


c = open("correct.txt","a",encoding="utf-8")
newText = []
inn=0
for i in range(902133,len(txt)//2,1):
    if txt[i] == "\n" or txt[i] == "\r" or txt[i] == "\r\n":
        continue
    result = spell_checker.check(txt[i])
    result.as_dict()  # dict로 출력
    newText.append(result[2]+'\r\n')
    if len(newText)==10000:
        c.write(newText)
        newText.clear()
    c.writelines("error : "+ str(i)+"\n")
    inn+=1
