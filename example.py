import discorduser

# auth
DS = discorduser.Client("your email", "your password");

# get servers
servers_list = DS.list_guilds();

# get server channels
server_channels_list  = DS.guild_channels(servers_list[4]["id"]);

# saving select channel_id
channel_id = server_channels_list[2]["id"];

# send message in the channel
DS.send_message("hello everyone", channel_id);
