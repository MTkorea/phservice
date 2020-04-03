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

#프사봇 부분

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
                            embed.set_footer(text=f"문의는 OOOP!#2036")
                            await i.send(embed=embed)
                    except:
                        pass

    if message.content.startswith("!삭제"):
        await message.channel.purge(limit=100)
        await message.channel.send('메세지 100개 가삭제되었습니다.')
        await message.channel.purge(limit=1)   

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

    if message.content == '!컬러테스트':
            embed=discord.Embed(title='컬러테스트', color=0x35afd5, timestamp=message.created_at)
            embed.add_field(name="컬러테스트", value=f'컬러테스트', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!도움말':
            embed=discord.Embed(title='초고퀄 최저가 프사샵', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="!디스코드", value=f'프사샵의 디스코드주소를 확인할수 있습니다.', inline=False)
            embed.add_field(name="!배너문의", value=f'프사샵 배너문의를 하실수 있습니다.', inline=False)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!도움말':
            embed=discord.Embed(title='대화봇', color=0x43b581, timestamp=message.created_at)
            embed.add_field(name="대화봇 <할말> (Beta)", value=f'예) "대화봇 안녕" 등등 답을 해줍니다.', inline=False)
            embed.add_field(name="!내정보", value=f'간단한 자신의정보를 확인할수 있습니다.', inline=False)
            embed.add_field(name="!핑", value=f'봇 정상 동작여부를 확인합니다.', inline=False)
            embed.add_field(name="!할까 말까", value=f'선택장애 당신에게 필요한 명령어', inline=False)
            embed.add_field(name="!주사위", value=f'주사위를 굴릴수 있습니다. 1 ~ 6까지 랜덤으로 나옵니다.', inline=False)
            embed.add_field(name="!현재시각", value=f'현재시각을 출력합니다!', inline=False)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!디버그':
            embed=discord.Embed(title='초고퀄 최저가 프사샵', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="!컬러테스트", value=f'임베드 컬러테스트', inline=True)
            embed.add_field(name="!핑", value=f'봇 정상 동작여부를 확인합니다.', inline=False)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

#대화봇 부분

    if message.content.startswith('+핑'):
        before = time.monotonic()
        msg = await client.send_message(message.channel, ':ping_pong: 퐁!')
        ping = (time.monotonic() - before) * 1000
        text = ":ping_pong: 퐁!  {0}ms ".format((round(ping, 1)))
        await client.edit_message(msg, text)
        print(text)
        
    if message.content.startswith('!현재시각'):
        t = t = datetime.datetime.now()
        h = str(t.hour)
        m = str(t.minute)
        s = str(t.second)
        await message.channel.send('지금 시각은 **' + h + ':' + m + ':' + s + '**(이)입니다.')

    if message.content.startswith('!할까 말까'):
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0000FF, timestamp=message.created_at)
            embed.add_field(name="할까 말까 :", value=f'하세요!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0xFF0000, timestamp=message.created_at)
            embed.add_field(name="할까 말까 :", value=f'하지마세요!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == '!핑':
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="퐁!:ping_pong: ", value=f'봇이 정상적으로 동작중입니다.', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content.startswith("!내정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x0170ed)
        embed.add_field(name="닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="디스코드가입일", value=str(date.year) + "/" + str(date.month) + "/" + str(date.day), inline=True)
        embed.add_field(name="디스코드주소: discord.gg/t5tZUUg", value=message.author.name + "님 반가워요!", inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)   

    if message.content.startswith('!주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="주사위", value=f'1번!', inline=True)
            embed.set_image(url=f"http://www.apcls.kro.kr/file/주사위/1.png")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        if randomNum == 2:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="주사위", value=f'2번!', inline=True)
            embed.set_image(url=f"http://www.apcls.kro.kr/file/주사위/2.png")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        if randomNum ==3:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="주사위", value=f'3번!', inline=True)
            embed.set_image(url=f"http://www.apcls.kro.kr/file/주사위/3.png")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        if randomNum ==4:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="주사위", value=f'4번!', inline=True)
            embed.set_image(url=f"http://www.apcls.kro.kr/file/주사위/4.png")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        if randomNum ==5:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="주사위", value=f'5번!', inline=True)
            embed.set_image(url=f"http://www.apcls.kro.kr/file/주사위/5.png")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        if randomNum ==6:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="주사위", value=f'6번!', inline=True)
            embed.set_image(url=f"http://www.apcls.kro.kr/file/주사위/6.png")
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

#대화봇 디비부분

    if message.content == "대화봇":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'넹? 저한테 할말 있어요?', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'왜 불렀어요 바쁜데 ㅡ.ㅡ', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 안녕":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'반갑습니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'안녕하세요!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 ㅎㅇ":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'ㅎㅇㅎㅇ!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'안뇽안뇽~', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 반가워":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'저도 반갑습니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'잘부탁드립니다~', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 반가워":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'저도 반갑습니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'잘부탁드립니다~', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 뭐해":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'오류 수정중입니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'상담중입니다 쉿!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 뭐해?":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'뒹굴뒹굴...', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'봇 자가업데이트중 입니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 대답해":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'네? 저 부르셨나요?', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'대답!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 뭐하니":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'심심해요...', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'밥먹고 있습니다!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 몇살?":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'너보다는 나이가 많을거시야...', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'random.randrange(10,20) ㅇㅋ?', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 바보":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f';;왜 나한테...', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0x0170ed, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'주인한테 이른다?', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)  

    if message.content == "대화봇 시발":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0xf26522, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'뭐 시바라', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0xe72423, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'시바 가만히 있는데 욕박네', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)

    if message.content == "대화봇 병신":
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            embed=discord.Embed(title='대화봇', color=0xf26522, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'지는 ㅋ', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title='대화봇', color=0xe72423, timestamp=message.created_at)
            embed.add_field(name="응답 :", value=f'개때끼가 딴데가서 지럴해 여기서 지럴하지말고', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)


#상태메세지 부분
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("!도움말")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game("초고퀄프사 제작중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game(f'{len(client.guilds)}개의 서버에 참여중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
        game = discord.Game(f'{len(client.users)}명의 유저들과 소통하는중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)
"""
        game = discord.Game("봇 테스팅중")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(2)  
"""

access_token = os.environ["BOT_TOKEN"]
        
client.loop.create_task(my_background_task())

client.run(access_token)
