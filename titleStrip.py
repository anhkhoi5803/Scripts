import os
import re

flag = True
while flag:

    # Ask user for the folder path
    folder_path = input("Enter the full path to the folder containing your files: ").strip()

    # Regex pattern to capture series name and volume number
    pattern = re.compile(r'^(.*? v\d{2})\b')

    # Process each file in the directory
    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            base_name = match.group(1)
            ext = os.path.splitext(filename)[1]
            new_filename = base_name + ext
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_filename)
            os.rename(src, dst)
            print(f'Renamed: {filename} → {new_filename}')
        else:
            print(f'Skipped: {filename} (no match)')

    # Ask user if they want to process another folder
    another = input("Do you want to process another folder? (y/n): ").strip().lower()
    if another != 'y':
        flag = False
        print("Exiting the program.")
    else:
        print("Processing another folder...")
