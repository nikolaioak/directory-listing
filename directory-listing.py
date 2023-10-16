import os
import sys
        
# Generator function to yield directory paths and files iteratively
def generate_directory_contents(directory):
    for root, dirs, files in os.walk(directory):
        # Alphabetize
        dirs.sort()
        files.sort()

        yield (os.path.relpath(root, start=directory), dirs, files)

# Function to generate an HTML listing for multiple directories
def generate_html_listing(directories):
    html = "<html><head><title>Directory Listing</title></head><body>"
    html += "<h1>Directory Listing</h1>"
    
    for directory in directories:
        previous_nest = 0
        current_nest = 0
        folderName = directory.split('/')[len(directory.split('/'))-1]
        html += "<h2>Directory: {}</h2><ul>".format(folderName)
        
        # List subdirectories and files iteratively
        for path, dirs, files in generate_directory_contents(directory):

            if current_nest != 0:
                previous_nest = len(paths)

            paths = path.split('/')
            current_nest = len(paths)

            if current_nest < previous_nest:
                html += '</ul></li>'*(previous_nest - current_nest)

            if path != '.':
                # Remove slashes to have a nested listing
                if '/' in path:
                    html += '<li><strong>{}</strong><ul>'.format(paths[len(paths)-1])
                else:
                    html += '<li><strong>{}</strong><ul>'.format(path)

            # set file_count for the existence of files in directory
            file_count = 0
            for file_name in files:
                file_count = 1
                html += '<li><a href="{}" target="_blank">{}</a></li>'.format(
                os.path.join(directory, path, file_name), file_name)
            
            if file_count:
                file_count = 0
                if len(dirs) == 0:
                    html += '</ul></li>'              

            #html += '</ul>'
        
        html += '</ul></ul>'

    html += "</body></html>"
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