import json
import pandas as pd
import matplotlib.pyplot as plt

# pandasのread_jsonでndjson読み込み
df = pd.read_json('prefecture.ndjson', lines=True)

# 東京(13)のデータ抽出
df_tokyo = df[df.prefecture == 13]

# 同じ日付ごとに合計を出す
df_tokyo = df_tokyo.groupby('date').sum()

# 不要な列名を削除
df_tokyo = df_tokyo.drop(columns=['prefecture', 'medical_worker', 'status'])

# 累積和計算
df_tokyo = df_tokyo.cumsum()

# インデックス降り直しによりdate列を作成
df_tokyo = df_tokyo.reset_index()
df_tokyo = df_tokyo.astype({'date': str})
# print(df)

# 日付-を/に置換
df_tokyo['date'] = df_tokyo['date'].str.replace('-', '/')

# csv出力
df_tokyo.to_csv('tokyo_vaccine_count.csv', index=False)

plt.plot(df_tokyo['count'])
plt.show()




