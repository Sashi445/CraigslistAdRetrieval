import json

f = open('positional_index.json','r')
index = json.load(f)
f.close()

query = input('Enter the query:').split(' ')

postings = []
for word in query:
    if word in index.keys():
        postings.append(index[word]) 

with open('query.json','w',encoding='utf-8') as file:
    json.dump(postings,file,indent=2)
    file.close()        