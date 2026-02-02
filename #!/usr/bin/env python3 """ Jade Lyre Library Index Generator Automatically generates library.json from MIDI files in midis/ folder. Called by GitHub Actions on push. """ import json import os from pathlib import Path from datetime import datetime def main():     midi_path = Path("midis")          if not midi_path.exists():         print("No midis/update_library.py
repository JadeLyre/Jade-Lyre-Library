#!/usr/bin/env python3
"""
Jade Lyre Library Index Generator
Automatically generates library.json from MIDI files in midis/ folder.
Called by GitHub Actions on push.
"""
import json
import os
from pathlib import Path
from datetime import datetime
def main():
    midi_path = Path("midis")
    
    if not midi_path.exists():
        print("No midis/ folder found, creating empty library.json")
        Path("library.json").write_text("[]")
        return
    
    # Find all MIDI files
    midi_files = list(midi_path.glob("*.mid")) + list(midi_path.glob("*.midi"))
    
    # Build library index
    library = []
    for f in sorted(midi_files):
        library.append({
            "name": f.stem,
            "filename": f.name,
            "path": str(f),
            "size": f.stat().st_size,
            "added": datetime.fromtimestamp(f.stat().st_mtime).isoformat()
        })
    
    # Write library.json
    Path("library.json").write_text(json.dumps(library, indent=2))
    print(f"✓ Updated library.json with {len(library)} songs")
    
    # Print summary
    for song in library:
        print(f"  - {song['name']}")
if __name__ == "__main__":
    main()
