import webbrowser
import os

# Based on https://xopixel.com/animated-image-grid-layout-html-css/
# Licensed under GNU GPL v3 https://www.gnu.org/licenses/gpl-3.0.en.html

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Animated Image Grid HTML CSS Grid | XO PIXEL</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/solid.css" integrity="sha384-r/k8YTFqmlOaqRkZuSiE9trsrDXkh07mRaoGBMoDcmA58OHILZPsk29i2BsFng1B" crossorigin="anonymous">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/fontawesome.css" integrity="sha384-4aon80D8rXCGx9ayDt85LbyUHeMWd3UiBaWliBlJ53yzm9hqN21A+o1pqoyK04h+" crossorigin="anonymous">
    <link href="css/normalize.css" rel="stylesheet" type="text/css">
    <link href="css/xopixel.css" rel="stylesheet" type="text/css">
    <link href="css/demo.css" rel="stylesheet" type="text/css">
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
<header class="xopixel-header">
    <div class="title"><h1>Art Gallery :: Project Yellow</h1></div>
</header>



<section class="xop-section">
    <div class="xop-wrapper">
        <div class="xop-container">
            {tiles}
        </div>
    </div>
</section>
</body>
</html>
'''

image_tile_content = '''
<a class="project" href="#">
    <figure>
        <img src="{image_url}" alt="{image_title}" title="{image_title}">
        <figcaption>
            <div>
                <h3>{image_title}</h3>
                <p class="cta">{image_artist}</p>
            </div>
        </figcaption>
    </figure>
</a>
'''


def create_image_tiles_content(images):
    content = ''
    for image in images:
        content += image_tile_content.format(
            image_title=image.title,
            image_artist=image.artist,
            image_url=image.url,
        )
    return content


def open_gallery_page(images):
    # Create or overwrite the output file
    output_file = open('web/index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        tiles=create_image_tiles_content(images))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
