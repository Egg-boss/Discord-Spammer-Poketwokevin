from webserver import keep_alive
import requests

channelID = 1320333008712110100
headers = {
    "AUTHOIRIZATION":
    MTMyMDMzMzQ4NTA2NzYwNDA1OA.G3s3mf.BcbjtQmk1L7DwSJdHHr9QGRkHXfaGyX5Nl3KPg
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
