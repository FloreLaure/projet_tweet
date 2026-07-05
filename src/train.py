import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('data/raw/processed.csv')
X_train,X_test,y_train,y_test=train_test_split(df.clean_message,df.label,test_size=0.2,stratify=df.label,random_state=42)
pipe=Pipeline([('tfidf',TfidfVectorizer(max_features=10000,ngram_range=(1,2))),('clf',LogisticRegression(class_weight='balanced',max_iter=1000))])
X_train = pd.Series(X_train).fillna("")
X_test = pd.Series(X_test).fillna("")
pipe.fit(X_train,y_train)
joblib.dump(pipe,'model.pkl')
model = joblib.load("model.pkl")
print(model.classes_)




