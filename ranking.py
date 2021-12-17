import json
from tf_idf import DocumentRanker


n = int(input('Enter the value of n : '))

f = open(str(n)+'-gram.json','r')
ngram = json.load(f)
f.close()

print('Use can use * as wildcard query')
print('Caution use only one * per word 2 or more are not allowed')
query = input('Enter the query:').split(' ')


d = DocumentRanker()

d.set_positional_index()

d.set_word_count()

d.get_idf_values()

