import discord
from discord.ext import commands
import openai

openai.api_key = '<openAI API Key>'

intents = discord.Intents.all()  # Enables all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def chat(ctx, *, message):
    response = openai.ChatCompletion.create(
      model="gpt-4", # assuming that the GPT-4 model is named "gpt-4"
      messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )
    await ctx.send(response['choices'][0]['message']['content'])

bot.run('<Discord bot token>')
