from os import listdir
from os.path import isfile, join
import json
from os import getcwd, path
import re

pattern = re.compile(r'''(?x)       # set flag to allow verbose regexps
	        ([A-Z]\.)+              # abbreviations
        |   [\$|Rs]?\d+(\.\d+)?%?   # currency and percentages,
        |   \w+                     # words 
 ''',re.VERBOSE | re.I)

class PostingListItem:
    def __init__(self, doc_id, freq) -> None:
        self.doc_id = doc_id
        self.freq = freq

    def __str__(self) -> str:
        return f"({self.doc_id},{self.freq})"

class InvertedIndexer:
    
    def __init__(self) -> None:
        self.posting = dict()


    def process_word(self, word):
        return word
    

    def process_file(self, file_name, file_content):
        print(f"Processing file {file_name}...")
        document_term_map = dict()
        # words = file_content.split(" ")
        words = pattern.finditer(file_content)

        for word in words:
            word = self.process_word(word)

            if word in document_term_map.keys():
                document_term_map[word] += 1
            else:
                document_term_map[word] = 1
        
        for item in document_term_map.items():
            term, freq = item
            posting_list_item = PostingListItem(file_name, freq)
            if term in self.posting.keys():
                self.posting[term].append(posting_list_item)
            else:
                self.posting[term] = list([posting_list_item])


    def index_directory(self, dir_path):
        files = [ f for f in listdir(dir_path) if isfile(join(dir_path, f))]
        print(f"Processing directory {dir_path}")
        print(f"{len(files)} found")
        index = 0
        for f in files:
            index += 1
            file_content = open(join(dir_path, f), encoding='utf-8')

            self.process_file(index, file_content.read())
    
    def export_index(self, output_file_name="Assign012019123-output"):
        print(f"Exporting results to {output_file_name}.txt....")
        for item in list(self.posting.items()):
            key, value  = item
            output_string = f"{key} : "
            posting_list = "".join([f"{str(posting_item.doc_id)}," for posting_item in value])
            output_string += f"( {len(value)} , [{posting_list}])\n" 
            with open(f"{output_file_name}.txt", 'a', encoding="utf-8") as f:
                f.write(output_string)

    
    # exporting to json so that reading the file becomes easy 
    # No need to process strings again while reading posting from file again
    def export_index_json(self, output_file_name="Assign012019123-output"):
        print(f"Exporting results to {output_file_name}.json....")
        serializable_posting = dict()

        for item in self.posting.items():
            key, value = item
            posting_items = [posting_item.doc_id for posting_item in value]
            serializable_posting[key] = {
                'count' : len(value),
                'docs' : posting_items,
            }

        json_object = json.dumps(serializable_posting)
        with open(f"{output_file_name}.json", 'a', encoding="utf-8") as f:
            f.write(json_object)
        

    # Optional
    # These two methods export frequency of the word as well
    def export_results(self, output_file_name="output"):
        print(f"Exporting results to {output_file_name}.txt....")
        for item in list(self.posting.items()):
            key, value  = item
            output_string = f"[{key}] : "
            output_string += "".join([f"{str(posting_item)}," for posting_item in value])
            with open(f"{output_file_name}.txt", 'a', encoding="utf-8") as f:
                f.write(output_string)


    def export_json(self, output_file_name="output"):
        print(f"Exporting results to {output_file_name}.json....")
        serializable_posting = dict()

        for item in self.posting.items():
            key, value = item
            posting_items = [str(posting_item) for posting_item in value]
            serializable_posting[key] = posting_items

        json_object = json.dumps(serializable_posting)
        with open(f"{output_file_name}.json", "w", encoding='utf-8') as output:
            output.write(json_object)
        

    def print_posting(self):

        for item in list(self.posting.items())[:10]:
            key, value = item
            print(f"{key} : ", end="")
            list_items = "".join(f"{str(posting_item)},"  for posting_item in value)
            print(list_items)

    def process_string_from_input(self, value):
        terms = value.split(",")
        doc_id = terms[0][1:]
        freq = terms[0][:-2]
        return tuple(int(doc_id), int(freq))
            



MY_PATH = path.abspath(getcwd()) + "\dataset"

inverted_indexer = InvertedIndexer()
inverted_indexer.index_directory(dir_path=MY_PATH)

inverted_indexer.export_index()
inverted_indexer.export_index_json()