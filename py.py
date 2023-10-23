import os

for dirpath, dirnames, filenames in os.walk("."):
    with open(os.path.join(dirpath, "index.html"), "w") as index_file:
        index_file.write('<html>\n<head><link rel="stylesheet" type="text/css" href="/style.css">\n<title>Algorithm & Programs</title>\n</head>\n<body>\n')  # Opening body tag here

        for filename in filenames:
            if filename != "index.html" and filename.endswith(".txt"):  # Exclude the index file and .txt files from the listing
                filename_without_extension, _ = os.path.splitext(filename)
                index_file.write(f'<a href="{filename}">{filename_without_extension}</a><br>\n')

        index_file.write('</body>\n</html>\n')  # Closing body tag here

# <html>
# <head>
# <link rel="stylesheet" type="text/css" href="/style.css">
# <title>Algorithm & Programs</title>
# </head><body>
# <h1>Algorithms and Program</h1>
# <a href="/c">C program</a><br>
# <a href="/j">Java</a><br>
# </body>
# </html>
