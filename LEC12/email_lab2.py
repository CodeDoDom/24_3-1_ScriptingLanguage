import os
os.chdir(r'C:\2022182024\24_3-1_ScriptingLanguage\LEC12')

import csv
f = open('oscar_age_female.csv')
reader = csv.DictReader(f, skipinitialspace=True)
for line in reader:
    print(line)
f.close()
