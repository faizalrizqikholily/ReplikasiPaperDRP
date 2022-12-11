# %%
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report


# %%
# membuka file data latihan
datas = pd.read_excel("uji.xlsx", sheet_name="labelled")
label = datas['sentiment']
data = datas['content']


# %%
# Pelatihan model
pipe = Pipeline(steps=[('vect', CountVectorizer()),
                        ('tfidf', TfidfTransformer()),
                        ('clf', MultinomialNB())])

tuned_parameters = {
    'vect__ngram_range': [(1, 1), (1, 2), (2, 2)],
    'tfidf__use_idf': (True, False),
    'tfidf__norm': ('l1', 'l2'),
    'clf__alpha': [1, 1e-1, 1e-2]
}


classifier = GridSearchCV(pipe, tuned_parameters, cv=10)
classifier.fit(data, label) # melatih model dengan data latih

# %%
# membuka data uji (131 data)
datas_test = pd.read_excel("uji.xlsx", sheet_name='testing')
data2 = datas_test['content']

# mengetes model menggunakan data uji
prediksi = classifier.predict(data2)
counter = 1; pos = 0; neg = 0; net = 0
for x in prediksi:
    print(f'sentimen data tweet ke-{counter}\n{x}'); counter+=1
    if x == 'Positif' :
        pos+=1
    if x == 'Negatif' :
        neg+=1
    else:
        net+=1

print("\nJumlah masing-masing sentimen setelah diklasifikasikan : ")
print(f"Sentimen Positif : {pos}\nSentimen Netral : {net}\nSentimen Negatif : {neg}")