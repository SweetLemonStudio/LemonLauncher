import subprocess
import webbrowser
import minecraft_launcher_lib as mc
from rich.console import Console

console = Console()


def login():
    CLIENT_ID = "7bb4c098-15de-4d4c-b446-176eaddcacb7"
    REDIRECT_URL = "https://login.live.com/oauth20_desktop.srf"

    login_url, state, code_verifier = mc.microsoft_account.get_secure_login_data(CLIENT_ID, REDIRECT_URL)
    webbrowser.open(login_url)
    LastUrl = input("LLauncher@login >")
    auth_code = mc.microsoft_account.parse_auth_code_url(LastUrl, state)
    login_data = mc.microsoft_account.complete_login(CLIENT_ID, None, REDIRECT_URL, auth_code, code_verifier)
    OPTION = {"username": login_data["name"],
              "uuid": login_data["id"],
              "token": login_data["access_token"]
              }

    return OPTION


def run(version, directory, option):
    cmd = mc.command.get_minecraft_command(version, minecraft_directory=directory, options=option)
    subprocess.call(cmd)


def install(version, directory):
    mc.install.install_minecraft_version(version, directory)
