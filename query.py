import json

f = open('positional_index.json','r')
index = json.load(f)
f.close()

n = int(input('Enter the value of n :'))

f = open(str(n)+'-gram.json','r')
ngram = json.load(f)
f.close()

print('Use can use * as wildcard query')
print('Caution use only one * per word 2 or more are not allowed')
query = input('Enter the query:').split(' ')           

def merge(n1,n2):
    s1 = set(n1)
    s2 = set(n2)
    return list(s1.intersection(s2))   

def processing(word):
    if n>=len(word):
        return ngram[word]
    else:
        answer = []
        for i in range(0,len(word)-n+1):
            if i==0:
                answer = ngram[word[i:i+n]]
            else:
                answer = merge(answer,ngram[word[i:i+n]])     
        return answer

def wildcard(word):
    if word[-1]=='*':
        w = '$'+word[0:-1]   
        return processing(w)              
    elif word[0]=='*':
        w = word[1:]+'$'
        return processing(w)
    else:
        i = word.find('*')
        w = '$'+word[0:i]  
        w2 = word[i+1:]+'$'
        return merge(processing(w),processing(w2))       

postings = []
queryvector = []
for word in query:
    if '*' in word:
        words = wildcard(word)
        words.sort()
        queryvector.append(words)
        sub_postings=[]
        for w in words:
            sub_postings.append(index[w])
        postings.append(sub_postings)    
    else:
        if word in index.keys():
            queryvector.append(word)
            postings.append(index[word])     

with open('query.json','w',encoding='utf-8') as file:
    json.dump(postings,file,indent=2)
    file.close()      

print("Query Vector :",queryvector) 