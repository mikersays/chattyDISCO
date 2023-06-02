import discord
from discord.ext import commands
import openai

openai.api_key = '<openAI API Key>'

intents = discord.Intents.all()  # Enables all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def chat(ctx, *, message, max_tokens=1500, temperature=1):
    response = openai.ChatCompletion.create(
      model="gpt-4",
      max_tokens=max_tokens,
      temperature=temperature,
      n=1,
      top_p=1,
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
