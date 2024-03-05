from warnings import resetwarnings
import requests
import pandas as pd
import datetime
import os
import json, yaml
import traceback

from credentialsConfig import credConfig

config = credConfig()

def getVulnerabilities():
    next=""
    append_data=[]
    for i in range(1, 100):
        try:
            url = f"https://container.{config.get_region()}.cloudone.trendmicro.com/api/vulnerabilities?limit=100&cursor={next}"
            payload = {}

            headers = { 
                'api-version': 'v1',
                'Authorization': f"ApiKey {config.get_apikey()}" 
            }
            response = requests.request("GET", url, headers=headers, data=payload).json()
            next=response["next"]
            if(len(response['vulnerabilities'])>0):
                df = pd.json_normalize(response['vulnerabilities'])
                append_data.append(df)
            else:
                print("Completed!, Vulnerabilities not found!")
        except Exception:
            return append_data
    return append_data

def toExcel(df):
    result = pd.concat(df)
    if(len(df)>0):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        with pd.ExcelWriter(f'vulnerabilities_{timestamp}.xlsx') as writer:  
            result.to_excel(writer, sheet_name='Container_Vulnerabilities')
            print("Completed!, The result are in Result_File.xlsx")
    else:
        print("Completed!, Vulnerabilities not found!")

def initialConfig():
    filename = "config.yml"
    try:
        if(os.path.isfile(filename)):
            with open(filename) as file:
                doc = yaml.load(file, Loader=yaml.FullLoader)
                config.set_apikey(doc["API_KEY"])
                config.set_region(doc["REGION"])
            toExcel(getVulnerabilities())
        else:
            print("Please provide the valid configuration file path, the file must be called config.yml")
    except (Exception, KeyError) as err:
        traceback.print_exc()
        print("Error: Please check that the Config.yml file is properly configured - ", err)
    
initialConfig()