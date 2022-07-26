import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

volunteer = pd.read_csv("volunteer.csv")
print(volunteer["title"].head())

tfidf_vec = TfidfVectorizer()
text_tfidf = tfidf_vec.fit_transform(volunteer["title"])

print(type(text_tfidf))

print(tfidf_vec.get_feature_names()[:30])
