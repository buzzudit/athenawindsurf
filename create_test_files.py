from pathlib import Path

def create_test_files():
    # Get the script's directory
    base_dir = Path(__file__).parent
    
    # Content for test.md
    content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit ipsum dolor sit amet, consectetur adipiscing elit"
    
    # Find all directories (excluding hidden ones like .git)
    folders = [f for f in base_dir.iterdir() if f.is_dir() and not f.name.startswith('.')]
    
    # Create test.md in each folder
    for folder in folders:
        test_file = folder / "test.md"
        try:
            with open(test_file, 'w') as f:
                f.write(content)
            print(f"Created test.md in {folder.name}")
        except Exception as e:
            print(f"Error creating test.md in {folder.name}: {e}")
    
    print("\nAll test files have been created successfully!")

if __name__ == "__main__":
    create_test_files()
