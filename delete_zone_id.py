#!/usr/bin/env python3
import os

# Set this to the folder you want to clean
root_folder = os.path.abspath(".")

# Walk through all folders and subfolders
for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        if "Zone.Identifier" in filename:
            file_path = os.path.join(dirpath, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

print("Cleanup complete!")