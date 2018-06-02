import os


def load_file(file_path, encoding='ISO-8859-15'):
    t = ''
    try:
        with open(file_path, encoding=encoding) as f:
            for line in f:
                line = line.strip('\n')
                t += line
    except Exception as e:
        print(e)
    return t


def visitDir(path, name='.php'):
    full_files = []
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
            if name in file:
                file_content.append(load_file(file))
                full_files.append(file)
    return file_content, full_files
