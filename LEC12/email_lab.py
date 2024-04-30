import os
os.chdir(r'C:\2022182024\24_3-1_ScriptingLanguage\LEC12')

import csv
f = open('simple.csv')
reader = csv.reader(f, skipinitialspace=True)
for line in reader:
    print(line)
f.close()
