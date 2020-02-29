import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("역할봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!역할봇 안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 안녕하세요"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 ㅎㅇ"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 인사"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 Hi"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 하이"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 hi"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!역할봇 짖어!"):
        await message.channel.send("왈왈")
    if message.content.startswith("!역할봇 짖어"):
        await message.channel.send("왈왈왈")

    if message.content.startswith("!역할봇사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!채널메세지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("!UserDM"):
        author = message.guild.get_member(int(message.content[8:26]))
        msg = message.content[27:]
        await author.send(msg)

    if message.content.startswith("!hrankUSER"):
        author = message.guild.get_member(int(message.content[11:29]))
        role = discord.utils.get(message.guild.roles, name="USER")
        await author.add_roles(role)

client.run("NjgzMjk2ODA3MTIzODEyNTk5.Xlpf1Q.ApDrjR9QK4cif9IrdjzYuAP1g7o")