from microsoftbotframework import ReplyToActivity
import requests


def echo_response(message):
  if message["type"] == "message":
    ReplyToActivity(fill=message,
                    text=message["text"]).send()


def cost_search(message):

  msg = search()
  if message["type"] == "message":
    if message["text"] == "bitcoin":
      ReplyToActivity(fill=message,
                      text=msg).send()
    else:
      ReplyToActivity(fill=message,
                      text=message["text"]).send()


def search():
  res = requests.get("https://api.korbit.co.kr/v1/ticker")

  t = str(res.text)
  res_dict = eval(t)

  last = res_dict.get('last')

  msg = "last cost : {}".format(last)
  print (msg)
  return msg
