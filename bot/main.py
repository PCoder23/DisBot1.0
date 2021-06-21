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

# intents = discord.Intents.all()
# client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

class JoinDistance:
    def __init__(self, joined, created):
        self.joined = joined
        self.created = created

    @property
    def delta(self):
        print(self.joined)
        print(self.created)
        return self.joined - self.created

class JoinDistanceConverter(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return JoinDistance(member.joined_at, member.created_at)

@bot.command()
async def delta(ctx, *, member: JoinDistanceConverter):
    
    is_new = member.delta.days < 100
    if is_new:
        await ctx.send("Hey you're pretty new!")
    else:
        await ctx.send("Hm you're not so new.")

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]] # Remove everyone role!

@bot.command()
async def roles(ctx, *, member: MemberRoles):
    """Tells you a member's roles."""
    await ctx.send('I see the following roles: ' + ', '.join(member))
    
wallet  = 200
@client.command()
async def bet(ctx, money_bet: int):
    outcome = ["win","loose"]
    if random.choice(outcome) == "win" and money_bet < wallet:
        await ctx.send(f"You just won {money_bet}, YAY !")
        users[str(user.id)]["wallet"] += money_bet
    elif random.choice(outcome) == "loose" and money_bet < wallet:
        await ctx.send(f"Damn, you just lost {money_bet} !!!")
        users[str(user.id)]["wallet"] -= money_bet
    else:
        await ctx.send(f"You don't have enough money in your wallet :/ ")

server.server()
bot.run(TOKEN)
