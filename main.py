
import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load character data from JSON
with open("data/characters.json", "r", encoding="utf-8") as f:
    characters = json.load(f)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready!")

@bot.command()
async def start(ctx):
    await ctx.send("🌱 Petualanganmu dimulai! Ketik `!party` untuk melihat anggota partymu.")

@bot.command()
async def party(ctx):
    for char_id, char_data in characters.items():
        embed = discord.Embed(title=char_data["name"], description=char_data["description"], color=0x6b4c9a)
        embed.set_thumbnail(url=f"attachment://{char_data['image'].split('/')[-1]}")
        embed.add_field(name="Skills", value=", ".join(char_data["skills"]), inline=False)

        file = discord.File(char_data["image"], filename=char_data["image"].split("/")[-1])
        await ctx.send(file=file, embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
