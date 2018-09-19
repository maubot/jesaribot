FROM maubot/plugin-base AS builder

COPY . /go/src/maubot.xyz/jesaribot
RUN go build -buildmode=plugin -o /maubot-plugins/jesaribot.mbp maubot.xyz/jesaribot

FROM alpine:latest
COPY --from=builder /maubot-plugins/jesaribot.mbp /maubot-plugins/jesaribot.mbp
VOLUME /output
CMD ["cp", "/maubot-plugins/jesaribot.mbp", "/output/jesaribot.mbp"]
