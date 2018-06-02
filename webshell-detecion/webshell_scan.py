from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from FileTravel import visitDir



webshell_vectorizer = joblib.load('AndShell_dict.m')
clf = joblib.load('AndShell_scan.m')

path = input('[+] Please input a path')

file_content, full_files = visitDir(path, '.php')

X = webshell_vectorizer.transform(file_content)

for i in X:
    result = clf.predict(i)
    print(result)
    if result == 1:
        print('this file is good')
    else:
        print('bad')

