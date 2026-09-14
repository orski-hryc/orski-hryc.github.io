from pathlib import Path
from dataclasses import dataclass
from typing import NewType
import json
import datetime

@dataclass
class TableItem:
    path: Path
    date: str

class Metadata:
    def __init__(self, path: Path):
        with open(path, 'r') as f:
            self._metadata = json.load(f)

    def date(self) -> datetime.date:
        return datetime.date.fromisoformat(self._metadata["date"])

def today() -> str:
    return datetime.datetime.now().strftime("%F")

def grab_links(path: Path) -> TableItem:
    for directory in path.iterdir():
        if (directory / "text.html").is_file():
            yield TableItem(path=directory / "text.html",
                            date=)

def format_link(path: Path) -> str:
    return f"<li>[<time datetime=\"{date}\">{date}</time>] <a href=\"{str(path)}\">{path.parent}</a></li>"

def generate_table(path: Path) -> str:
    """ Generates a html link table 
    """
    return f"""
    <nav>
        <ul>
            {"\n\t\t\t".join(map(format_link, grab_links(path)))}
        </ul>
    </nav>
    """

def generate_html(path: Path) -> str:
    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>Posts</title>
</head>

<body>
    <header>
	<h1>Posts</h1>
	<aside> last update on: {today()} </aside>
    </header>
    <hr>

    {generate_table(path)}

</body>
</html>
"""

if __name__ == "__main__":
    path = Path('.')
    
    with open("index.html", 'w') as file:
        file.write(generate_html(path))
