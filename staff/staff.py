import discord
import asyncio
from datetime import datetime, timedelta
from redbot.core import commands, checks, Config, modlog


class Staff(commands.Cog):
    """Cog for alerting Staff."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self, 200730042020, force_registration=True)
        default_guild = {
            "role": None,
            "channel": None
        }
        self.config.register_guild(**default_guild)

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete
        """
        return

    @commands.group()
    async def staffset(self, ctx):
        """Staff notifier configuration."""

    @staffset.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def channel(self, ctx, channel: discord.TextChannel):
        """Sets the channel for staff to receive notifications."""
        await self.config.guild(ctx.guild).set_raw("channel", value=channel.id)
        embed = discord.Embed(
            title="Successful :white_check_mark:",
            description=f"{channel.mention} will now receive notifications from users to notify the staff."
        )
        await ctx.send(embed=embed)

    @staffset.command()
    @checks.admin_or_permissions(manage_guild=True)
    async def role(self, ctx, role: discord.Role):
        """Sets the Staff role."""
        try:
            await self.config.guild(ctx.guild).set_raw("role", value=role.id)
            embed = discord.Embed(
                title="Successful :white_check_mark:",
                description=f"{role.mention} will now be considered as the Staff role.",
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(
                title="Oopsies! :x:",
                description=f"Something went wrong during the setup process."
            )
            await ctx.send(embed=embed)
        return
        
    @commands.command()
   # @commands.cooldown(1, 600, commands.BucketType.user)
    async def staff(self, ctx):
        """Notifies the staff."""
        message = ctx.message
        role = await self.config.guild(ctx.guild).role()
        channel = await self.config.guild(ctx.guild).channel()
        channel = discord.utils.get(ctx.guild.channels, id=channel)
        role = discord.utils.get(ctx.guild.roles, id=role)
        jumper_link = ctx.message.jump_url
        author_id = ctx.author.id
        jumper_f = "**[Click here for context]({})**".format(jumper_link)
        embed = discord.Embed(
            title=":warning: ALERT!",
            description=f"**{ctx.author.name}** has just called for the staff in {ctx.channel.mention}!",
            color=0xffff33)
        embed.set_footer(text=f"{bot.user.name} | Staff", icon_url=bot.user.avatar_url)
        if channel is not None:
            await message.add_reaction("✅")
            await ctx.send("We have sent a report to the staff team. They will be with you as soon as possible.")
            if role is not None:
                return await channel.send(content=f":warning: {role.mention}", allowed_mentions=discord.AllowedMentions(roles=True), embed=embed, delete_after=43200)
            else:
                await channel.send(allowed_mentions=discord.AllowedMentions(roles=True), embed=embed, delete_after=43200)
            return
        else:
            await message.add_reaction("❌")
            return await ctx.send("The staff team have not yet configured a channel.")
