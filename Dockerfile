FROM maubot/plugin-base

COPY . /go/src/maubot.xyz/jesaribot
CMD ["go", "build", "-buildmode=plugin", "-o", "/output/jesaribot.mbp", "maubot.xyz/jesaribot"]
