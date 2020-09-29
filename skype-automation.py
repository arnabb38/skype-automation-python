from skpy import Skype

_SKYPE_ID = 'Skype_User_ID'
_SKYPE_PASS = 'Skype_User_Passeord'

_CONN = Skype(_SKYPE_ID, _SKYPE_PASS)

# Getting User, Contact and Chat information 
_CONN.user
_CONN.contacts
_CONN.chats

#Setting up Receiver 
_CH = _CONN.chats["USER/GROUP_ID"]

# Sending Text Message
_CH.sendMsg("This message is automated using Python.")

# For Attachment
_CH.sendFile(open("PATH_TO_FILE", "rb"), "ENCODING_FILE_NAME")

