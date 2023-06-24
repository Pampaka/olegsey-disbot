import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name='test')
async def test(ctx, arg):
    await ctx.send(arg)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'спишь?':
        await message.channel.send('На работу пора?')

bot.run(settings['token'])
