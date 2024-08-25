# AirAlert

<p align="center"><img src="https://i.imgur.com/bCyYrTt.png" height="250px" alt="AlertNotify Pic"/></p>

**AirAlert** is a Windows alerting tool designed to provide real-time notifications about missile and drone incidents in Israeli-Oref. The tool fetches data from a public API and displays notifications with sound alerts.

## Features

- Real-time notifications for missile and drone incidents.
- Pop-up alerts with modern design.
- Sound notifications for immediate attention.
- Customizable alert image and sound.

## Requirements

- Python 3.x
- `requests` library
- `winsound` library (for sound notifications)
- `tkinter` library (for GUI)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/airalert.git
    cd airalert
    ```

2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script:
    ```bash
    python airalert.py
    ```

2. The tool will start monitoring for new incidents. When an incident is detected, a pop-up notification will appear with the details.

Update these variables in the `airalert.py` script as needed.

