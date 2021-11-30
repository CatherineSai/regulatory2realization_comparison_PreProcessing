# general imports
import os
import spacy
import re
import neuralcoref
import pickle
# own path/ class imports
from file_paths import *
from preprocessing import *

# Create the nlp object
nlp = spacy.load('en_core_web_lg')
neuralcoref.add_to_pipe(nlp)

## parse documents ############################################ START
def read_documents(directory): 
  '''reads in txts of regulatory and realization documents
  Input: multiple .txt (each a document article)
  Output: dictionary with article name as key and article text as value'''
  doc_dict = dict()
  files = os.listdir(directory)
  try:
    for fi in files:
        if fi.endswith('.txt'):
          with open(directory+'/'+fi,'r') as f:
              doc_dict[re.sub('\.txt', '', fi)] = f.read()
  except FileNotFoundError:
    print("Wrong file or file path to dir. Check config file.")
    quit()
  return doc_dict

reg_paragraphs = read_documents(ISO_REGULATION_INPUT_DIRECTORY) 
rea_paragraphs = read_documents(ISO_REALIZATION_INPUT_DIRECTORY) 

################################################################# END


## calling class ############################################ START

#Text cleaning
pp = PreProcessing(nlp)
reg_anaphora_resolved_paragraphs = pp.apply_anaphora_resolution(reg_paragraphs)
rea_anaphora_resolved_paragraphs = pp.apply_anaphora_resolution(rea_paragraphs)
# save to pickle and read in main script (which runs with python 3.9 and spacy 3)
with open(join(RESULT_DIRECTORY,"iso_reg_para_anaphora_resolved.txt"), "wb") as fp:  
  pickle.dump(reg_anaphora_resolved_paragraphs, fp)
with open(join(RESULT_DIRECTORY,"iso_rea_para_anaphora_resolved.txt"), "wb") as fp:  
  pickle.dump(rea_anaphora_resolved_paragraphs, fp)


