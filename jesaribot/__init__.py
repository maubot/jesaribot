from maubot import Plugin, CommandSpec, PassiveCommand, MessageEvent
from mautrix.types import (MessageType, MediaMessageEventContent, ImageInfo, ThumbnailInfo,
                           ContentURI)

COMMAND_JESARI = "xyz.maubot.jesari"

quality = {
    "crap": MediaMessageEventContent(
        msgtype=MessageType.IMAGE,
        body="putkiteippi.gif",
        url=ContentURI("mxc://maunium.net/IkSoSYYrtaYJQeCaABSLqKiD"),
        info=ImageInfo(
            mimetype="image/gif",
            width=364,
            height=153,
            size=2079294,
            thumbnail_url=ContentURI("mxc://maunium.net/iivOnCDjcGqGvnwnNWxSbAvb"),
            thumbnail_info=ThumbnailInfo(
                mimetype="image/png",
                width=364,
                height=153,
                size=51302,
            ),
        ),
    ),
    "low": MediaMessageEventContent(
        msgtype=MessageType.IMAGE,
        body="putkiteippi.gif",
        url=ContentURI("mxc://maunium.net/PXbFbVEmcGzkaMXwUOrzZcQM"),
        info=ImageInfo(
            mimetype="image/gif",
            width=640,
            height=267,
            size=2352044,
            thumbnail_url=ContentURI("mxc://maunium.net/QGTVCHOEqUOweASaxKQhEvyD"),
            thumbnail_info=ThumbnailInfo(
                mimetype="image/png",
                width=640,
                height=267,
                size=109306,
            ),
        ),
    ),
    "medium": MediaMessageEventContent(
        msgtype=MessageType.IMAGE,
        body="putkiteippi.gif",
        url=ContentURI("mxc://maunium.net/LNjeTZvDEaUdQAROvWGHLLDi"),
        info=ImageInfo(
            mimetype="image/gif",
            width=1280,
            height=535,
            size=7500893,
            thumbnail_url=ContentURI("mxc://maunium.net/xdhlegZQgGwlMRzBfhNxyEfb"),
            thumbnail_info=ThumbnailInfo(
                mimetype="image/png",
                width=800,
                height=334,
                size=417896,
            ),
        ),
    ),
    "high": MediaMessageEventContent(
        msgtype=MessageType.IMAGE,
        body="putkiteippi.gif",
        url=ContentURI("mxc://maunium.net/HJGpkfVWxZYaBWpOYecOiJtg"),
        info=ImageInfo(
            mimetype="image/gif",
            width=1920,
            height=802,
            size=15824736,
            thumbnail_url=ContentURI("mxc://maunium.net/iIDrkChFzwyZAXycmfZFaAbV"),
            thumbnail_info=ThumbnailInfo(
                mimetype="image/png",
                width=800,
                height=334,
                size=362611,
            ),
        ),
    ),
}


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
        await evt.respond(quality["high"])
