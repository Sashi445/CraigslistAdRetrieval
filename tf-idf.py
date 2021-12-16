import json
import math

def func():
    with open("./positional_index.json", encoding='utf-8') as index :
        print(json.loads(index.read()))
        index.close()

def document_vector():
    pass

def tf():
    pass

def idf(total_docs, docs_present):
    # pass
    return math.log(total_docs/docs_present)

func()







