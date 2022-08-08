import json
import requests

import conf
sandbox = ("https://sandboxapicdc.cisco.com")

def obtener_token(usuario, clave):


    url = sandbox + "/api/aaaLogin.json"
    body = {
        "aaaUser":{
            "attributes":{
                "name":usuario,
                "pwd":clave

            }
        }
    }
    cabecera = {
    "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    #requests.packages.urllib3.disable_warnings() : deshabilita las advertencias
    #verify=False: omite la verificacion
    respuesta = requests.post(url, headers=cabecera, data=json.dumps(body), verify=False)
    token = respuesta.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
    return token
#token = obtener_token("admin", "!v3G@!4@Y")
token = obtener_token(conf.usuario, conf.clave)
print(token)