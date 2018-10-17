from maubot import Plugin, CommandSpec, PassiveCommand, MessageEvent
from mautrix.types import (MessageType, MediaMessageEventContent, ImageInfo, ThumbnailInfo,
                           ContentURI)

COMMAND_JESARI = "xyz.maubot.jesari"


class JesariBot(Plugin):
    async def start(self) -> None:
        self.set_command_spec(CommandSpec(
            passive_commands=[PassiveCommand(
                name=COMMAND_JESARI,
                matches="jesari",
                match_against="body",
            )]
        ))
        self.client.add_command_handler(COMMAND_JESARI, self.handler)

    async def stop(self) -> None:
        self.client.remove_command_handler(COMMAND_JESARI, self.handler)

    @staticmethod
    async def handler(evt: MessageEvent) -> None:
        await evt.respond(MediaMessageEventContent(
            msgtype=MessageType.IMAGE,
            body="putkiteippi.gif",
            url=ContentURI("mxc://maunium.net/IkSoSYYrtaYJQeCaABSLqKiD"),
            info=ImageInfo(
                mimetype="image/gif",
                height=153,
                width=364,
                size=2079294,
                thumbnail_url=ContentURI("mxc://maunium.net/iivOnCDjcGqGvnwnNWxSbAvb"),
                thumbnail_info=ThumbnailInfo(
                    mimetype="image/png",
                    height=153,
                    width=364,
                    size=51302,
                ),
            ),
        ))
