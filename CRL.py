# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bacalhau_Bot.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jbuny-fe <jbuny-fe@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/30 11:31:29 by jbuny-fe          #+#    #+#              #
#    Updated: 2022/05/12 12:05:50 by jbuny-fe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import discord
import datetime
import os
import sys
import time
import toml
import threading
import requests
import json

client = discord.Client()
issue_list = ["issue", "issues", "problem", "problems"]
how_list = ["how to", "how do i", "i'm having problems", "im having problems", "im having a", "i'm having a"]
thanks = ["thank you", "thank u", "thanks"]
bacalhau = ["bacalhau", "bacalhau"]
sorry = ["Sorry", "sorry"]
gm = ["gm", "good morning"]
hey = ["hey", "hello", "heyy"]

def timer():  # starts once the program is started
    try:
        with open('time_keeper', 'r') as f:  # opens a time_keeper file if it already exists
            tk = toml.load(f)
            seconds = tk["seconds"]
            f.close()
            while True:
                time.sleep(1)
                seconds += 1
                global time_active  # time active to show in the console
                time_active = (str(int(seconds)))
                if stop == True:
                    break
                with open('time_keeper',
                          'w') as tk:  # updates the time_keeper file so that is doesn't loose time once the program
                    # is closed
                    tk.write('seconds = ' + str(seconds) + '\n')
                    tk.close()
    except:  # Creates a new time_keeper file if one isn't found
        with open("time_keeper", 'w') as f:
            s = 0
            f.write('seconds = ' + str(int(s)) + '\n')
            f.close()

@client.event
async def on_ready():
    channel = client.get_channel(977697637350375464)
    print("bacalhau is starting up! ⚡️")
    await channel.send("Starting up! ⚡️")
    log_exists = os.path.exists("Log")
    if log_exists == True:
        print("Log file found! ✅")
        await channel.send("Log file found! ✅")
    else:
        print("No log file found❌, creating a log file📝")
        await channel.send("No log file found❌, creating a log file📝")
        try:
            with open("log", 'w') as log:
                log.write("Log file started on" + str(datetime.now()) + "\n")
            print("Log file successfully created! ✅")
            await channel.send("Log file successfully created! ✅")
        except:
            print("Unable to create a log file, please check permissions and space left on device.❌")
            await channel.send("Unable to create a log file, please check permissions and space left on device.❌")
            pass
    await channel.send("All systems online, bacalhau is up and running 🦾")
    print('{0.user} is now online! ✅\n'.format(client))

async def responses(message, userid, user):
    Admins = ["El Madeirense", "Garrett"]
    if message.author == client.user:
        return
    for word in thanks:
        if word in message.content.lower():
            thanks_true = True
            break
        else:
            thanks_true = False
    for word in issue_list:
        if word in message.content.lower():
            issue_True = True
            break
        else:
            issue_True = False
    for word in how_list:
        if word in message.content.lower():
            how_to = True
            break
        else:
            how_to = False
    for word in bacalhau:
        if word in message.content.lower():
            bacalhau_true = True
            break
        else:
            bacalhau_true = False
    for word in sorry:
        if word in message.content.lower():
            sorry_true = True
            break
        else:
            sorry_true = False
    for word in gm:
        if word in message.content.lower():
            gm_true = True
            break
        else:
            gm_true = False
    for word in hey:
        if word in message.content.lower():
            hey_true = True
            break
        else:
            hey_true = False
    if message.content.startswith(("hello there", "Hello there")):
        await message.channel.send("General Kenobi")
    if hey_true and bacalhau_true:
        await message.channel.send("Hey there! " + f"<@{userid}>" + ". What's up?👋")
    if message.content.startswith(('bacalhau.help', "bacalhau.help")):
        embed=discord.Embed(title="**Here are a few commands you can use with me:**",
        description="**User commands:**\n\
                **   - bacalhau.wiki -->** Sends the link to the bacalhau In The Sky wiki and FAQs\n\
                **   - bacalhau.login -->** Sends the link the the bacalhau In The Sky login page\n\
                **   - bacalhau.calendar -->** Sends the link to the Google Calendar events on the Live Sessions \n\
                **   - bacalhau.progress -->** Shows the current Journey progress in time %\n\
                **   - bacalhau.uptime -->** Shows how long I've been awake for\n\
                **   - bacalhau.take five -->** I'll go to sleep for five minutes, in case you want to say my name without calling me\n\
        **Admin only commands:**\n\
                **   - bacalhau.purge -->** Deletes all the messages in the current channel\n\
                **   - bacalhau.log-file -->** Sends the last 10 messages in the log file\n\
                **   - bacalhau.reboot -->** Reboots me in case I'm doing something I'm not supposed to \n\
                **   - bacalhau.STOP! -->** Completely shuts me down, should only be used as a last resort \n",
        color=discord.Color.blue())
        await message.channel.send("Heyy " + f"<@{userid}>" + "\n",embed=embed)
    if message.content.startswith(("bacalhau.login", "bacalhau.login")):
        embed=discord.Embed(title="bacalhau In The Sky login page",
        url="https://go.bacalhauinthesky.education/learn/login", 
        description="Welcome to the bacalhau In The Sky Platform", 
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://media-exp1.licdn.com/dms/image/C4D0BAQE6Qyi6gobkNg/company-logo_200_200/0/1635152143581?e=2147483647&v=beta&t=JNhdpt_fKozF3-AnxO9T9b3DOsrZN2aJsQjXJxWFwcY")
        await message.channel.send(f"<@{userid}>", embed=embed)
    if message.content.startswith(("bacalhau.calendar", "bacalhau.calendar")):
        embed=discord.Embed(title="Live Sessions Calendar",
        url="https://calendar.google.com/event?action=TEMPLATE&tmeid=MXNkbGowb3NuczQ1bmlzMGdlZGVxbHQ2ZXFfMjAyMjA1MTJUMTgwMDAwWiBjb21tdW5pdHktbWFuYWdlbWVudEBtaWxlc2ludGhlc2t5LmVkdWNhdGlvbg&tmsrc=community-management%40bacalhauinthesky.education&scp=ALL", 
        description="Hey " + f"<@{userid}>" + ", here you have the calendar for the Live Sessions of this Jorney", 
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://logosmarcas.net/wp-content/uploads/2021/04/Google-Calendar-Logo.png")
        await message.channel.send(f"<@{userid}>", embed=embed)
    if message.content.startswith(('bacalhau.wiki', 'bacalhau.wiki')):
        embed=discord.Embed(title="bacalhau Wiki",
        url="https://demo.bacalhauinthesky.education/learn/wiki/digital-experience-part-time-april-2022", 
        description="Hey " + f"<@{userid}>" + ", here you have the bacalhau In The Sky Platform wiki and FAQs", 
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://media-exp1.licdn.com/dms/image/C4D0BAQE6Qyi6gobkNg/company-logo_200_200/0/1635152143581?e=2147483647&v=beta&t=JNhdpt_fKozF3-AnxO9T9b3DOsrZN2aJsQjXJxWFwcY")
        await message.channel.send(f"<@{userid}>", embed=embed)
    if message.content.startswith("bacalhau.git"):
        embed=discord.Embed(title="BunyMan's GitHub",
        url="https://github.com/BunyMan",
        description="Hey " +f"<@{userid}>" + ", my code isn't on GitHub but you can check other projects from my creator!",
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/25/25231.png")
        await message.channel.send(f"<@{userid}>", embed=embed)
    if user in Admins and message.content.startswith(("bacalhau.reboot", "bacalhau.reboot", "bacalhau, reboot")):
        await message.channel.send("Rebooting process inicialized! ❌ bacalhau will be down for a few seconds")
        print("bacalhau is rebooting...")
        await message.channel.send("Shutting down... ☠️ ")
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif user not in Admins and message.content.startswith(("bacalhau.reboot", "bacalhau.reboot", "bacalhau, reboot")):
        await message.channel.send("Hey " + f"<@{userid}>"+ ", that's an admin only command!")
    if user in Admins and message.content.startswith(("bacalhau.take five", "bacalhau, take five")):
       await message.channel.send("I'll be back!")
       time.sleep(300)
       await message.channel.send("My 5 minutes are up, I'm back!")
    elif user not in Admins and message.content.startswith(("bacalhau.take five", "bacalhau, take five")):
        await message.channel.send("Hey " + f"<@{userid}>"+ ", that's an admin only command!")
    if message.content.startswith("bacalhau.uptime") or message.content.startswith("bacalhau.uptime"):
        with open("time_keeper", 'r') as f:
            tk = toml.load(f)
            seconds = tk["seconds"]
            f.close()
            await message.channel.send("I've been awake for " + str(seconds) + " seconds, now do the math.")
    if message.content.startswith("bacalhau.norris"):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        json_data = json.loads(response.text)
        quote = json_data["value"]
        await message.channel.send(str(quote))
    if user in Admins and message.content.startswith(("bacalhau.log-file", "bacalhau.log-file")):
        with open("Log") as f:
            for line in (f.readlines() [-10:]):
                await message.channel.send(line)
        await message.channel.send(line)
    elif user not in Admins and message.content.startswith(("bacalhau.log-file", "bacalhau.log-file")):
        await message.channel.send("Hey, " + f"<@{userid}>" + ", only admins can use that command!")
    if "bacalhau?" in message.content or "bacalhau?" in message.content:
        await message.channel.send("I'm alive! Kinda... 🤖")
    if gm_true:
        await message.channel.send("Good morning!!🌞")
    if thanks_true and bacalhau_true:
        await message.channel.send("You're welcome, " + f"<@{userid}>" + " !")
    if sorry_true and bacalhau_true:
        await message.channel.send("No problem, " + f"<@{userid}>" + ". Don't worry about it!")
    if message.content.startswith(("bacalhau.progress", "bacalhau.progress", "bacalhau, progress", "bacalhau, progress")):
        start = datetime.date(2022,4,29)
        today = datetime.date.today()
        future = datetime.date(2022,5,30)
        time_since_start = today - start
        progress = future - today
        rd1 = str(progress)
        rd2 = str(time_since_start)
        await message.channel.send("Your Journey has started " + rd2[0:7] + " ago and you have " + rd1[0:7] + " left until the end of this Journey! Keep it up! 💪")
    if ("login" in message.content) and (issue_True):
        await message.channel.send("Hey " +f"<@{userid}>"+ ", if you're having issues with login you can either talk to us about it in the #support(https://discord.com/channels/961277429383594014/961277429383594022)  channel or send us an email at community-management@bacalhauinthesky.education")
    if message.content.startswith("ping"):
        await message.channel.send("pong 🏓")
    if how_to:
        await message.channel.send("If you're having platform related issues, you cant try to find a solution in the wiki, here is the link 🌍: ")
        embed=discord.Embed(title="bacalhau Wiki",
        url="https://demo.bacalhauinthesky.education/learn/wiki/digital-experience-part-time-april-2022", 
        description="Hey " + f"<@{userid}>" + ", here you have the bacalhau In The Sky Platform wiki and FAQs", 
        color=discord.Color.blue())
        embed.set_thumbnail(url="https://media-exp1.licdn.com/dms/image/C4D0BAQE6Qyi6gobkNg/company-logo_200_200/0/1635152143581?e=2147483647&v=beta&t=JNhdpt_fKozF3-AnxO9T9b3DOsrZN2aJsQjXJxWFwcY")
        await message.channel.send(f"<@{userid}>", embed=embed)
    if user in Admins and message.content.startswith("bacalhau.purge") or message.content.startswith("Bacalhau.purge"):
        await message.channel.send("🐟")
        time.sleep(1)
        await message.channel.purge()
    elif user not in Admins and message.content.startswith("bacalhau.purge") or message.content.startswith("Bacalhau.purge"):
        await message.channel.send("Hey, " + f"<@{userid}>" + ", only admins can use that command!")
    
@client.event
async def on_message(message):
    threading.Thread(target=timer).start()
    user = message.author.name
    userid = message.author.id
    global stop
    stop = False
    try:
        try:
            with open("Log", 'a') as log:
                log.write(user + " --> on " + str(datetime.datetime.now()) + " -->  " + str(message.content) + "\n")
                log.close
        except:
            print("Unable to write to log file ❌")
        try:
            print(user + " --> on " + str(datetime.datetime.now()) + " --> '" + str(message.content) + "'")
        except:
            print(user)
    except:
        print("Couldn't get username")
    if user == "El Madeirense" and message.content.startswith("bacalhau.STOP!") or message.content.startswith("bacalhau.STOP!") or message.content.startswith("bacalhau, STOP!") or message.content.startswith("bacalhau, STOP!"):
        await message.channel.send("🎣")
        stop = True
        time.sleep(1)
        exit()
    elif user != "El Madeirense" and message.content.startswith("bacalhau.STOP!") or message.content.startswith("bacalhau.STOP!") or message.content.startswith("bacalhau, STOP!") or message.content.startswith("bacalhau, STOP!"):
        await message.channel.send("Hey " + f"<@{userid}>" + ", only admins can use that command!")
    try:
        await responses(message, userid, user)
    except:
        await message.channel.send(f"<@{userid}>" + " Oops, that didn't work! Please report this :)")
        print("Warning, something failed. Please check for user report.")

client.run('OTczNTY1NjI3MjkxODIwMDQy.GVL7cp.pdUGL8WLhbZZPVksyXskgI8R4Kf4ZYCwH1zgN8')
