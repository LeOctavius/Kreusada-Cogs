import discord
from validator_collection import validators
from redbot.core import commands, checks, Config
from .allianceembed import Embed


class Alliance(commands.Cog):
    """Tools for your alliance on MCOC."""

    def __init__(self):
        self.config = Config.get_conf(
            self, 200730042020, force_registration=True)
        self.config.register_guild(
            role=None,
            channel=None
        )

    @commands.command()
    async def timezone(self, ctx, *, timezone: str = None):
        """
        Use this command to set your timezone on your nickname.
        For example - `Kreusada [+4]`
        """
        if timezone is None:
            await ctx.author.edit(nick=ctx.author.name)
            embed = Embed.create(
                self, ctx, title="Successful <:success:777167188816560168>",
                description=f"""
                You can set your nickname using `dem timezone <timezone>`.
                For example: `dem timezone +4` or `dem timezone -12`.
                Your timezone is no longer shown on your nickname (`{ctx.author.name}`)
                """
            )
            return await ctx.send(embed=embed)
        user = ctx.author
        before = ctx.author.name
        after = timezone
        tag = "{0} [{1}]".format(before, after)
        try:
            await user.edit(nick=tag)
            embed = Embed.create(
                self, ctx, title="Successful <:success:777167188816560168>",
                description="Your timezone is now displayed on your nickname as: ``{}``".format(
                    tag),
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = Embed.create(
                self, ctx, title="Oopsies! <:error:777117297273077760>",
                description="""
                    Something went wrong during the setup process, I could not change your nickname.
                    This may be due to the following errors:
                    :x: `Invalid Permissions`
                    :x: `Role Heirarchy`
                    Please resolve these issues before I can set nicknames.
                    If you are the server owner, the heirarchy between us cannot be justified.
                    If problems continue, please ask for help in our [support server](https://discord.gg/JmCFyq7).
                    """,
            )
            await ctx.send(embed=embed)

    @commands.group(name="alliancealert")
    async def aa(self, ctx):  # aliases: aa, alert):
        """Alert your fellow alliance mates for movement."""

    @aa.group(name="set")
    @commands.admin_or_permissions(manage_guild=True)
    async def aas(self, ctx):
        """Set the alliance role to be pinged for alerts."""

    @aas.command()
    async def channel(self, ctx, channel: discord.TextChannel):
        await self.config.guild(ctx.guild).channel.set_raw(value=channel)
        embed = Embed.create(
            self, ctx, title="Successful <:success:777167188816560168>",
            description="{} will now be the channel that the alerts will be sent to when Alliance events start".format(
                channel.mention
            )
        )
        await ctx.send(embed=embed)

    @aas.command()
    async def role(self, ctx, role: discord.Role):
        try:
            await self.config.guild(ctx.guild).role.set_raw(value=role.id)
            embed = Embed.create(
                self, ctx, title="Successful <:success:777167188816560168>",
                description=f"{role.mention} will now be mentioned when Alliance events start.",
            )
            await ctx.send(embed=embed)
        except discord.Forbidden:
            embed = Embed.create(
                self, ctx, title="Oopsies! <:error:777117297273077760>",
                description=f"Something went wrong during the setup process.",
            )
            await ctx.send(embed=embed)

    @aa.command(invoke_without_command=True, pass_context=True, aliases=["aa", "alert"])
    async def aqstart(self, ctx):
        """Alliance Quest has started!"""
        embed = Embed.create(
            self, ctx, title='Alliance Quest has STARTED!',
            image="https://media.discordapp.net/attachments/745608075670585344/772947661421805648/aqstarted.png?width=1441&height=480",
            description="Time to join Alliance Quest."
        )
        role = ctx.guild.get_role(await self.config.guild(ctx.guild).get_raw("role"))
        await ctx.send(content=role.mention, allowed_mentions=discord.AllowedMentions(roles=True), embed=embed)
