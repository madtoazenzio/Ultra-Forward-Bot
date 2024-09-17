from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return '@ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ꜱᴇʀɪᴇꜱ'


if name == "main":
    app.run()
