from pathlib import Path
from html import escape

ROOT = Path("files")

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Index of {path}</title>
<style>
body {{
    font-family: sans-serif;
    max-width: 1000px;
    margin: auto;
    padding: 2rem;
}}
table {{
    width: 100%;
    border-collapse: collapse;
}}
td {{
    padding: 0.4rem;
    border-bottom: 1px solid #ddd;
}}
a {{
    text-decoration: none;
}}
</style>
</head>
<body>

<h1>Index of /{path}</h1>

<table>
{rows}
</table>

</body>
</html>
"""

for directory in ROOT.rglob("*"):
    if not directory.is_dir():
        continue

    rows = []

    rel = directory.relative_to(ROOT)

    if rel != Path("."):
        rows.append(
            '<tr><td><a href="../index.html">../</a></td></tr>'
        )

    for item in sorted(directory.iterdir()):
        name = item.name

        href = (
            f"{name}/index.html"
            if item.is_dir()
            else name
        )

        display = name + "/" if item.is_dir() else name

        rows.append(
            f'<tr><td><a href="{escape(href)}">{escape(display)}</a></td></tr>'
        )

    html = TEMPLATE.format(
        path=escape(str(rel)),
        rows="\n".join(rows)
    )

    (directory / "index.html").write_text(html)
