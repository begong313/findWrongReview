import numpy as np
import math

# TF
# filename = 'comments_preprocessing_400.txt'
filename = 'comments_rating1_preprocessing.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
words = text.split()
dic = dict()
file.close()

# 단어가 있으면 +1, 없으면 추가
for word in words:
    try: dic[word] +=1
    except: dic[word] = 1

print(len(dic), "words count comeplete!")

# 단어 등장 횟수별로 정렬
TFList = sorted(dic.items(), key=lambda x: x[1], reverse=True)

# TF를 txt 파일로 저장
# outputFile = "comments_TF.txt"
# with open(outputFile, 'w', encoding='utf-8') as TF_output_write:
#     for each in TFList:
#         TF_output_write.write(str(each))
# TF_output_write.close()

print("Complete calculating TF!")


# DF
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
file.close()
D = len(lines)

DFList = [0]*100
for line in lines:
    for i in range(100):
        if TFList[i][0] in line:
            DFList[i] += 1

# DF를 txt파일로 저장
# outputFile = "comments_DF.txt"
# with open(outputFile, 'w', encoding='utf-8') as DF_output_write:
#     tmp = 0
#     for each in DFList:
#         DF_output_write.write(TFList[tmp][0] + ', ' + str(each) + '\n')
#         tmp += 1
# DF_output_write.close()

print("Complete calculating DF!")

# IDF
IDFList = []
for DF in DFList:
    IDFList.append(np.log(D/(1+DF)))

# TF-IDF
TF_IDF = []
for i in range(100):
    TF_IDF.append([TFList[i][0], TFList[i][1] * IDFList[0]])

# 정규화
total = 0
for i in range(100):
    total += (TF_IDF[i][1] * TF_IDF[i][1])
tfidfNorm = math.sqrt(total)

for i in range(100):
    TF_IDF[i][1] /= tfidfNorm

TF_IDF.sort(key=lambda x: x[1], reverse=True)
print("TF_IDF: ", TF_IDF)

# TF-IDF를 txt파일로 저장
# outputFile = "comments_rating1_TF_IDF.txt"
# with open(outputFile, 'w', encoding='utf-8') as TF_IDF_output_write:
#     for each in TF_IDF:
#         TF_IDF_output_write.write(str(each)+', \n')
# TF_IDF_output_write.close()
