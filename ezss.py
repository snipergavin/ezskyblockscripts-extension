import os, sys, json, time, ctypes
try:
    import discord, keyboard, requests
    import pyautogui as pt
    from pynput.mouse import Controller
    from discord.ext import commands
    mouse = Controller()
except:
    os.system("pip install discord")
    os.system("pip install keyboard")
    os.system("pip install requests")
    os.system("pip install pyautogui")
    os.system("pip install pynput")
    os.system("pip install opencv-python")
    os.system("pip install pillow")
    python = sys.executable
    os.execl(python, python, * sys.argv)

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW(f"ezSkyblockScripts Extension")

def download_file(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1].replace(" ", "_")
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        pass

config= {
    "Main": {
        "Prefix": ".",
        "Discord Token": "token here",
        "Script Start Key": "key here",
    }
}

if not os.path.exists("buttons"):
    os.makedirs("buttons")
if not os.path.exists("buttons/cobblestone.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566425579184178/cobblestone.png", "./buttons")
if not os.path.exists("buttons/fishing.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566425809879050/fishing.png", "./buttons")
if not os.path.exists("buttons/horizontal.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566426086674543/horizontal.png", "./buttons")
if not os.path.exists("buttons/netherwart.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566426497728532/netherwart.png", "./buttons")
if not os.path.exists("buttons/pumpkin.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566426820706314/pumpkin.png", "./buttons")
if not os.path.exists("buttons/sugarcane.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566425101025301/sugarcane.png", "./buttons")
if not os.path.exists("buttons/vertical.png"):
    download_file("https://cdn.discordapp.com/attachments/929085488848044045/948566425390415902/vertical.png", "./buttons")

if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    print("config created. Please setup config, then restart.")
    time.sleep(3)
    os._exit(0)

with open("config.json") as f:
    config = json.load(f)
    prefix=config["Main"]["Prefix"]
    token=config["Main"]["Discord Token"]
    button=config["Main"]["Script Start Key"]

if token=="token here" or "":
    print("Please enter discord token in config.json.")
    time.sleep(3)
    os._exit(0)
if button=="key here" or "":
    print("Please enter key in config.json.")
    time.sleep(3)
    os._exit(0)
if len(button)!=1:
    print("Your start key cant be correct! Please double check your config.json.")
    time.sleep(3)
    os._exit(0)
r=requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"})
if r.status_code!=200:
    print("Invalid token, please make sure to reenter a valid discord token.")
    time.sleep(3)
    os._exit(0)

bot = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True)
bot.remove_command("help")

def nav_to_image(image, clicks, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=.8)

    if position is None:
        print(f"{image} not found.")
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.2)
        pt.click(clicks=clicks, interval=.1)

creds=requests.get('https://pastebin.com/raw/Yt2Mmeqw').text
current_farming="nothing"

@bot.event
async def on_connect():
    os.system("cls")
    print("Discord connected to: "+bot.user.name+"#"+bot.user.discriminator)
    print("Script is ready")

@bot.command()
async def stop(et):
    await et.message.delete()
    if current_farming!="nothing":
        print(f"stopped farming {current_farming}")
        await et.send(f"```Stopped farming {current_farming}```")
        keyboard.press_and_release(button)
    else:
        await et.send("```You cant stop farming nothing!```")

@bot.command()
async def sugarcane(et):
    await et.message.delete()
    print(f"started sugarcane")
    time.sleep(1)
    keyboard.press_and_release(button)
    time.sleep(.5)
    nav_to_image("buttons/sugarcane.png", 1)
    global current_farming
    current_farming="sugarcane"
    await et.send("```Started farming sugarcane```")

@bot.command()
async def netherwart(et, style):
    await et.message.delete()
    time.sleep(1)
    keyboard.press_and_release(button)
    time.sleep(.5)
    nav_to_image("buttons/netherwart.png", 1)
    global current_farming
    current_farming="netherwart"
    if style=="sshape":
        time.sleep(.5)
        nav_to_image("buttons/horizontal.png", 1)
        print(f"started farming netherwart in s shape")
        await et.send("```Started farming netherwart in s shape```")
    else:
        time.sleep(.5)
        nav_to_image("buttons/vertical.png", 1)
        print(f"started farming netherwart vertically")
        await et.send("```Started farming netherwart vertically```")

@bot.command()
async def fishing(et):
    await et.message.delete()
    print(f"started fishing")
    time.sleep(1)
    keyboard.press_and_release(button)
    time.sleep(.5)
    nav_to_image("buttons/fishing.png", 1)
    global current_farming
    current_farming="fish"
    await et.send("```Started fishing```")

@bot.command()
async def cobblestone(et):
    await et.message.delete()
    print(f"started cobblestone")
    time.sleep(1)
    keyboard.press_and_release(button)
    time.sleep(.5)
    nav_to_image("buttons/cobblestone.png", 1)
    global current_farming
    current_farming="cobblestone"
    await et.send("```Started farming cobblestone```")

@bot.command()
async def pumpkin(et):
    await et.message.delete()
    print(f"started pumpkin")
    time.sleep(1)
    keyboard.press_and_release(button)
    time.sleep(.5)
    nav_to_image("buttons/pumpkin.png", 1)
    global current_farming
    current_farming="pumpkin"
    await et.send("```Started farming pumpkin```")

@bot.command()
async def screenshot(et):
    await et.message.delete()
    ss=pt.screenshot()
    ss.save("screenshot.png")
    with open("screenshot.png", "rb") as file:
        await et.send(file=discord.File(file, "screenshot.png"))
    os.remove("screenshot.png")

@bot.command()
async def shutdown(et, cooldown: int=0):
    await et.message.delete()
    await et.send(f"```Shutting down pc in {cooldown} seconds!")
    os.system(f"shutdown -s -t {cooldown}")

@bot.command(aliases=["reboot", "reload"])
async def restart(et):
    await et.message.delete()
    python = sys.executable
    os.execl(python, python, * sys.argv)

@bot.command()
async def help(et):
    await et.message.delete()
    await et.send(f"""```fix\n[ezSkyblockScripts Extension]``````INI\n[Farming Modes]
{prefix}netherwart <sshape/vertical> » start netherwart
{prefix}sugarcane » start sugarcane
{prefix}fishing » start fishing
{prefix}cobblestone » start cobblestone
{prefix}pumpkin » start pumpkin
{prefix}stop » stop any active script``````INI\n[Remote Access Utility]
{prefix}screenshot » send screenshot of pc
{prefix}shutdown <None/Timer> » shutdown pc with optional timer
{prefix}restart » restart this script``````Credits: {creds}```""")


bot.run(token, bot=False)
