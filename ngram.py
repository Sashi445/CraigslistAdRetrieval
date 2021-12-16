import os
import re 
import json

os.chdir('dataset')

index = {}

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

        for word in sentence.split(' '):
            if word!=' ' and word!='':
                word = '$'+word+'$'
                if n >= len(word):
                    if word not in index.keys():
                        index[word] = [word[1:-1]]
                    else:
                        if word not in index[word]:
                            index[word].append(word[1:-1])
                else:
                    for i in range(len(word)-n+1):
                        if word[i:i+n] not in index.keys():
                            index[word[i:i+n]] = [word[1:-1]]
                        else:
                            if word not in index[word[i:i+n]]:
                                index[word[i:i+n]].append(word[1:-1])           
    
os.chdir('..')

with open(str(n)+'-gram.json','w',encoding='utf-8') as file:
    json.dump(index,file,indent=4)
    file.close()   

print('No of grams in the corpus {}'.format(len(index)))
