import requests
import pandas as pd
import datetime

url = "https://container.us-1.cloudone.trendmicro.com/api/vulnerabilities?cursor="

payload = {}

headers = { 
    'api-version': 'v1',
    'Authorization': 'ApiKey tmc12cmwoXL8F7J6Z4QTr8TC7GqGulc:23oVt3XCadMVnD6FfrJ4N3e4BhheKn8PzF8a3Vf7i719ADSsUEyKKVqebtikkZ5MBR' 
    }

response = requests.request("GET", url, headers=headers, data=payload).json()


#df = pd.DataFrame.from_dict(response[0], orient="index", columns=["vulnerabilities"])


df = pd.json_normalize(response['vulnerabilities'])
print(df)
df.to_excel("vulnerabilities.xlsx")

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

report = f"vulnerabilities_{timestamp}.xlsx"

with open(report, "w") as archivo:
    archivo.write("Contenido del archivo")
