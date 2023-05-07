file1 = 'comments_TF_IDF.txt'
file2 = 'comments_rating1_TF_IDF.txt'
with open(file1, 'r', encoding='utf-8') as openFile1:
    textFile1 = openFile1.readlines()
openFile1.close()
with open(file2, 'r', encoding='utf-8') as openFile2:
    textFile2 = openFile2.readlines()

totalKeywords = []
rate1Keywords = []
for i in range(100):
    totalKeywords.append(textFile1[i].split(',')[0][2:-1])
    rate1Keywords.append(textFile2[i].split(',')[0][2:-1])

setTotalKeywords = set(totalKeywords)
setRate1Keywords = set(rate1Keywords)
print(textFile2[0])

# 교집합, 차집합을 통해 개선된 키워드 추출
advancedKeywords = setTotalKeywords & setRate1Keywords
advancedRate5Keywords = setTotalKeywords - setRate1Keywords
advancedRate1Keywords = setRate1Keywords - setTotalKeywords


print("advancedKeywords: ", advancedKeywords)
print("advancedRate5Keywords: ",advancedRate5Keywords)
print("advancedRate1Keywords: ",advancedRate1Keywords)


