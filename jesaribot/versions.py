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
from typing import Dict

from mautrix.types import (MessageType, MediaMessageEventContent, ImageInfo, ThumbnailInfo,
                           ContentURI)

gif_versions: Dict[str, MediaMessageEventContent] = {
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
