# Directory Listing Script

This Python script generates an HTML listing of files and subdirectories within a specified directory and saves it to an HTML file. It can be run as a cron job to create daily directory listings.

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
4. Open the script and replace '/path/to/your/directory' with the actual path of the directory you want to list.
5. Save the script.
6. To run the script manually:
   ```bash
   ./directory-listing.py
   ```
   This will generate an HTML file in the same directory.
7. To set up a daily cron job to run the script:
   - Open your crontab file for editing:
    ```bash
    crontab -e
    ```
   - Add the following cron job entry to run the script daily at midnight:
    ```bash
    0 0 * * * /usr/bin/python3 /path/to/your/script/directory-listing.py
    ```
   - Replace /usr/bin/python3 with the path to your Python interpreter and /path/to/your/script/directory-listing.py with the actual path to your Python script.
   - Save and exit the text editor.
8. The script will now run automatically every day at midnight and generate an HTML listing of the specified directory. Feel free to change the timing of the script to your liking.

## Requirements

Python 3

## License

This script is licensed under the MIT License.
   
        
    
