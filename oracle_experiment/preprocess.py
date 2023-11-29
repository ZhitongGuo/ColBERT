import pandas as pd

df_all = pd.read_csv('mind2web_all_1031.csv')
df_compressed = pd.read_csv('compressed_mind2web.csv')

df_all = df_all.reset_index()
df_compressed = df_compressed.reset_index()

merged_df = pd.merge(df_compressed, df_all[['index', 'PREVIOUS ACTIONS']], on='index', how='left')

merged_df.drop('index', axis=1, inplace=True)

merged_df.to_csv('updated_compressed_mind2web.csv', index=False)
