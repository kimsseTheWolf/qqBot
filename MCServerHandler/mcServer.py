import requests

SERVER_IP_ADDRESS = ""

def get_server_status(server_ip):
    response = requests.get(f"https://api.mcsrvstat.us/3/{server_ip}")
    print(response)
    return response.json()

class MinecraftJavaServer:
    
    def __init__(self, exeFileLocation:str, minMem:int, maxMem:int, frpURL:str):
        self.exeFileLocation = exeFileLocation
        self.minMem = minMem
        self.maxMem = maxMem
        self.frpURL = frpURL
        pass