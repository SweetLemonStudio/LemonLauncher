import configparser

import minecraft_launcher_lib as mc
from rich.console import Console
import defined

crp = configparser.ConfigParser()
crp.read("data.ini")
RootDirectory = crp.get("LauncherSettings", "directory")
console = Console()

console.print("Hello World!", style='bold green')
console.print("This is [bold green]LemonLauncher[/bold green]![bold red]Welcome~[/bold red]:smiley:")
console.print("[i]enjoy your self~[/i]")
crp.read("data.ini")

CLIENT_ID = "7bb4c098-15de-4d4c-b446-176eaddcacb7"
REDIRECT_URL = "https://login.live.com/oauth20_desktop.srf"
OPTION = ''


while True:
    command = input('LemonLancher@root >')
    if "login" in command:
        OPTION = defined.login()

    elif "run" in command:
        console.print("You will start minecraft. Enter a [bold red]version[/bold red]!↓")
        StartVersion = input("LLauncher@run >")
        defined.run(StartVersion, RootDirectory, OPTION)

    elif "quit" in command:
        console.print("LemonLauncher will quit", style='blue')
        console.print("Bye~", style='green')
        quit()

    elif 'install' in command:
        if RootDirectory == '':
            print('Please set the game directory at the first!')
        else:
            console.print(
                'What Minecraft version would you want to install? Input at [gold red]below[/gold red],please.')
            WantToInstall = input('LLauncher@installer>')
            console.print("Minecraft is installing please wait.", style='blue')
            console.print("Installation time is about 3-5 minutes", style='green')
            defined.install(WantToInstall, RootDirectory)
            console.print("Minecraft installing [gold green]finished[/gold green]. [gold blue]Enjoy yourself!["
                          "/gold blue]")

    elif 'set_game_directory' in command:
        RootDirectory = input('GameDirectorySetting >')
        crp.set("LauncherSettings", "directory", RootDirectory)
        with open("data.ini", "w+") as f:
            crp.write(f)

    elif "help" in command:
        console.print("[bold blue]run[/bold blue]-->start minecraft")
        console.print("[bold blue]login_offline[/bold blue]-->add a Offline account")
        console.print("[bold blue]Login_Microsoft[/bold blue]-->add a Microsoft account")
        console.print("[bold blue]install[/bold blue]-->install a minecraft")
        console.print("[bold blue]quit_Launcher[/bold blue]-->quit LemonLauncher")
        console.print("[bold blue]set_game_directory[/bold blue]-->set Game Directory")

    else:
        console.print("Maybe something was wrong", style='red')
