"""
This project is licensed under the GNU General Public License v3.0
Please refer to the LICENSE file for more information.
"""

import tracemalloc

tracemalloc.start(25)

import decouple
import discord


class Bot(discord.AutoShardedBot):
    """
    The main class of the bot.
    Inherited from discord.AutoShardedBot
    """

    def __init__(self) -> None:
        _intents = discord.Intents.default()
        _intents.members = True
        super().__init__(
            intents=_intents,
            owner_ids={733920687751823372, 1068494523723944027},
            activity=discord.Game("OuO Bot V2"),
        )
        self._client_ready = False
        for k, v in self.load_extension("cogs", recursive=True, store=True).items():
            if v:
                print(f"成功載入插件 {k}")
            else:
                print(f"載入插件 {k} 失敗: {v}")

    async def on_shard_connect(self, shard_id: int) -> None:
        """
        The event that is triggered when a shard connected.

        :param shard_id: The shard ID.
        :type shard_id: int
        """
        print(f"分片 {shard_id} 已連線至 Discord")

    async def on_shard_ready(self, shard_id: int) -> None:
        """
        The event that is triggered when a shard is ready.

        :param shard_id: The shard ID.
        :type shard_id: int
        """
        print(f"分片 {shard_id} 已準備就緒")

    async def on_shard_resumed(self, shard_id: int) -> None:
        """
        The event that is triggered when a shard resumed.

        :param shard_id: The shard ID.
        :type shard_id: int
        """
        print(f"分片 {shard_id} 已恢復連線至 Discord")

    async def on_shard_disconnect(self, shard_id: int) -> None:
        """
        The event that is triggered when a shard disconnected.

        :param shard_id: The shard ID.
        :type shard_id: int
        """
        print(f"分片 {shard_id} 已斷線")

    async def on_ready(self) -> None:
        """
        The event that is triggered when the bot is ready.
        """
        if self._client_ready:
            return

        print("-------------------------")
        print(f"已登入: {self.user.name}#{self.user.discriminator} ({self.user.id})")
        print(f"分片數量: {self.shard_count}")
        print(f"記憶體使用量: {tracemalloc.get_traced_memory()[0] / 1024 ** 2:.2f} MB")
        print(f"API 延遲: {self.latency * 1000:.2f} ms")
        print("-------------------------")
        self._client_ready = True

    async def close(self) -> None:
        """
        Closes the bot.
        """
        await super().close()

    def run(self) -> None:
        """
        Starts the bot.
        """
        super().run(decouple.config("token"))


if __name__ == "__main__":
    Bot().run()
