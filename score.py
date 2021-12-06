import math
import json

def logtf(posting):
    res = 1 + math.log(posting['word_count'])
    return round(res,3)

f = open('query.json','r')
postings = json.load(f)
f.close() 

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


