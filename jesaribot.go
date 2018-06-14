// jesaribot - A simple maubot plugin.
// Copyright (C) 2018 Tulir Asokan
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>. 

package main

import (
	"strings"

	"maubot.xyz"
)

type JesariBot struct {
	client maubot.MatrixClient
}

func (bot *JesariBot) Start() {
	bot.client.AddEventHandler("m.room.message", bot.MessageHandler)
}

func (bot *JesariBot) Stop() {}

func (bot *JesariBot) MessageHandler(evt *maubot.Event) maubot.EventHandlerResult {
	if strings.Contains(strings.ToLower(evt.Content.Body), "jesari") {
		evt.ReplyContent(maubot.Content{
			Body: "putkiteippi.gif",
			Info: maubot.FileInfo{
				MimeType: "image/gif",
				ThumbnailInfo: &maubot.FileInfo{
					MimeType: "image/png",
					Height: 153,
					Width: 364,
					Size: 51302,
				},
				ThumbnailURL: "mxc://maunium.net/iivOnCDjcGqGvnwnNWxSbAvb",
				Height: 153,
				Width: 364,
				Size: 2079294,
			},
			MsgType: maubot.MsgImage,
			URL: "mxc://maunium.net/IkSoSYYrtaYJQeCaABSLqKiD",
		})
	}
	return maubot.Continue
}

var Plugin = maubot.PluginCreator{
	Create: func(client maubot.MatrixClient) maubot.Plugin {
		return &JesariBot{
			client: client,
		}
	},
	Name:    "maubot.xyz/jesaribot",
	Version: "1.0.0",
}
