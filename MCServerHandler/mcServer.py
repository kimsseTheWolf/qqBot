import requests

SERVER_IP_ADDRESS = ""

def get_server_status(server_ip):
    response = requests.get(f"https://api.mcsrvstat.us/3/{server_ip}")
    print(response)
    return response.json()

def generate_pretty_status_output(resp):
    content = ""
    if resp["online"] == False:
        content += "⚠️服务器当前离线！\n"
    else:
        content += "✔️服务器当前在线!\n"
        content += f"- 在线人数:{resp['players']['online']}\n"
        content += f"- Minecraft版本:{resp['protocol']['name']}\n"
    
    content += f"""
============
- 服务器IP地址:{resp["dns"]["a"]["name"]}:{resp["port"]}
若遇到任何问题请咨询服主,或使用以下指令操作服务器:
1. 开启服务器:尝试启动服务器
2. 查询服务器状态:输出服务器状态信息
============
    """
    return content

class MinecraftJavaServer:
    
    def __init__(self, exeFileLocation:str, minMem:int, maxMem:int, frpURL:str):
        self.exeFileLocation = exeFileLocation
        self.minMem = minMem
        self.maxMem = maxMem
        self.frpURL = frpURL
        pass
    
# print(get_server_status("us-1.lcf.icu:34111"))