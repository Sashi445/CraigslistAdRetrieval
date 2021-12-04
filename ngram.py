import os
import re 
import json

os.chdir('corpus')

index = {}
words = {}

n = int(input('Enter the value of n : '))

for file in os.listdir():
    f = open(file,'r',encoding='utf-8')  
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',f.read())
    f.close()

    for sentence in sentences:
        sentence = sentence.lower()
        sentence = re.sub(r'\W',' ',sentence)        # removing non-word symbols
        sentence = re.sub(r'\s+',' ',sentence)       # replacing extra spaces with single space
        sentence = sentence.strip()

        # n-gram index
        if n > len(sentence):
            if sentence in index.keys():
                index[sentence]+=1
            else:
                index[sentence]=1
        else:
            for j in range(0,len(sentence)-n):
                gram = ''.join(sentence[j:j+n])
                if gram in index.keys():
                    index[gram]+=1
                else:
                    index[gram]=1 

        # word-count index
        for word in sentence.split(' '):
            if word!=' ' and word!='':
                if word not in words.keys():
                    words[word]=1
                else:
                    words[word]+=1
    
os.chdir('..')

with open(str(n)+'-gram.json','w',encoding='utf-8') as file:
    json.dump(index,file,indent=4)
    file.close()   

with open('word-count.json','w',encoding='utf-8') as file:
    json.dump(words,file,indent=4)
    file.close()

print('no.of words in the corpus {}'.format(len(words)))
print('No of grams in the corpus {}'.format(len(index)))
