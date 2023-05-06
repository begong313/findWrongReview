import re

filename = 'comments_rating5.txt'

outputFilename = 'comments_rating5_spaceremove.txt'
with open(filename, 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# 공백 제거 및 띄어쓰기 수정
output_text = re.sub(r' {2,}', ' ', input_text)


# 수정된 내용을 파일에 작성.
with open(outputFilename, 'w', encoding='utf-8') as output_file:
    
    output_file.write(output_text)

input_file.close()
output_file.close()

