filename = 'comments_rating5_spaceremove.txt'

outputFilename = 'comments_rating5_preprocessing.txt'
with open(filename, 'r', encoding='utf-8') as input_file:
    input_text = input_file.readlines()

output_text = []
# 사장님 댓글 삭제
for line in input_text:
    if '고객님' in line: # 사장님의 답글이 달린 경우 '고객님'이 포함되는 경우가 대부분임
        pass
    else:
        output_text.append(line)


# 수정된 내용을 파일에 작성.
with open(outputFilename, 'w', encoding='utf-8') as output_file:
    for line in output_text:
        output_file.write(line)

input_file.close()
output_file.close()
