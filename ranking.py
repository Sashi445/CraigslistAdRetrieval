import json
from tf_idf import DocumentRanker

query = input('Enter the query:').split(' ')


d = DocumentRanker()

d.set_positional_index()

d.set_word_count()

d.get_idf_values()

d.get_doc_vectors()

coefficients = d.find_similarity_coefficients(query=query)

values = zip(coefficients.keys(), coefficients.values())

results = sorted(values,  key=lambda x : x[1], reverse=True)

print(results)

retrieval = [results[i][0] for i in range(10)]
with open('retrieval.json','w',encoding='utf-8') as f:
    json.dump(retrieval,f,indent=4)
    f.close()
