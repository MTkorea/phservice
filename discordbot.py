import discord
import asyncio
import random
import time
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')

@client.event
async def on_message(message):
    if message.content.startswith('!공지'):
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    try:
                        msg = message.content[4:]
                        if message.author.id == 560330444428673026:
                            embed=discord.Embed(colour=0x0170ed, timestamp=message.created_at, title="초고퀄 최저가 프사샵")
                            embed.add_field(name="전체공지", value=msg, inline=True)
                            embed.set_footer(text=f"부담없이 문의주세용!")
                            await i.send(embed=embed)
                    except:
                        pass

    if message.content.startswith("!삭제"):
        await message.channel.purge(limit=100)
        await message.channel.send('메세지 100개 가삭제되었습니다.')
        await message.channel.purge(limit=1)

    if message.content.startswith("!내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x0170ed)
        embed.add_field(name="닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="디스코드가입일", value=str(date.year) + "/" + str(date.month) + "/" + str(date.day), inline=True)
        embed.add_field(name="디스코드주소: discord.gg/t5tZUUg", value=message.author.name + "님 반가워요!", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)      

    if message.content == '!배너문의':
            embed=discord.Embed(title='배너문의', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="배너문의", value=f'OOOP!#2036', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
            
    if message.content == '!디스코드':
            embed=discord.Embed(title='Discord', color=0x7289da, timestamp=message.created_at)
            embed.add_field(name="디스코드 주소", value=f'https://discord.gg/t5tZUUg', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!핑':
            embed=discord.Embed(title='초고퀄 최저가 프사샵', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="퐁!:ping_pong: ", value=f'봇이 정상적으로 동작중입니다.', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!컬러테스트':
            embed=discord.Embed(title='컬러테스트', color=0x35afd5, timestamp=message.created_at)
            embed.add_field(name="컬러테스트", value=f'컬러테스트', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!도움말':
            embed=discord.Embed(title='초고퀄 최저가 프사샵', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="!내정보", value=f'간단한 자신의정보를 확인할수 있습니다.', inline=True)
            embed.add_field(name="!디스코드", value=f'프사샵의 디스코드주소를 확인할수 있습니다.', inline=False)
            embed.add_field(name="!배너문의", value=f'프사샵 배너문의를 하실수 있습니다.', inline=False)
            embed.add_field(name="!핑", value=f'봇 정상 동작여부를 확인합니다.', inline=False)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!도움말':
            embed=discord.Embed(title='대화봇', color=0x43b581, timestamp=message.created_at)
            embed.add_field(name="대화봇 <할말> (Beta)", value=f'예) "대화봇 안녕" 등등 답을 해줍니다.', inline=False)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!디버그':
            embed=discord.Embed(title='초고퀄 최저가 프사샵', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="!컬러테스트", value=f'임베드 컬러테스트', inline=True)
            embed.add_field(name="!핑", value=f'봇 정상 동작여부를 확인합니다.', inline=False)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

#대화봇 디비부분

    if message.content == '대화봇 안녕':
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답", value=f'반갑습니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

            
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("!배너문의")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("초고퀄프사 제작중")
        await client.change_presence(status=discord.Status.online, activity=game)
        game = discord.Game("대화봇 구동중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        await asyncio.sleep(2)
        game = discord.Game(f'{len(client.guilds)}개의 서버에 참여중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game(f'{len(client.users)}명의 유저들과 소통하는중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)

access_token = os.environ["BOT_TOKEN"]
        
client.loop.create_task(my_background_task())

client.run(access_token)
