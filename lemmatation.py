#lemmatation is more accurate and smart

import spacy
nlp=spacy.load("en_core_web_sm")
# doc=nlp("eating eats eat ate ajustable rafting ability meeting better manageable")
# for token in doc:
#     print(token,"|",token.lemma_,"|",token.lemma)




ar=nlp.get_pipe('attribute_ruler')
ar.add([[{"TEXT":"Bro"}],[{"TEXT":"Brah"}]],{"LEMMA":"Brother"})
doc2=nlp("Bro , you wanna go? Brah, don't say no!I am exhausted")
for token in doc2:
    print(token.text,"|",token.lemma_)


