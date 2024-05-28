# __init__.py (Python)

from .giveaway_cog import GiveawayCog

def setup(bot):
    bot.add_cog(GiveawayCog(bot))