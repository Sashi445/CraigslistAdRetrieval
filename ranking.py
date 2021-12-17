import json
from tf_idf import DocumentRanker


# n = int(input('Enter the value of n : '))

# f = open(str(n)+'-gram.json','r')
# ngram = json.load(f)
# f.close()

# print('Use can use * as wildcard query')
# print('Caution use only one * per word 2 or more are not allowed')
query = input('Enter the query:').split(' ')


d = DocumentRanker()

d.set_positional_index()

d.set_word_count()

d.get_idf_values()

# d.create_document_vector_matrix()

d.get_doc_vectors()

coefficients = d.find_similarity_coefficients(query=query)

# print(coefficients)

values = zip(coefficients.keys(), coefficients.values())

results = sorted(values,  key=lambda x : x[1], reverse=True)

<<<<<<< HEAD
print(results)

retrieval = [results[i][0] for i in range(10)]
with open('retrieval.json','w',encoding='utf-8') as f:
    json.dump(retrieval,f,indent=4)
    f.close()
=======
print(results[:10])
>>>>>>> 9dbe787e6362b041720f4fe8f5da319b9c5a2889
