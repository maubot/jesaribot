# jesaribot - A simple maubot plugin.
# Copyright (C) 2018 Tulir Asokan
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
from typing import Type

from maubot import Plugin, CommandSpec, PassiveCommand, Command, Argument, MessageEvent
from mautrix.util import BaseProxyConfig, ConfigUpdateHelper

from .versions import gif_versions

COMMAND_JESARI = "xyz.maubot.jesari"
ARG_QUALITY = "$quality"
COMMAND_JESARI_QUALITY = f"jesariquality {ARG_QUALITY}"


class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        if self.get("quality", None) in gif_versions.keys():
            helper.copy("quality")
        else:
            self["quality"] = "high"


class JesariBot(Plugin):
    async def start(self) -> None:
        self.config.load_and_update()
        self.set_command_spec(CommandSpec(
            passive_commands=[PassiveCommand(
                name=COMMAND_JESARI,
                matches="jesari",
                match_against="body",
            )],
            commands=[Command(
                syntax=COMMAND_JESARI_QUALITY,
                arguments={
                    ARG_QUALITY: Argument(".+", required=True, description="The quality"),
                },
                description="Change the quality of the jesari gif",
            )]
        ))
        self.client.add_command_handler(COMMAND_JESARI, self.handler)
        self.client.add_command_handler(COMMAND_JESARI_QUALITY, self.quality_handler)

    async def stop(self) -> None:
        self.client.remove_command_handler(COMMAND_JESARI, self.handler)

    async def handler(self, evt: MessageEvent) -> None:
        await evt.respond(gif_versions[self.config["quality"]])

    async def quality_handler(self, evt: MessageEvent) -> None:
        new_quality = evt.content.command.arguments[ARG_QUALITY]
        if new_quality not in gif_versions.keys():
            await evt.reply(f"Invalid quality. Available qualities: {gif_versions.keys()}")
            return
        self.config["quality"] = new_quality
        self.config.save()
        await evt.reply(gif_versions[self.config["quality"]])

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config
