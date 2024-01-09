import os

for dirpath, dirnames, filenames in os.walk("."):
    with open(os.path.join(dirpath, "index.html"), "w") as index_file:
        index_file.write(
"""
<html>\n<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta property="og:title" content="Lab Programs and Algorithms"/>
<meta property="og:description" content="Java & C" />
<meta property="og:image" content="https://i.pinimg.com/564x/1c/54/f7/1c54f7b06d7723c21afc5035bf88a5ef.jpg" />
<meta property="og:url" content="https://aashishvinu.me/"/>
<link rel="stylesheet" type="text/css" href="/style.css">
<title>Algorithm & Programs</title><link rel="stylesheet" type="text/css" href="/style.css"></head></body></html>""") 
        for filename in filenames:
            if filename != "index.html" and filename.endswith(".txt"):
                filename_without_extension, _ = os.path.splitext(filename)
                index_file.write(f'<a href="{filename}">{filename_without_extension}</a>\n')

        index_file.write('</body>\n</html>\n')

<html>
<head>
<meta property="og:title" content="Lab Programs and Algorithms" />
<meta property="og:description" content="Java & C" />
<meta property="og:image" content="https://i.pinimg.com/564x/1c/54/f7/1c54f7b06d7723c21afc5035bf88a5ef.jpg" />
<meta property="og:url" content="https://aashishvinu.me/"/>
<link rel="stylesheet" type="text/css" href="/style.css">
<title>Algorithm & Programs</title>
</head><body>
<a href="/c">C program</a>
<a href="/j">Java</a>
</body>
</html>

