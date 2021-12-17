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

print(results)