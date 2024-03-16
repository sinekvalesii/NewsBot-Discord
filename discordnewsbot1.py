import feedparser
import discord
import asyncio

# Discord bot token ve kanal ID (gerçek değerlerle değiştirin)
DISCORD_BOT_TOKEN = 'BOT_TOKEN'
DISCORD_CHANNEL_ID = 'CHANNEL_ID'

# Evrim Ağacı RSS feed URL
FEED_URL = 'https://evrimagaci.org/rss.xml'

# Discord istemcisini başlat
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

async def check_feed():
    # RSS feed'i ayrıştır
    feed = feedparser.parse(FEED_URL)

    # Mesajların gönderileceği kanalı al
    channel = client.get_channel(int(DISCORD_CHANNEL_ID))

    if channel:
        # Her haber öğesini Discord kanalına gönder
        for item in feed.entries:
            await channel.send(f"**{item.title}**\n{item.link}")

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    await check_feed()
    # Feed'i her 10 dakikada bir kontrol et
    while True:
        await asyncio.sleep(60)  # 10 dakika saniye cinsinden
        await check_feed()

# Discord botunu başlat
client.run(DISCORD_BOT_TOKEN)

# Lütfen DISCORD_BOT_TOKEN ve DISCORD_CHANNEL_ID'nin gerçek değerlerle değiştirilmesi gerektiğini unutmayın.
