from scanner import scan_ports
from well_known_ports import print_well_known_ports
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
    print("Welcome to Port Scanner!")
    print("This tool allows you to scan for open ports on a host or network.")
    print("Please enter the required information below:\n")

    while True:
        try:
            host = input(f"Enter the host or IP address to scan (default: {default_host}): ").strip() or default_host
            start_port = int(input(f"Enter the start port (default: {default_start_port}): ").strip() or default_start_port)
            end_port = int(input(f"Enter the end port (default: {default_end_port}): ").strip() or default_end_port)
            break
        except ValueError:
            clear_terminal()
            print("Invalid input! Port numbers must be integers.")

    clear_terminal()
    print("Scanning...")
    open_ports = scan_ports(host, start_port, end_port)
    clear_terminal()
    print_well_known_ports()
    if open_ports:
        print(f"\n\nThe following ports are open on {host}:\n")
        for port in open_ports:
            print(f"Port {port} is open.")
    else:
        print(f"\nNo open ports found on {host} in the specified range.")
    print("\n")


if __name__ == "__main__":
    main()
