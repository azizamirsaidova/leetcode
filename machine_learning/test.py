from pyconll import load_from_file
from conllu import parse

data = parse('NER_ALS_Test_no_labels.conll')
print(data)