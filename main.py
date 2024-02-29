from scanner import scan_ports
from geolocation import get_geolocation
from well_known_ports import *
from colorama import Fore, Style
import socket
import os

default_host = "localhost"
default_start_port = 0
default_end_port = 33434

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear_terminal()
    print("Welcome to Port Scanner!\n")
    print("This tool allows you to scan for open ports on a host or network.")
    print("Please enter the required information below:\n")

    while True:
        try:
            host = input(f"Enter the host or IP address to scan {Style.DIM}(default: {default_host}){Style.RESET_ALL}: ").strip() or default_host
            start_port = int(input(f"Enter the start port {Style.DIM}(default: {default_start_port}){Style.RESET_ALL}: ").strip() or default_start_port)
            end_port = int(input(f"Enter the end port {Style.DIM}(default: {default_end_port}){Style.RESET_ALL}: ").strip() or default_end_port)
            country, city, latitude, longitude = get_geolocation(host)
            break
        except ValueError:
            clear_terminal()
            print(f"{Fore.RED}Invalid input! Port numbers must be integers.{Style.RESET_ALL}\n")
        except socket.gaierror:
            clear_terminal()
            print(f"{Fore.RED}Host must be valid.{Style.RESET_ALL}\n")

    clear_terminal()
    print("Scanning...")
    open_ports = scan_ports(host, start_port, end_port)
    clear_terminal()
    print_well_known_ports()
    if any([country, city, latitude, longitude]):
        print(f"\nHost '{host}' located at ({latitude},{longitude}) - {city}, {country}")
    else:
        print(f"\nHost '{host}' {Fore.RED}(unknown location){Style.RESET_ALL}")
    if open_ports:
        print(f"\nThe following ports are open:")
        for port in open_ports:
            if port in well_known_ports:
                print(f"• Port {port} is open - Known port for {well_known_ports[port]}")
            else:
                print(f"• Port {port} is open.")
    else:
        print(f"\n{Fore.RED}No open ports found on host in the specified range.{Style.RESET_ALL}")
    print("\n")


if __name__ == "__main__":
    main()
