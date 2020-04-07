def convertator(file_path):
    with open(file_path, 'rb') as open_file:
        content = open_file.read()
    content = content.replace(b'\n', b'\r\n')
    with open(file_path, 'wb') as open_file:
        open_file.write(content)
        
        
        
convertator('/Users/romafurman/Semester2/programing/L3_255909/file2.txt')