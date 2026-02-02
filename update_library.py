name: Update Jade Library
on:
  push:
    branches:
      - uploads  
      - main     
permissions:
  contents: write
jobs:
  organize:
    runs-on: ubuntu-latest
    steps:
      - name: 📥 Checkout Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Get all history
      - name: 🐍 Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: 🧠 Run The Brain
        run: python update_library.py
      - name: 💾 Save Changes
        run: |
          git config --local user.email "auto@jadelyre.com"
          git config --local user.name "Jade Library Automation"
          
          # Add the new index
          git add library.json
          
          # Commit (only if changed)
          git diff --quiet && git diff --staged --quiet || git commit -m "Auto-index library [skip ci]"
          
          # Push to Main (The Vault)
          git push origin HEAD:main
