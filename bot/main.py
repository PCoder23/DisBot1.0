import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="$")
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    # guild = discord.utils.get(client.guilds, name=GUILD)
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')
    # general_channel=client.get_channel(851710538983538721)
    # await general_channel.send(
    #     "hello"
    # )

# text messages and responses
# chat =  {"greeting":{"message":["hi corvis","hello corvis","hi corvis","corvis"],
#                      "response":["hi","hello",]},
#          "wishes":{"message":["happy birthday","good morning"],
#                    "response":["happy birthday","good moring"]},
#          "talks1":{"message":["do you know me","do you know about me","you know about me"],
#                  "response":["yeah,you are a great guy"]},
#     "talks1":{"message":["tell me something i don't know"],
#                  "response":["yeah,you are a great guy"]}
         
# }
 
# @client.event
# async def on_member_join(member):
#     if (member.name=="Nishant Ranjan"):
#         await member.create_dm()
#         await member.dm_channel.send(
#         f"Hi {member.name}, muh main lega"
#         )
#     else:
#         await member.create_dm()
#         await member.dm_channel.send(
#         f"Hi {member.name}, welcome to PCoder"
#         )
@client.event
async def on_member_join(member):
    await member.send('Hi {member.name}, welcome to my Discord server!,\n ThankYou for joining. Pranav will contact you shortly ')
# @client.event
# async def on_message(message):
#     if (message.author==client.user):
#         return
#     if (message.content=="Hi"):
#         response= random.choice(greetings)
#         await message.channel.send(response)
#     for elements in chat:
#         for items in chat[elements]['message']:
#             if (message.content == items):
#                 response = random.choice(chat[elements]['response'])
#                 await message.channel.send(response)
#     print (message)

server.server()
bot.run(TOKEN)
