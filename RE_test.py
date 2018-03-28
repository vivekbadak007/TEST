import re
line =['hello world','good morning','heither nil','exit code', ]
lst = []
for li in line:
    lst_1 = re.findall('^h',li)
    if len(lst_1) != 0:
        lst.append(li)
print lst