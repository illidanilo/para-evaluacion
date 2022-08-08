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
obtener_token(conf.usuario, conf.clave)


##GET http://apic-ip-address/api/class/topSystem.json
def top_system():
    cabecera = {
        "Content-Type": "application/json"
    }
    lagalleta = {
        "APIC-Cookie": obtener_token(conf.usuario, conf.clave)
    }

    respuesta = requests.get(sandbox+"/api/class/topSystem.json", headers=cabecera, cookies=lagalleta, verify=False)
    for i in range(0, 3):
    #respuesta.json()["imdata"][0]["topSystem"]["attributes"]["state"]
    #se cambia el 0 por la variable i que indica que tiene el valor del 1 al 3 segun lo definido
    #respuesta.json()["imdata"][i]["topSystem"]["attributes"]["state"]

         estado = respuesta.json()["imdata"][i]["topSystem"]["attributes"]["state"]
         print(estado)
top_system()