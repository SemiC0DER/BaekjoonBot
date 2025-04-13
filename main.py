import discord
from discord import app_commands
from dotenv import load_dotenv

# 토큰 로드
load_dotenv()

# 클라이언트 생성
class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)
    
    async def on_ready(self):
        print(f'안녕하세요, 백준봇입니다! {self.user}')
        await self.tree.sync()