
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run('OTY3MTEzOTEwMTg2NTY1Njk0.Gx6KGb.PsSrdrMzUmJMB_JuNLdBufsyHmf_7_sYb8TIEI')

