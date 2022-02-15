import os
os.system("py test.py")

with open('./test_input') as test_input_raw:
    test_input = test_input_raw.readlines()

for i in test_input:
    os.system('{}'.format(i.rstrip()))
