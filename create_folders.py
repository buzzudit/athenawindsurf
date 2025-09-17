import os
import re
from pathlib import Path

def slugify(text):
    # Convert to lowercase, replace spaces with hyphens, and remove special characters
    text = str(text).strip().lower()
    text = re.sub(r'[^\w\s-]', '', text)  # Remove special characters
    text = re.sub(r'[\s-]+', '-', text)     # Replace spaces and multiple hyphens with single hyphen
    text = re.sub(r'^-+|-+$', '', text)      # Remove leading/trailing hyphens
    return text

def main():
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    
    # Read the names from projects.md
    with open(script_dir / 'projects.md', 'r', encoding='utf-8') as file:
        names = [line.strip() for line in file if line.strip()]

    # Create a folder for each name
    for name in names:
        if not name:  # Skip empty lines
            continue
            
        folder_name = slugify(name)
        folder_path = script_dir / folder_name
        
        try:
            folder_path.mkdir(exist_ok=True)
            print(f"Created folder: {folder_name}")
        except Exception as e:
            print(f"Error creating folder {folder_name}: {e}")

    print("\nAll folders have been created successfully!")

if __name__ == "__main__":
    main()
