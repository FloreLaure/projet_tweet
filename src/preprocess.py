import pandas as pd, re, nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords'); nltk.download('wordnet')
stop=set(stopwords.words('english')); lem=WordNetLemmatizer()
df=pd.read_csv('data/raw/tweets_suspect.csv')
df=df.drop_duplicates().dropna()
def clean(t):
 t=str(t).lower()
 t=re.sub(r'http\S+|www\S+','',t)
 t=re.sub(r'@\w+','',t)
 t=re.sub(r'[^a-zA-Z\s]',' ',t)
 return ' '.join(lem.lemmatize(w) for w in t.split() if w not in stop)
df['clean_message']=df['message'].apply(clean)
df.to_csv('data/raw/processed.csv',index=False)
