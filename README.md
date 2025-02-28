# Directory Listing Script

This Python script generates an HTML listing of files and subdirectories from any number of specified directories and saves it to an HTML file. It can be run as a cron job to create daily directory listings.

## Usage

1. Clone this repository or download the script to your local machine.

2. Open a terminal and navigate to the directory where the script is located:
    ```bash
    cd /path/to/your/script/directory
    ```
3. Make sure the script is executable:
   ```bash
   chmod +x directory-listing.py
   ```
4. To run the script manually:
   ```bash
   ./directory-listing.py /path/to/output/folder /path/to/directory1 /path/to/directory2 ...
   ```
   This will generate an HTML file in the output folder specified. To output the HTML in the same directory as the script, use ```'.'``` .
5. To set up a daily cron job to run the script:
   - Open your crontab file for editing:
    ```bash
    crontab -e
    ```
   - Add the following cron job entry to run the script daily at midnight:
    ```bash
    0 0 * * * /usr/bin/python3 /path/to/your/script/directory-listing.py /path/to/output/folder /path/to/directory1 /path/to/directory2 ...
    ```
   - Replace ```/usr/bin/python3``` with the path to your Python interpreter and ```/path/to/your/script/directory-listing.py``` with the actual path to your Python script, then the rest of the arguments as desired.
   - Save and exit the text editor.
6. The script will now run automatically every day at midnight and generate an HTML listing of the specified directories. Feel free to change the timing of the script to your liking.

## Requirements

Python 3

## License

This script is licensed under GPLv3.
