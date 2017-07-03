from microsoftbotframework import ReplyToActivity
import requests

def echo_response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=message["text"]).send()


def cost_search(message):
  res = requests.get("https://api.korbit.co.kr/v1/ticker")
  res.json()

  last = res['last']

  msg = "last cost : {}".format(last)

  if message["type"] == "message" and message["text"] == "bitcoin":
    ReplyToActivity(fill=message,
                    text=msg).send()