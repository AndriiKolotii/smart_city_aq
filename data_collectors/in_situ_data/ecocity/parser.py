import urllib.request, json 
import pandas as pd
import pymysql

with urllib.request.urlopen("https://eco-city.org.ua/output") as url:
    data = json.loads(url.read().decode())
    df = pd.json_normalize(data)
    
pollutants  = df.loc[:, 'pollutants']
columns = ['id','cityName', 'stationName', 'localName', 'latitude', 'longitude', 'timezone', 'pol','unit','time', 'value', 'averaging']
df_out = pd.DataFrame(columns=columns)

for station in range(0, df.shape[0]):
    metadata_tmp = df.loc[station, ["id", "cityName","localName", "latitude","longitude", "timezone"]]
    metadata_tmp = pd.DataFrame([metadata_tmp], columns=metadata_tmp.keys())
    metadata_tmp = metadata_tmp.reset_index(drop=True)
    for measurements in range(0,len(pollutants[station])):
        compound = pollutants[station][measurements]
        compound_dt = pd.DataFrame([compound], columns=compound.keys())
        compound_dt = compound_dt.reset_index(drop=True)
        tmp = pd.concat([metadata_tmp,compound_dt], axis = 1)
        df_out = df_out.append(tmp)
        
df_out = df_out.reset_index(drop=True)
df_out['value'] = df_out['value'].astype(float)
df_out= df_out.dropna(subset=['value'])
df_out= df_out.rename(columns = {'id': 'Station_ID'}, inplace = False)
df_out=df_out.drop(columns=['stationName'])

#df_out.to_csv('/Users/andrew/Downloads/res.csv',index=range(0, df.shape[0]))


connection = pymysql.connect(host='...', user='...', password='...', db='ecocity')
cursor=connection.cursor()
sql = "INSERT INTO ecocity_data(Station_ID, cityName, localName, latitude, longitude, timezone, pol, 	unit, time,	value,	averaging) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for i,row in df_out.iterrows():
    cursor.execute(sql, tuple(row))
    connection.commit()

connection.close()
