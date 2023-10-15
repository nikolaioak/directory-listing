import os

# Function to generate an HTML listing for a directory
def generate_html_listing(directories):
    html = "<html><head><title>Directory Listing</title></head><body>"
    html += "<h1>Directory Listing</h1>"
    html += "<ul>"

    for directory in directories:
        html += "<h2>Directory: {}</h2>".format(directory)
    
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
directories_to_list = [
    '/path/to/first/directory',
    '/path/to/second/directory'
]

# Generate the HTML listing
html_listing = generate_html_listing(directories_to_list)

# Specify the output path if desired
output_path = ''

# Write the HTML content to a file
output_file = output_path + 'directory_listing.html'
with open(output_file, 'w') as f:
    f.write(html_listing)