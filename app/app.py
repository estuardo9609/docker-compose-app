from flask import Flask, request
import os
import redis

app = Flask(__name__)

r = redis.Redis()

redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
  return "I will save whatever message you give me. Send me the key and your message at /remember/[key]/[message]. To get the message just type the key of your message at /message/[key]."

@app.route("/remember/<key>/<message>")
def remeber(key, message):
  r.set(key,message)
  return "I saved your message with the key: %s" % key

@app.route("/message/<key>")
def message(key):
  my_message = r.get(key)
  return "Your message was: %s" % my_message


if __name__ == "__main__":
  app.run(host='0.0.0.0', port="3000")