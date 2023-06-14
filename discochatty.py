import discord
from discord.ext import commands
import openai

openai.api_key = '<openAI API Key>'

intents = discord.Intents.all()  # Enables all intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def chat(ctx, *, message, max_tokens=1500, temperature=1):
    for _ in range(2):  # two attempts in total: one original and one retry
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-0613",
                max_tokens=max_tokens,
                temperature=temperature,
                n=1,
                top_p=1,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant named Chatty."
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
            break  # if the operation is successful, we break the loop

        except Exception as e:
            print(e)
            if _ == 0:  # if it's the first attempt
                print("An error occurred. Retrying...")
            else:  # if it's the second attempt
                await ctx.reply("Oops! Something went wrong. Please try again.")
                break  # we break the loop

bot.run('<Discord bot token>')
