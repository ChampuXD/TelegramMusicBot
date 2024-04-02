from ChampuXMusic.core.bot import Champu
from ChampuXMusic.core.dir import dirr
from ChampuXMusic.core.git import git
from ChampuXMusic.core.userbot import Userbot
from ChampuXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Champu()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
