import re
string = open('file1.txt').read()
new_str = re.sub('[^a-zA-Z\n\.]', ' ', string)
open('file2.txt', 'w').write(new_str)
