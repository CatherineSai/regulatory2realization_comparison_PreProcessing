
from spacy.matcher import Matcher


class PreProcessing:
  def __init__(self, nlp):
    self.nlp = nlp

  def get_relevant_paragraphs(self, paragraphsraw):  
    '''transferes paragraphs to list and cleans them
    Input: Dictionary or Paragraphs
    Output: List of Paragraphs'''
    paragraphs_list = []
    cleaned_paragraphs_list = []
    for paraid, paragraph in paragraphsraw.items():
        paragraphs_list.append(paragraph)
    for para in paragraphs_list:
        new_para = para.replace(";", ".") #in reg there are many ; which should be counted as seperate senteces
        new_para = new_para.replace("or\n\n\n", "")
        new_para = new_para.replace("or\n\n", "")
        new_para = new_para.replace("and\n\n\n", "")
        new_para = new_para.replace("and\n\n", "")
        new_para = new_para.replace("\n\n\n", "")
        new_para = new_para.replace("\n\n", "")
        cleaned_paragraphs_list.append(new_para) 
    return cleaned_paragraphs_list 

  def apply_anaphora_resolution(self, paragraphsraw):
    '''replaces mentions like "that", "it", "he" with the corresponding subject - needed as the text will be split into sentences and reviewed individually'''
    cleaned_paragraphs_list = self.get_relevant_paragraphs(paragraphsraw) 
    cleaned_paragraphs_list2 = []
    for para in cleaned_paragraphs_list:
        doc = self.nlp(para)
        new_para = para.replace(para, doc._.coref_resolved)
        cleaned_paragraphs_list2.append(new_para) 
    return cleaned_paragraphs_list2