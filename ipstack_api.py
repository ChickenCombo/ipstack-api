from requests import get
import requests
import socket

# API data
BASE_URL = "http://api.ipstack.com/"
API_KEY = "?access_key=f572e15bd416e3cecedc244c63eec13b&format=1"

def main():
    while True:
        # User input
        print(f"Choose an option:")
        print(f"1 - Get device's IP address")
        print(f"2 - Manually enter IP address")
        print(f"q - Quit")
        user_input = input("Choice: ")

        # Get device's IP address
        if user_input == "1":
            ip_address = get('https://api.ipify.org').content.decode('utf8')
            apiRequest(ip_address)
        # Manually enter IP address
        elif user_input == "2":
            ip_address = input("Enter IP address: ")
            apiRequest(ip_address)
        # Quit
        elif user_input == "q":
            break
        # Invalid input
        else:
            continue

def apiRequest(user_input):
    try:
        # Check if user input is a valid IPv4/IPv6 address
        socket.inet_aton(user_input)

        # Request from the API
        api_request = BASE_URL + user_input + API_KEY
        data = requests.get(api_request).json()

        # Display output
        print(f"\nIP Address: {(data['ip'])}")
        print(f"Version: {(data['type'])}")
        print(f"Continent: {(data['continent_name'])}")
        print(f"Country: {(data['country_name'])}")
        print(f"Region: {(data['region_name'])}")
        print(f"City: {(data['city'])}")
        print(f"Zip: {(data['zip'])}\n")

    except socket.error:
        # Error message
        print("Invalid IP Address!")

if __name__=="__main__":
    main()