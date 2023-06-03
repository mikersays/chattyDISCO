import discord
from discord.ext import commands
import openai

openai.api_key = '<openAI API Key>'

intents = discord.Intents.all()  # Enables all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def chat(ctx, *, message, max_tokens=1500, temperature=1):
    try:
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
        response_message = response['choices'][0]['message']['content']

        # Split long messages into multiple parts
        while len(response_message) > 0:
            if len(response_message) > 2000:
                part, response_message = response_message[:2000], response_message[2000:]
            else:
                part, response_message = response_message, ''
            await ctx.reply(part)

    except Exception as e:
        print(e)
        await ctx.reply("Oops! Something went wrong. Please try again.")

bot.run('<Discord bot token>')
