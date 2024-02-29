# Port Scanner

This is a simple Python port scanner application that allows users to scan TCP ports on a specified host and retrieve geolocation information for it´s IP address.

## Features

- Scan ports on a specified host (including localhost) or IP address
- Match with big list of well known ports
- Retrieve geolocation information for identified IP addresses
- Multi-process scanning for improved performance
- User-friendly interface

## Requirements

- Python 3.x
- `geoip2` library for geolocation
- `colorama` library for colored text

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/port-scanner.git
    ```

2. Navigate to the project directory:

    ```
    cd port-scanner
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the port scanner script:

    ```
    python main.py
    ```

2. Follow the prompts to specify the host or IP address to scan, as well as the port range

3. View the results, including open ports and the corresponding geolocation information of the host

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request
