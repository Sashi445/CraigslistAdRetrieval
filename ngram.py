import os
import re 
import json

os.chdir('corpus')

file = open('corpus.txt','r',encoding='utf-8')
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',file.read())
file.close()

for i in range(0,len(sentences)):
    sentence = sentences[i].lower()
    sentence = re.sub(r'\W',' ',sentence)        # removing non-word symbols
    sentence = re.sub(r'\s+',' ',sentence)       # replacing extra spaces with single space
    sentence = sentence.strip()
    sentences[i] = sentence

n = int(input('Enter the value of n : '))

print(sentences)

index = {}
for sentence in sentences:
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

os.chdir('..')

with open(str(n)+'_gram.json','w',encoding='utf-8') as file:
    json.dump(index,file,indent=4)
    file.close()    

print('No of grams in the corpus {}'.format(len(index)))
