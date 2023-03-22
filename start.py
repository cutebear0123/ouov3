import discord,json

intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(
    activity=discord.Game("OuO Bot V2"),
    owner_ids={733920687751823372, 1068494523723944027},
    intents=intents,
)

if __name__ == "__main__":
    #載入Cogs
    for key, value in bot.load_extension("cogs", recursive=True, store=True).items():
        if value == True:
            print(f"成功載入插件 {key}")
        else:
            print(f"載入插件 {key} 失敗: {value}")
    # 啟動機器人
    config = open("data/config.json")
    config = json.load(config)
    bot.run(config["token"])