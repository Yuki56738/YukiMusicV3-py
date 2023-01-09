import discord

from discord import *

import wavelink

bot = discord.Bot()


#
@bot.slash_command()
async def play(ctx: ApplicationContext):
    vc = await ctx.user.voice.channel.connect()
    vc.play(discord.FFmpegPCMAudio("VR - Virtual Reality (Music Only) _ KMNZ [Official Music Video]-lYQGWVSVl_Y.mp3"))



bot.run("MTAyMTY3NDYxODY4MTAzMjcyNA.GSkizf.emLroGkSY4GEGFePy6AXMsO5_g7P8q3sQp-r0s")
