import json
import math
import os
import os.path

DIR = '.\dataset'


class DocumentVector:

    def __init__(self):
        self.total_documents_len = (len([name for name in os.listdir(
            DIR) if os.path.isfile(os.path.join(DIR, name))]))
        self.positional_index = dict()
        self.idf_values = list()
        self.document_vectors = list()

    def set_positional_index(self):
        with open("./positional_index.json", encoding='utf-8') as index:
            self.positional_index = json.loads(index.read())
            index.close()

    def get_idf_values(self):

        temp_idf_vals = list()

        for key in sorted(self.positional_index.keys()):
            reference = self.positional_index[key]
            occurences = reference['document_count']
            idf = math.log10(self.total_documents_len / occurences)
            temp_idf_vals.append(idf)
        
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

    def create_document_matrix(self):
        words = sorted(self.positional_index.keys())
        for doc_id in range(1, self.total_documents_len + 1):
            document_vector = list()
            for word in words:
                tf_values = self.get_tf_values(word)
                if str(doc_id) in tf_values.keys():
                    # multiply by tf-val and idf-value and add value to vector
                    idf_value = self.idf_values[int(doc_id) - 1]
                    tf_value = tf_values[str(doc_id)]
                    document_vector.append(tf_value * idf_value)
                else:
                    # add zero to doc_vector
                    document_vector.append(0)
            with open(f"document_vectors.txt", "a", encoding="utf-8") as f:
                f.write(f"{tuple(document_vector)}\n")
                f.close()

            # self.document_vectors.append(tuple(document_vector))

    def get_word_count(self, doc_id):
        word_count = 0
        with open(f".\dataset\{doc_id}.txt", "r", encoding="utf-8") as f:
            file_string = f.read()
            word_count = len(file_string.split(" "))
            f.close()
        return word_count


d = DocumentVector()

d.set_positional_index()

d.get_idf_values()

d.create_document_matrix()


# def document_vector():
#     pass

# def tf():
#     pass

# def idf(total_docs, docs_present):
#     # pass
#     return math.log(total_docs/docs_present)

# func()
