# jesaribot - A simple maubot plugin.
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from typing import Type, Tuple

from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper
from maubot import Plugin, MessageEvent
from maubot.handlers import command

from .versions import gif_versions


class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        if self.get("quality", None) in gif_versions.keys():
            helper.copy("quality")
        else:
            self["quality"] = "high"


class JesariBot(Plugin):
    async def start(self) -> None:
        await super().start()
        self.config.load_and_update()

    @command.passive("jesari")
    async def handler(self, evt: MessageEvent, _: Tuple[str]) -> None:
        await evt.respond(gif_versions[self.config["quality"]])

    @command.new("jesariquality", help="Change the quality of the jesari gif")
    @command.argument("new_quality", "quality")
    async def quality_handler(self, evt: MessageEvent, new_quality: str) -> None:
        if new_quality not in gif_versions.keys():
            await evt.reply(f"Invalid quality. Available qualities: {gif_versions.keys()}")
            return
        self.config["quality"] = new_quality
        self.config.save()
        await evt.reply(gif_versions[self.config["quality"]])

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config
