import discord
from discord.ext import commands
import AI_Logic

DISCORD_TOKEN = "DISCORD API TOKEN" # <--- Discord Bot TOKEN here
intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is connected and ready!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!'): # change the '!' to change the prefix of the bot
        text_content = message.content
        text_content = text_content[1:]

        text_content = message.content
        reply = AI_Logic.gpt.askGPT({text_content})
        await message.channel.send(reply)
        print(f"{message.author}: {text_content}")

bot.run(DISCORD_TOKEN)