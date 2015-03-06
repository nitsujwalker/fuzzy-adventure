#Sends the current file text to 1Writer.
#Designed for Pythonista, but should word with Editorial
#Can be edited to suit your purposes

import editor
import webbrowser
from urllib import quote
import console

file = str(editor.get_text())

text = quote(file)

button = True


#Uses Pythonista's graphical alert system to name file upon sending
while button == True:
	name = console.input_alert('Before you go', 'Please give a title for the document')

	if len(name) < 1 or ' ' in name:
		i = console.alert('Uh Oh!', "Please enter your title: use '_' for spaces", "OK")

	else:
		button = False

#change the x-callback URL below to open in another compatible app.
open_in_app = 'onewriter://x-callback-url/create?name=%s&text=%s' % (name, text)

webbrowser.open(open_in_app)
