import re

def strip_tags(html: str) -> str:

    pattern = r"<\/?[^>]+>"
    return re.sub(pattern, "", html)

## Tests

assert strip_tags('<a href="#">Click here</a>') == "Click here"
assert strip_tags('<p class="center">Hello <b>World</b>!</p>') == "Hello World!"
assert strip_tags('<img src="cat.jpg" alt="Cat">') == ""
assert strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') == "sectionsection"