import botpy
from botpy.message import Message
import GPT.gpt as gpt
import MCServerHandler.mcServer as mcserver

class TinyIW(botpy.Client):
    async def on_at_message_create(self, message:Message):
        if message.content.find("嗷") != -1:
            await message.reply(content=f"嗷嗷嗷！")
            
        elif message.content.find("你是谁") != -1:
            await message.reply(content=f"我是小傻狼，这个小窝的小助理！记得投喂嗷嗷饼干哦！")
            
        elif message.content.find("？") != -1 or message.content.find("?") != -1:
            print("Generating answers from GPT...")
            await message.reply(content=gpt.sendQuestionPrivate(message.content)["data"])
            
        elif message.content.find("服务器") != -1:
            if (message.content.find("状态") != -1):
                await message.reply(content=mcserver.generate_pretty_status_output(mcserver.get_server_status("us-1.lcf.icu:34111")))
                
        else:
            await message.reply(content=f"小傻狼接收到你的消息啦！")
        
intests = botpy.Intents(public_guild_messages=True)
client = TinyIW(intents=intests)
client.run(appid="102080996", token="lrQ9QhB63LeRbdqrNpiiofygK3vgXVjO")
