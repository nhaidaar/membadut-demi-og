import discord
import requests
import time
import numpy as np
import webserver
from webserver import keep_alive

class MyClient(discord.Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
      chan = self.get_channel(909771824307511316)
      r = requests.get("https://raw.githubusercontent.com/nhaidaar/membadut-demi-og/master/quotes2.json")
      data = r.json()
      
      while (True):
        await chan.send(np.random.choice(data, size=1)[0]['quote'])
        time.sleep(65)

keep_alive()
client = MyClient()
client.run("MzY1NDc4MzQ0Mjk0NDAwMDEw.YX-cJw.C7e_aLZ_3JUtbkL0JfHeMryPvMs", bot=False)
