out_file = open('vocabulary.txt', 'w', encoding="utf-8")

engVoca = ''

while(True):
    engVoca = input("영어 단어를 입력하세요: ")
    if (engVoca == 'q'):
        break
    korVoca = input("한국어 뜻을 입력하세요: ")
    out_file.write("%s: %s\n" %(engVoca, korVoca))

out_file.close()