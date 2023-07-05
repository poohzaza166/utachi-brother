import discord
from discord.ext import bridge, commands
from discord.utils import get
from src.fio_log import logs,botconfig
from src.waifu_gen import gen_waifu
import io

typani = []
def run():

    client = bridge.Bot(command_prefix=commands.when_mentioned_or(botconfig['bot_setting']['botprefix']), intents=discord.Intents.all())
    # client = commands.Bot(command_prefix=botconfig['bot_setting']['botprefix'], intents=discord.Intents.all())
    # client = bridge.Bot(command_prefix=botconfig['bot_setting']['botprefix'], intents=discord.Intents.all())

    client.remove_command("help")

    @client.event
    async def on_ready():
        print('base class online')
        logs.info('base class online')

    @client.bridge_command()
    async def help(ctx):
        await ctx.send('https://github.com/poohzaza166/Utachi-discord/wiki')

    @client.bridge_command()
    async def animation(ctx):
        guildid = ctx.guild.id
        if guildid in typani:
            await ctx.send('disabling typing animation')
            typani.remove(guildid)
        else:
            await ctx.send('enabling typing animation')
            typani.append(guildid)

    @client.bridge_command()
    async def gen(ctx, query: str, num_inference_steps: int = 100, seed: int = 69420, guidance_scale: int = 17):
        print('i had been run')
        await ctx.respond("kay gotta draw up the thing give me some time")
        img = gen_waifu(query=query,num_inference_steps=num_inference_steps,seed=seed,guidance_scale=guidance_scale)
        # picture = discord.File(img)
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))
        await ctx.send(f"So you ask me for \n '{query}' \n so here you go!")
        
        
    client.run(botconfig['bot_setting']['bottoken'])

if __name__ == '__main__':
    run()

