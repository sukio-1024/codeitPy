from random import randint

in_file = open('vocabulary.txt', 'r', encoding='utf-8')

vocab = {}
for line in in_file:
    data = line.strip().split(": ")
    vocab[data[1]] = data[0]

keys = list(vocab.keys())

while True:
    index = randint(0, len(keys) - 1)
    korean_word = keys[index]
    english_word = vocab[korean_word]

    vocabulary = input("%s: " %(korean_word))
    if(vocabulary == english_word):
        print("맞았습니다!")
    elif(vocabulary == 'q'):
        break
    else:
        print("틀렸습니다. 정답은 %s입니다." %(english_word))

in_file.close()
