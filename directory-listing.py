import os

# Function to generate an HTML listing for a directory
def generate_html_listing(directory):
    html = "<html><head><title>Directory Listing</title></head><body>"
    html += "<h1>Directory Listing for {}</h1>".format(directory)
    html += "<ul>"
    
    # List directories
    for dir_name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, dir_name)):
            html += '<li><strong>{}</strong></li>'.format(dir_name)

    # List files
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            html += '<li><a href="{}" target="_blank">{}</a></li>'.format(
                file_name, file_name)

    html += "</ul></body></html>"
    return html

# Specify the directory you want to list
directory_path = '/path/to/your/directory'

# Generate the HTML listing
html_listing = generate_html_listing(directory_path)

# Specify the output path
output_path = ''

# Write the HTML content to a file
output_file = 'directory_listing.html'
with open(output_file, 'w') as f:
    f.write(html_listing)