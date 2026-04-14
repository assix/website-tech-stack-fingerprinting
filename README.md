# Website Tech Stack Fingerprinting

A powerful command-line tool for technographic analysis and web fingerprinting. Automatically extracts web server details, hosting providers, geographic location, security headers, and the underlying technology stack (frameworks, analytics, CMS) of any target website.

## Features

* **Hosting & Network Information:** Resolves IP addresses, cloud providers, ISPs, and geographic location.
* **Security & Server Headers:** Detects web servers (Nginx, Apache, etc.) and evaluates essential security headers (HSTS, CSP, XSS Protection).
* **Deep Stack Fingerprinting:** Powered by Wappalyzer, it identifies programming languages, frontend/backend frameworks, analytics engines, and JavaScript libraries.
* **Flexible Execution:** Supports interactive mode, single-URL scanning, and batch scanning of multiple URLs simultaneously.

## Prerequisites

* Python 3.7+
* Linux, macOS, or Windows

## Installation

Clone the repository and install the required dependencies using a virtual environment:

~~~~bash
git clone https://github.com/assix/website-tech-stack-fingerprinting.git
cd website-tech-stack-fingerprinting

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
~~~~

## Usage

The script can be run in three different modes.

**1. Interactive Mode**
Run the script without arguments and it will prompt you for a URL.
~~~~bash
python scanner.py
~~~~

**2. Single Target**
Pass a single domain or URL directly in the terminal.
~~~~bash
python scanner.py example.com
~~~~

**3. Batch Scanning**
Pass multiple URLs separated by spaces.
~~~~bash
python scanner.py example.com github.com python.org
~~~~

## Example Output

~~~~text
--- Analyzing https://example.com ---

[*] HOSTING & NETWORK
  IP Address: 93.184.216.34
  Country: United States
  ISP/Cloud Provider: EdgeCast Networks / EdgeCast Networks

[*] SECURITY & SERVER HEADERS
  Web Server (Header): ECS (sec/974D)
  X-Powered-By: Hidden/Not specified
  X-XSS-Protection: Missing
  X-Frame-Options (Clickjacking): Missing
  Content-Security-Policy (CSP): Missing
  Strict-Transport-Security (HSTS): Missing

[*] TECHNOLOGY STACK
  Web servers:
    - Nginx
  Programming languages:
    - PHP (v8.1)
  JavaScript libraries:
    - jQuery (v3.6.0)
~~~~

## Disclaimer

This tool is designed for educational purposes, security research, and system administration. Always ensure you have permission to scan and analyze target web properties.

## License
MIT License
