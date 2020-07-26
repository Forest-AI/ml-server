import pyrebase


class Database(object):
	
	"""
	Firebase Configuration and Credentials
	"""
	firebaseConfig = {
    		"apiKey": "AIzaSyDdroMu06jPnQKbF7p2w7ZYyJox4fYwH-M",
    		"authDomain": "forest-ai-console.firebaseapp.com",
    		"databaseURL": "https://forest-ai-console.firebaseio.com",
    		"projectId": "forest-ai-console",
    		"storageBucket": "forest-ai-console.appspot.com",
    		"messagingSenderId": "521367617950",
    		"appId": "1:521367617950:web:d0cfdeafea8294e2a1168f",
    		"measurementId": "G-SKZG9E8CD6"}




	"""
	Initializing the firebase connection with configuration.
	Firebase storage path and download directory path is defined here.
	"""
	def __init__(self):
		self.__storage = pyrebase.initialize_app(self.firebaseConfig).storage()
		self.__downloadDirectory = "model//downloads"	



	"""
	Method to fetch and store the audio file into the download directory
	"""
	def download(self, audio_id):
		self.__storage.child(audio_id).download("data//audio.wav")
	
	


