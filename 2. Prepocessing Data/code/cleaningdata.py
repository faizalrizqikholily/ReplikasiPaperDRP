import matplotlib.pyplot as plt
import pandas as pd
import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import pandas as pd

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
path = "crawl1.xlsx"

# membaca file hasil crawling
df = pd.read_excel(path, sheet_name='before')
df2 = pd.read_excel(path, sheet_name='after')
datas = df['content'].tolist()
datas.extend(df2['content'].tolist())

def preprocess(text):
    # mengecilkan huruf
    text = (text).lower()  #     
    text = re.sub(r"\d+", "", text) #menghapus angka

    # menghilangkan simbol dan tanda baca
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split()) 

    # menghilangkan stopwords
    text = stopword.remove(text)

    return text


data = [preprocess(t) for t in datas]
data = [*set(data)]

excel_data = {
    'content' : data, 'sentiment':''
}

df = pd.DataFrame(excel_data)

df.to_excel('prepocessing.xlsx', index=False)