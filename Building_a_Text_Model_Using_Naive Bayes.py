from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

volunteer["category_desc"] = volunteer["category_desc"].fillna("None")

le = LabelEncoder()
volunteer["y_category_desc"] = le.fit_transform(volunteer["category_desc"])

y = volunteer["y_category_desc"]
X_train, X_test, y_train, y_test = train_test_split(text_tfidf.toarray(), y, stratify=y)

nb = GaussianNB()
nb.fit(X_train, y_train)

print(nb.score(X_test, y_test))
