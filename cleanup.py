'''
eBoard Canvas Cleanup Script
Programmed by James Regan (akr5321)
'''

import pandas as pd

# only read columns printed below
cols = ['Student', 'Current Points', 'Final Points']
df = pd.read_excel('Test data.xlsx', usecols=cols)

# drop first row (with read only tags)
df = df.drop([0], axis=0)

# remove students below point value
point_min = 0.5
df = df[df['Final Points'] >= point_min]

print(df)

# save excel document
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, 'Students')
writer.save()
