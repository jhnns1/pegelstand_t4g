import requests
import streamlit as st

# request data for fuzzyId passau and waters Donau, Inn, Ilz
response = requests.get("https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json?fuzzyId=passau&waters=DONAU,INN,ILZ")

data = response.json()

# extract 4 stations with their matching uuid
stations = [data[i]['shortname'] for i in range(4)]

res = list()
for i in range(len(stations)):
    url_tmp = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/" + stations[i] + "/W/currentmeasurement.json"
    req_tmp = requests.get(url_tmp)
    data_tmp = req_tmp.json()
    res.append(data_tmp)

st.title('Passau-Wasserstände')

st.write("Lieber Nutzer, hier die Wasserstände inkl. Tendenz für die 4 Messstellen in Passau")
for i in range(len(stations)):
    st.write("Station: {}" .format(stations[i]))
    try: 
        st.write("Pegel: {}" .format(res[i]['value']))
        if res[i]['trend'] == 1:
              st.write("Trend: steigend")
        elif res[i]['trend'] == -1:
              st.write("Trend: fallend")
        else:
              st.write("Trend: gebleibend")
        if res[i]['value'] >= 850.0:
              st.write("Warnung: Meldestufe 4")
        elif res[i]['value'] >= 770.0:
              st.write("Warnung: Meldestufe 3")
        elif res[i]['value'] >= 740.0:
              st.write("Warnung: Meldestufe 2")
        elif res[i]['value'] >= 700.0:
              st.write("Warnung: Meldestufe 1")
        else: st.write("Keine Warnung vorliegend.")
        st.write("\n\n")
    except:
        st.write("Leider haben wir für diese Station keine Daten. Wir bitten um Ihr Verständnis.")
        st.write("\n\n")
        continue
