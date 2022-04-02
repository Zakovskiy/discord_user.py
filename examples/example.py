from discord_user import discord_user

DS = discord_user.Client("your email", "your password");

# get servers
servers_list = DS.list_guilds();

# get server channels
server_channels_list  = DS.guild_channels(servers_list[0]["id"]);

# select channel_id
channel_id = server_channels_list[0]["id"];

# send message in the channel
DS.send_message("hello everyone", channel_id);
