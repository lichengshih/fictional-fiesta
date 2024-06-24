import pandas as pd

file_path = '‪Users/Li Cheng/Desktop/PC Vendors Shipments.xlsx'
data = pd.read_excel(file_path, sheet_name='工作表1')

df_long = pd.melt(data, id_vars=['Company'], var_name='Quarter', value_name='Shipments')

df_long['Year'] = df_long['Quarter'].str.extract(r'(\d{4})').astype(int)
df_long['Quarter_Number'] = df_long['Quarter'].str.extract(r'Q(\d)').astype(int)

df_long['Quarter_Start'] = pd.to_datetime(df_long['Year'].astype(str) + '-' + (df_long['Quarter_Number']*3-2).astype(str) + '-01')

output_path = 'Users/Li Cheng/Desktop/PC_Vendors_Shipments_Long_Format.csv'
df_long.to_csv(output_path, index=False)

df_long.head()
