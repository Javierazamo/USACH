import requests
import json

url = "https://10.10.20.14/api/aaaLogin.json"

data = {

    "aaaUser": {

        "attributes": {

            "name": "admin",

            "pwd": "C1sco12345"

        }

    }

}

cabecera = {"content-type": "application/json"}

requests.packages.urllib3.disable_warnings()
respuesta = requests.post(url, json.dumps(data), headers=cabecera, verify=False)

respuesta_json = respuesta.json()

# print(respuesta.json())

API_Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
# print("***************************************")

print("API-Token :" + API_Token)

url1 = "https://10.10.20.14/api/mo/uni.json"
cabecera = {
    "Content-Type": "application/json"
}

WebToken = {
    "APIC-Cookie": API_Token
}

respuesta1 = requests.get(url1, headers=cabecera, cookies=WebToken,verify=False)
print(respuesta1.json())