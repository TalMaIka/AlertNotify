# AlertNotify

<p align="center"><img src="https://i.imgur.com/bCyYrTt.png" height="250px" alt="AlertNotify Pic"/></p>

**AlertNotify** is a Windows alerting tool designed to provide real-time notifications about missile and drone incidents in Israeli-Oref. The tool fetches data from a public API and displays notifications with sound alerts.

## Features

- Real-time notifications for missile and drone incidents.
- Sound notifications for attention.

## Requirements

- Python 3.x
- `requests` library
- `winsound` library (for sound notifications)
- `tkinter` library (for GUI)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/TalMaIka/AlertNotify.git
    cd AlertNotify
    ```

2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script:
    ```bash
    python AlertNotify.py
    ```

2. The tool will start monitoring for new incidents. When an incident is detected, a pop-up notification will appear with the details.

