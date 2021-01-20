'''
# TG  = https://t.me/zakovskiy
# Git = https://github.com/Zakovskiy
# Vk  = https://vk.com/id514492216
'''

import json
import requests
import random
import time

class Client():

	def __init__(self, email:str = None, password:str = None):
		self.api = "https://discord.com/api/v8/";
		self.headers = {'Content-Type': 'application/json',
						'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDkiLCJvc192ZXJzaW9uIjoiNi4xLjc2MDEiLCJvc19hcmNoIjoieDY0IiwiY2xpZW50X2J1aWxkX251bWJlciI6NzQwMDgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
						'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'};
		self.login(email, password);

	def login(self, email:str = None, password:str = None):
		response = requests.post(f"{self.api}auth/login", headers={'content-type': 'application/json'}, data=json.dumps({"login":email,"password":password,"undelete":False,"captcha_key":None,"login_source":None,"gift_code_sku_id":None})).json();
		try:
			self.token = response["token"];
			self.headers['Authorization'] = response["token"];
		except:
			exit(response);
		return response;

	def logout(self):
		response = requests.post(f"{self.api}auth/logout", data=json.dumps({"provider":None,"voip_provider":None}), headers=self.headers).json();
		return response;

	def affinities_users(self):
		response = requests.get(f"{self.api}users/@me/affinities/users", headers=self.headers).json();
		return response;

	# return your guilds(servers) list
	def list_guilds(self):
		response = requests.get(f"{self.api}users/@me/guilds", headers=self.headers).json();
		return response;

	# return info about guild(server)
	def guild_info(self, guild_id:int = 0):
		response = requests.get(f"{self.api}guilds/{guild_id}", headers=self.headers).json();
		return response;

	# return list channels from guild(server)
	def guild_channels(self, guild_id:int = 0):
		response = requests.get(f"{self.api}guilds/{guild_id}/channels", headers=self.headers).json();
		return response;

	# return your dialogs with users
	def list_channels(self):
		response = requests.get(f"{self.api}users/@me/channels", headers=self.headers).json();
		return response;

	def leave_guild(self, guild_id:int = 0):
		response = requests.delete(f"{self.api}users/@me/guilds/{guild_id}", headers=self.headers).json();
		return response;

	def leave_channel(self, channel_id:int = 0):
		response = requests.delete(f"{self.api}users/@me/channels/{channel_id}", headers=self.headers).json();
		return response;

	def discoverable_guilds(self, offset:int=0, limit:int=24):
		response = requests.get(f"{self.api}discoverable-guilds?offset={offset}&limit={limit}", headers=self.headers).json();
		return response;

	def all_friends(self):
		response = requests.get(f"{self.api}users/@me/relationships", headers=self.headers).json();
		return response;

	def user_info(self, user_id:int = 0):
		response = requests.get(f"{self.api}users/{user_id}/profile", headers=self.headers).json();
		return response;

	def delete_friend(self, user_id:int = 0):
		response = requests.delete(f"{self.api}users/@me/relationships/{user_id}", headers=self.headers).json();
		return response;

	def typing_active(self, channel_id:int = 0):
		response = requests.get(f"{self.api}channels/{channel_id}/typing", headers=self.headers).json();
		return response;

	def change_username(self, name:str = "Фан Зака"):
		response = requests.patch(f"{self.api}users/@me", data=json.dumps({"password": self.password, "username": name}),
							 headers=self.headers).json()
		return response;

	def change_status(self, emoji:str = None, text:str = None):
		response = requests.patch(f"{self.api}users/@me/settings",
							 data=json.dumps({"custom_status": {"emoji_name": emoji, "text": text}}),
							 headers=self.headers).json()
		return response;

	def send_message(self, content:str = None, channel_id:int = None):
		response = requests.post(f"{self.api}channels/{channel_id}/messages", data=json.dumps({"content":content,"nonce":random.randint(100000000000000000,900000000000000000),"tts":False}), headers=self.headers).json();
		return response;

	def delete_message(self, message_id:int = 0, channel_id:int = 0):
		response = requests.delete(f"{self.api}channels/{channel_id}/messages/{message_id}", headers=self.headers).json();
		return response;

	def channel_messages(self, channel_id:int = 0):
		response = requests.get(f"{self.api}channels/{channel_id}/messages", headers=self.headers).json();
		return response;
