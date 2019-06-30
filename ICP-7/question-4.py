from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier

train_data = fetch_20newsgroups(subset='train', shuffle=True)
test_data = fetch_20newsgroups(subset='test', shuffle=False)

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')

X_train_tfdif = tfidf_vectorizer.fit_transform(train_data.data)
X_test_tfdif = tfidf_vectorizer.transform(test_data.data)

multinomial_nb = MultinomialNB()
multinomial_nb.fit(X_train_tfdif, train_data.target)

prediction = multinomial_nb.predict(X_test_tfdif)

multinomial_nb_score = round(metrics.accuracy_score(test_data.target, prediction), 4)
print("MultinomialNB accuracy is: ", multinomial_nb_score)

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train_tfdif, train_data.target)

knn_score = round(knn.score(X_train_tfdif, train_data.target) * 100, 4)
print("KNN accuracy is: ", knn_score / 100)
