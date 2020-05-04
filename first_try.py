import requests
import streamlit as st

# request data for fuzzyId passau and waters Donau, Inn, Ilz
response = requests.get("https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?fuzzyId=passau&waters=DONAU,INN,ILZ")

data = response.json()

# extract 4 stations with their matching uuid
stations = [data[i]['uuid'] for i in range(4)]

res = list()
for i in range(len(stations)):
    url_tmp = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/" + stations[i] + "/W/currentmeasurement.json"
    req_tmp = requests.get(url_tmp)
    data_tmp = req_tmp.json()
    res.append(data_tmp)
    
    print("Lieber Nutzer, hier die Wasserstände inkl. Tendenz für die 4 Messstellen in Passau")
for i in range(len(stations)):
    print("Station: {}" .format(stations[i]))
    try: 
        print("Pegel: {}" .format(res[i]['value']))
        if res[i]['trend'] == 1:
              print("Trend: steigend")
        elif res[i]['trend'] == -1:
              print("Trend: fallend")
        else:
              print("Trend: gebleibend")
        if res[i]['value'] >= 850.0:
              print("Warnung: Meldestufe 4")
        elif res[i]['value'] >= 770.0:
              print("Warnung: Meldestufe 3")
        elif res[i]['value'] >= 740.0:
              print("Warnung: Meldestufe 2")
        elif res[i]['value'] >= 700.0:
              print("Warnung: Meldestufe 1")
        else: print("Keine Warnung vorliegend.")
        print("\n\n")
    except:
        print("Leider haben wir für diese Station keine Daten. Wir bitten um Ihr Verständnis.")
        print("\n\n")
        continue