from skpy import Skype

_SKYPE_ID = ''
_SKYPE_PASS = ''

_CONN = Skype(_SKYPE_ID, _SKYPE_PASS)

_CONN.user
_CONN.contacts
_CONN.chats

print(_CONN.chats.recent())

_CH = _CONN.chats["19:c096722edf1343d5a3dbc8420910e50a@thread.skype"]
_CH.sendMsg("Hey there, this is a test message!")
_CH.sendFile(open("/home/arnabb/Documents/satuday-school/2-python-automation/saturday.jpg", "rb"), "saturday.jpg")

