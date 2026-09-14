import sys
import os
import datetime
from dataclasses import dataclass
from pathlib import Path

def create_new_post(args: Args, root_path=Path("/home/maciej/orski-hryc.github.io/posts")) -> None:
    dirname = args.title.replace(' ', '_')
    os.mkdir(root_path / dirname)
    with open(root_path / dirname, 'w') as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>{args.title}</title>
</head>

<body>
    <header>
	<h1>{args.title}</h1>
	<aside>{args.date}</aside>
    </header>

    <nav>
       <a href="../..">home</a> |
    </nav>
    <hr>

</body>
</html>
    """)

@dataclass
class Args:
    title: str
    date: str

@dataclass
class PostMetadata:
    path: Path
    title: str
    date: datetime.date

def update_metadata(metadata: PostMetadata,
                    path=Path("/home/maciej/orski-hryc.github.io/metadata.json")) -> None:
    with open(path, 'rw') as f:
        metadata = json.load(f)
        metadata["posts"].append({"path": metadata.path,
                                  "title": metadata.title,
                                  "date": metadata.date})
        f.write(json.dumps(metadata))

if __name__ == "__main__":
    post_metadata = PostMetadata(
            date=datetime.date.today())

    args = Args(title=sys.argv[1],
                date=date)
