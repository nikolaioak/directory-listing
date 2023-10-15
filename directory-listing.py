import os
import sys

# Function to generate an HTML listing for a directory
def generate_html_listing(directories):
    html = "<html><head><title>Directory Listing</title></head><body>"
    html += "<h1>Directory Listing</h1>"
    html += "<ul>"

    for directory in directories:
        html += "<h2>Directory: {}</h2>".format(directory)

        # list files and directories in top level directory (alphabetic order)
        for files_dirs in sorted(os.listdir(directory)):
            
            if os.path.isdir(os.path.join(directory,files_dirs)):
                html += '<li><strong>{}</strong><ul>'.format(files_dirs)

                # alphabetic order please
                for file_name in sorted(os.listdir(os.path.join(directory,files_dirs))):
                    if os.path.isdir(os.path.join(directory, files_dirs, file_name)):
                        html += '<li><strong>{}</strong><ul>'.format(file_name)

                        # Go another level if it's a folder
                        for subfile in sorted(os.listdir(os.path.join(directory, files_dirs, file_name))):
                            html += '<li><a href="{}" target="_blank">{}</a></li>'.format(
                            os.path.join(directory, files_dirs, file_name, subfile), subfile)

                        html += '</ul></li>'
                            
                    if os.path.isfile(os.path.join(directory, files_dirs, file_name)):
                        html += '<li><a href="{}" target="_blank">{}</a></li>'.format(
                        os.path.join(directory, files_dirs, file_name), file_name)
                
                html += '</ul></li>'

            if os.path.isfile(os.path.join(directory, files_dirs)):
                html += '<li><a href="{}" target="_blank">{}</a></li>'.format(
                os.path.join(directory, files_dirs), files_dirs)

    html += "</ul></body></html>"
    return html

# Check if directories were provided as command line arguments
if len(sys.argv) < 3:
    print("Usage: python script.py /path/to/output/folder /path/to/directory1 /path/to/directory2 ...")
    sys.exit(1)

# Get the directories from command line arguments (excluding the script name and output path)
directories_to_list = sys.argv[2:]

# Generate the HTML listing
html_listing = generate_html_listing(directories_to_list)

# Specify the output path if desired
output_path = sys.argv[1]

# Write the HTML content to a file
output_file = output_path + '/directory-listing.html'
with open(output_file, 'w') as f:
    f.write(html_listing)