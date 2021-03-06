import json
import math
import os
import os.path

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

class DocumentRanker:

    
    def __init__(self):
        self.DIR = '.\dataset'
        self.total_documents_len = (len([name for name in os.listdir(
            self.DIR) if os.path.isfile(os.path.join(self.DIR, name))]))
        self.positional_index = dict()
        self.idf_values = dict()
        self.document_vectors = list()
        self.word_count = dict()
        self.document_vectors = dict()

    def set_word_count(self):
        with open("./word-count.json", "r", encoding="utf-8") as f:
            self.word_count = json.loads(f.read())
            f.close()

    def set_positional_index(self):
        with open("./positional_index.json", encoding='utf-8') as index:
            self.positional_index = json.loads(index.read())
            index.close()

    def get_idf_values(self):

        temp_idf_vals = dict()

        for key in sorted(self.positional_index.keys()):
            reference = self.positional_index[key]
            occurences = reference['document_count']
            idf = math.log10(self.total_documents_len / occurences)
            temp_idf_vals[key] = idf
        
        # print(json.dumps(temp_idf_vals,sort_keys=True, indent=4))

        self.idf_values = temp_idf_vals
        # return idf_values

    def get_tf_values(self, word):
        word_ref = self.positional_index[word]
        documents = word_ref["documents"]
        tf_values = dict()
        for key in documents.keys():
            doc_ref = documents[key]
            total_words_doc = self.get_word_count(doc_id=key)
            freq = doc_ref["word_count"]
            tf_value = freq / total_words_doc
            tf_values[key] = tf_value
        return tf_values

    def get_tf_idf_from_doc_word(self, word, doc_id):
        
        word_ref = self.positional_index[word]
        
        docs = word_ref['documents']

        if doc_id in docs.keys():
             
             doc_ref = docs[doc_id]

             freq = doc_ref["word_count"]

             total_words = self.get_word_count(doc_id=doc_id)

             tf_value = freq / total_words

             idf_value = math.log10( self.total_documents_len /  word_ref["document_count"] )    

             return tf_value * idf_value

        else:

            return 0

        # documents = word_ref["documents"]
        # print(documents)
        # doc_ref = documents[doc_id]
        # total_words_doc = self.get_word_count(doc_id)
        # freq = doc_ref["word_count"]
        # tf_value = freq / total_words_doc
        # idf_value = math.log10( self.total_documents_len / int(word_ref["document_count"]) )
        # return tf_value * idf_value

    def get_doc_vectors(self):
        
        doc_vectors = dict()

        for doc_id in range(1, 330):
            doc_vector = list()
            for word in sorted(self.positional_index.keys()):
                tf_idf = self.get_tf_idf_from_doc_word(word, str(doc_id))
                doc_vector.append(tf_idf)
            doc_vectors[str(doc_id)] = doc_vector        
        
        self.document_vectors = doc_vectors

        # print(self.document_vectors)

            


    def create_document_vector_matrix(self):
        words = sorted(self.positional_index.keys())
        for doc_id in range(1, self.total_documents_len + 1):
            document_vector = list()
            for word in words:
                tf_values = self.get_tf_values(word)
                if str(doc_id) in tf_values.keys():
                    # multiply by tf-val and idf-value and add value to vector
                    idf_value = self.idf_values[word]
                    tf_value = tf_values[str(doc_id)]
                    document_vector.append(tf_value * idf_value)
                else:
                    # add zero to doc_vector
                    document_vector.append(0)
            # with open(f"document_vectors.txt", "a", encoding="utf-8") as f:
            #     f.write(f"{tuple(document_vector)}\n")
            #     f.close()
            self.document_vectors[str(doc_id)] = tuple(document_vector)

    def get_word_count(self, doc_id):
        return self.word_count[doc_id]

    def get_query_info(self, query):

        query_info = dict()

        for word in query:
            word = word.lower()
            if word in stop_words:
                continue
            else:
                # word = ps.stem(word)
                if word in self.positional_index.keys():
                    if word in query_info.keys():
                        query_info[word] += 1
                    else:
                        query_info[word] = 1
        
        return query_info

    def get_query_vector(self, query):
        query_info = self.get_query_info(query)
        total_length = max(query_info.values())
        query_vector = list()
        for word in sorted(self.positional_index.keys()):
            if word in query_info.keys():
                tf_value = query_info[word] / total_length
                idf_value = self.idf_values[word]
                query_vector.append(tf_value*idf_value)
            else:
                query_vector.append(0)
        return query_vector

    def cosine_similarity(self, query_vector, document_vector):
        value_doc = math.sqrt(sum([ value * value for value in document_vector ]))
        value_vector = math.sqrt(sum([ value * value for value in query_vector ]))

        prod_val = 0

        for value in zip(document_vector, query_vector):
            a , b = value
            prod_val += a * b
        
        return prod_val / ( value_doc + value_vector )
    
    def find_similarity_coefficients(self, query):
        coefficients = dict()
        for doc_id in range(1, self.total_documents_len + 1):
            if str(doc_id) in self.document_vectors.keys():
                document_vector = self.document_vectors[str(doc_id)]
                query_vector = self.get_query_vector(query)
                cosine_similarity = self.cosine_similarity(document_vector=document_vector, query_vector=query_vector)
                coefficients[str(doc_id)] = cosine_similarity
        return coefficients




