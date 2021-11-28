import math
import json

def logtf(posting):
    res = 1 + math.log(posting['word_count'])
    return round(res,3)

f = open('positional_index.json')
index = json.load(f)
f.close()

query = input('Enter the query:').split(' ')

postings = []
for word in query:
    if word in index.keys():
        postings.append(index[word]) 

documents = dict()

for posting in postings:
    for key in posting['documents'].keys():
        if key in documents.keys():
            documents[key]+=logtf(posting['documents'][key])
        else:
            documents[key]=logtf(posting['documents'][key])

retrieval = []
for i in sorted(documents.items(),key = lambda x:x[1],reverse=True):
    retrieval.append(i[0])

print(retrieval)


