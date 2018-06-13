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
	"encoding/json"
	"strings"

	"maubot.xyz"
	"maubot.xyz/database"
	"maubot.xyz/matrix"
	"maunium.net/go/gomatrix"
)

type JesariBot struct {
	client *matrix.Client
}

func (bot *JesariBot) Start() {
	bot.client.AddEventHandler(gomatrix.EventMessage, bot.MessageHandler)
}

func (bot *JesariBot) Stop() {}

func (bot *JesariBot) MessageHandler(evt *gomatrix.Event) {
	text, _ := evt.Content["body"].(string)
	if strings.Contains(strings.ToLower(text), "jesari") {
		bot.client.SendMessageEvent(evt.RoomID, "m.room.message", json.RawMessage(`{
  "body": "putkiteippi.gif",
  "info": {
    "mimetype": "image/gif",
    "thumbnail_info": {
      "mimetype": "image/png",
      "h": 153,
      "w": 364,
      "size": 51302
    },
    "h": 153,
    "thumbnail_url": "mxc://maunium.net/iivOnCDjcGqGvnwnNWxSbAvb",
    "w": 364,
    "size": 2079294
  },
  "msgtype": "m.image",
  "url": "mxc://maunium.net/IkSoSYYrtaYJQeCaABSLqKiD"
}`))
	}
}

var Plugin = maubot.PluginCreator{
	Create: func(bot *maubot.Bot, info *database.Plugin, client *matrix.Client) maubot.Plugin {
		return &JesariBot{
			client: client,
		}
	},
	Name:    "jesaribot",
	Version: "1.0.0",
}
