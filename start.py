from telethon import TelegramClient, events, sync
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel

FOLLOW = ["ipomogator"]
FOLLOW_PRIVATE = ["AAAAAFFULXxCe-AVQxy9Fw"] 

def main():
    api_id = 1018957
    api_hash = '4b0f0fe8a71dbff9a4422dc1ab43d4f2'
    client = TelegramClient('me', api_id, api_hash)
    client.start()
    for follow_name in FOLLOW:
        channel  = client(ResolveUsernameRequest(follow_name))
        client(JoinChannelRequest(channel))
    for follow_hash in FOLLOW_PRIVATE:
        client(ImportChatInviteRequest(hash = follow_hash))
if __name__ == '__main__':
    main()