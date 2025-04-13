import discord

def todayLeaderboard(members):
    embed = discord.Embed(title='현황판', description='', color=current_color)
    for i in range(len(members)):
        embed.add_field(name=market[1], value='', inline=False)