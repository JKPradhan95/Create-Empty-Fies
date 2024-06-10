from pathlib import Path

root_dir = Path('files')

for i in range(5, 10):
  filename = str(i) + '.html'
  filepath = root_dir / Path(filename)
  filepath.touch()