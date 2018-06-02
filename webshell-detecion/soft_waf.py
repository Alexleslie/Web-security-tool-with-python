from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from FileTravel import visitDir

pattern = r'\b\w+\b\(|\'\w+\''


webshell_bigram = CountVectorizer(ngram_range=(1, 1), decode_error='ignore',
                                  token_pattern=pattern, min_df=1)

webshell_tdf = TfidfVectorizer(ngram_range=(1, 2), decode_error='ignore',analyzer='char',sublinear_tf='True',
                               token_pattern=pattern, min_df=0.0)


file_content_1, _ = visitDir('data/good/', '.php')[:730]
file_content_2, _ = visitDir('data/bad/', '.php')[:730]
yGood = [1 for _ in range(0, len(file_content_1))]
yBad = [0 for _ in range(0, len(file_content_2))]
print(len(yBad))
y = yGood + yBad
webshell_files_content = file_content_1 + file_content_2

webshell_tdf.fit(webshell_files_content)
# joblib.dump(webshell_tdf, 'AndShell_dict.m')

X = webshell_tdf.transform(webshell_files_content)

X_train, X_test, y_train, y_test = train_test_split(X, y)


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

clf.fit(X, y)
# joblib.dump(clf, 'AndShell_scan.m', )

acc = clf.score(X_test, y_test)
print(y_test)
print(acc)



