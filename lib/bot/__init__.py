from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as Botbase

PREFIX = ">"
OWNER_IDS = []


class Bot(Botbase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guilds = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, OWNER_IDS=OWNER_IDS)


def run(self):
    pass


async def on_connect(self):
    print("bot connected")


async def on_disconnect(self):
    print("bot disconnected")


async def on_ready(self):
    pass


async def on_message(self, message):
    pass
