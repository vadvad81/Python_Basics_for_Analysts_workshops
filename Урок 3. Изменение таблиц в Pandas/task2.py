import pandas as pd
df = pd.read_csv('kc_house_data.csv', sep=',')
clients = pd.DataFrame({
    'client_id': [1459, 4684, 3498, 3942, 4535, 2308, 2866, 2765, 1472, 4236, 2295, 939, 3840, 280, 20, 4332, 3475, 4213, 3113, 4809, 2134, 2242, 2068, 4929, 1384, 1589, 3317, 2260, 1727, 1764, 1611, 1474],

'house_id': 
[
    8965450190, 6823100225, 5104540330, 2131701075, 1522700060, 1189000207,
    6821600300, 7137950720, 9510920050, 6131600255, 5428000070, 1788800910,
    8100400160, 3123049142, 6306800010, 5083000375, 7920100025, 1951600150,
    809001400, 339600110, 1622049154, 1099600250, 8563000110, 2768100205,
    3995700435, 8861700030, 3303980210, 7731100066, 8146100580, 825069097,
    3889100029, 9524100196
]
})

clients_house_id = clients.set_index('house_id')

df_idx = df.set_index('id')

joined = clients_house_id.join(df_idx)

merged = clients.merge(df, left_on='house_id', right_on='id')

