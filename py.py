import os

for dirpath, dirnames, filenames in os.walk("."):
    with open(os.path.join(dirpath, "index.html"), "w") as index_file:
        for filename in filenames:
            if filename != "index.html":  # Exclude the index file from the listing
                index_file.write(f'<a href="{filename}">{filename}</a><br>\n')
