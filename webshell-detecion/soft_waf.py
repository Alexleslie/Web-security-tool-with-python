import os
from sklearn.feature_extraction.text import CountVectorizer
import sys
import numpy as np
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

pattern = r'\b\w+\b\(|\'\w+\''

full_files = []


def load_file(file_path):
    t = ''
    with open(file_path) as f:
        for line in f:
            line = line.strip('\n')
            t += line
    return t


def visitDir(path):
    file_content = []
    if not os.path.isdir(path):
        print('ERROR:', path, 'is not a directory or does not exist')
        return
    list_dirs = os.walk(path)

    for root, dirs, files in list_dirs:
        # for d in dirs:
        #     print(os.path.join(root, d))
        for f in files:
            file = os.path.join(root, f)
            if 'php' in file:
                file_content.append(load_file(file))
                full_files.append(file)
    return file_content


webshell_bigram = CountVectorizer(ngram_range=(1, 1), decode_error='ignore',
                                  token_pattern=pattern, min_df=1)


file_content_1 = visitDir('data/wordpress')
file_content_2 = visitDir('data/PHP-WEBSHELL/xiaoma/')
yGood = [1 for _ in range(0, len(file_content_1))]
yBad = [0 for _ in range(0, len(file_content_2))]

y = yGood + yBad
webshell_files_content = file_content_1 + file_content_2

X = webshell_bigram.fit_transform(webshell_files_content)

X_train, X_test, y_train, y_test = train_test_split(X, y)


from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

clf.fit(X_train, y_train)
clf.score(X_test, y_test)




