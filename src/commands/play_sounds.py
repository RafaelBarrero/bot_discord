import asyncio
import discord
import pathlib
from discord.ext import commands
from discord.ext.commands import Context


class PlaySound(commands.Cog):
    file_path = pathlib.Path(__file__)
    sound_path = file_path.parent.parent.joinpath("canciones")
    print()

    def __init__(self, bot):
        self.bot = bot

    async def play_sound(self, ctx: Context, path: str):
        author: discord.Member = ctx.message.author
        voice_channel: discord.VoiceChannel = author.voice.channel

        audio_source = discord.FFmpegPCMAudio(source=path)

        await voice_channel.connect()
        voice: discord.VoiceClient = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice.is_playing():
            voice.play(audio_source, after=None)
            while voice.is_playing():
                await asyncio.sleep(1)
            await voice.disconnect()
            print("terminó de reproducir el audio")

    @commands.command(name='vox', help='FRANCO, FRANCO. ESPAÑA, ESPAÑA')
    async def vox(self, ctx: Context):
        file = self.sound_path.joinpath("vox/song.mp3")

        await self.play_sound(ctx, file)

    @commands.command(name='dance', help='WOW, YOU CAN REALLY DANCE')
    async def dance(self, ctx: Context):
        file = self.sound_path.joinpath("dance/song.mp3")

        await self.play_sound(ctx, file)


def setup(bot):
    bot.add_cog(PlaySound(bot))