#!/usr/bin/env python3
import json
import os
from pathlib import Path
from datetime import datetime
def main():
    midi_folder = Path("midis")
    output_file = Path("library.json")
    
    if not midi_folder.exists():
        midi_folder.mkdir(exist_ok=True)
    
    files = list(midi_folder.glob("*.mid")) + list(midi_folder.glob("*.midi"))
    
    library = []
    for f in sorted(files):
        stats = f.stat()
        library.append({
            "name": f.stem.replace("_", " ").title(),
            "filename": f.name,
            "path": f"midis/{f.name}",
            "size": stats.st_size,
            "added": datetime.fromtimestamp(stats.st_mtime).isoformat()
        })
    
    output_file.write_text(json.dumps(library, indent=2))
    print(f"Indexed {len(library)} songs.")
if __name__ == "__main__":
    main()
