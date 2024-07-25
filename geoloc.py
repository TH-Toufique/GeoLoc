# This is an opensource project. Modify according to your need if you want. Give proper credit

import pyfiglet
import time
import sys
import requests
import random
from colorama import init, Fore

#Initialize colorama
init()

# Create ascii banner
ascii_banner = pyfiglet.figlet_format("GeoLoc")
credit = "By Ripp3r \n"
full_banner = ascii_banner + "\n" + credit

def type_animation(text, delay=0.01, color = Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(Fore.RESET)

# Split the banner into lines and animate each line
for line in full_banner.split('\n'):
    type_animation(line)

# Fetch location data from ipgeolocation.io API
def fetch_location(api_key, identifier):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={identifier}"
    response = requests.get(url)
    data = response.json()
    return data

# Print fetched location data with random colors
def print_colored(key, value):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    color = random.choice(colors)
    print(color + f"{key}: {value}" + Fore.RESET)

def display_location_data(location_data):
    print_colored("IP", location_data.get('ip'))
    print_colored("Hostname", location_data.get('hostname'))
    print_colored("Continent", location_data.get('continent_name'))
    print_colored("Country", f"{location_data.get('country_name')} ({location_data.get('country_code3')})")
    print_colored("State/Province", location_data.get('state_prov'))
    print_colored("District", location_data.get('district'))
    print_colored("City", location_data.get('city'))
    print_colored("Zipcode", location_data.get('zipcode'))
    print_colored("Latitude", location_data.get('latitude'))
    print_colored("Longitude", location_data.get('longitude'))
    print_colored("Is EU", 'Yes' if location_data.get('is_eu') else 'No')
    print_colored("Calling Code", location_data.get('calling_code'))
    print_colored("Country TLD", location_data.get('country_tld'))
    print_colored("Languages", location_data.get('languages'))
    print_colored("ISP", location_data.get('isp'))
    print_colored("Organization", location_data.get('organization'))
    print_colored("ASN", location_data.get('asn'))
    print_colored("Currency", f"{location_data.get('currency').get('name')} ({location_data.get('currency').get('code')}) {location_data.get('currency').get('symbol')}")
    print_colored("Time Zone", location_data.get('time_zone').get('name'))
    print_colored("Current Time", location_data.get('time_zone').get('current_time'))
    print_colored("Is DST", 'Yes' if location_data.get('time_zone').get('is_dst') else 'No')
    print_colored("DST Savings", f"{location_data.get('time_zone').get('dst_savings')} hour(s)")

def main():
    # Replace with your actual API key
    API_KEY = 'b1be5db32e674696ab5b149fd41c5c4b'

    print("\nSelect Input Type:")
    print("1. IPv4 (IP Address)")
    print("2. IPv6")

    choice = input("Enter the number corresponding to your input type: ")

    if choice == "1":
        identifier_type = "IPv4"
    elif choice == "2":
        identifier_type = "IPv6"
    else:
        print("Invalid choice. Defaulting to IPv4.")
        identifier_type = "IPv4"

    identifier = input(f"Enter {identifier_type}: ")

    location_data = fetch_location(API_KEY, identifier)
    display_location_data(location_data)

if __name__ == "__main__":
    main()