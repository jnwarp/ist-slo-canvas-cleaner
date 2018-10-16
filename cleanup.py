'''
eBoard Canvas Cleanup Script
Programmed by James Regan (akr5321)
'''

import pandas as pd

# only read columns printed below
cols = ['Name', 'Points']
df = pd.read_excel('canvas.xlsx', usecols=cols)

# remove students below point value
point_min = 0.5
df = df[df['Points'] >= point_min]

print(df)

# save excel document
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, 'Students')
writer.save()
