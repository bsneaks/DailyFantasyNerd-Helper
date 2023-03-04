import os
import re
import pandas as pd

os.chdir(os.path.expanduser('~/Downloads'))
new_row_columns = ['PG', 'PG.1', 'SG', 'SG.1', 'SF', 'SF.1', 'PF', 'PF.1', 'C']

with open('DAILYFANTASYNERD-NBA.csv', 'r') as file:
    content = file.read()
with open('DAILYFANTASYNERD-NBA.csv', 'w') as file:
    file.write(','.join(new_row_columns) + '\n' + content)
    file.seek(0)

df1 = pd.read_csv("FANDUEL-NBA.csv")
df2 = pd.read_csv("DAILYFANTASYNERD-NBA.csv")

cell_value = df1.loc[10, 'Instructions']
pattern = r'(\d{5})-\d{4}'
first_five_digits = re.search(pattern, cell_value).group(1)

columns_to_append = ['PG', 'PG.1', 'SG', 'SG.1', 'SF', 'SF.1', 'PF', 'PF.1', 'C']
for col in columns_to_append:
    df2[col] = df2[col].apply(lambda x: first_five_digits + '-' + str(x) if isinstance(x, (int, float)) and not pd.isna(x) else x)

new_columns = ['PG', 'PG', 'SG', 'SG', 'SF', 'SF', 'PF', 'PF', 'C']
df2.columns = new_columns

df2.to_csv("DAILYFANTASYNERD-NBA.csv", index=False)

#Uncomment this section if you want to copy the values back into the Fanduel Spreadsheet...although you can simply upload the updated DAILYFANTASYNERD-NBA.csv"
#df1.loc[0:24, ['PG', 'PG.1', 'SG', 'SG.1', 'SF', 'SF.1', 'PF', 'PF.1', 'C']] = df2.loc[0:24, ['PG', 'PG.1', 'SG', 'SG.1', 'SF', 'SF.1', 'PF', 'PF.1', 'C']]
#df1.to_csv("FANDUEL_NBA.csv", index=False)


