#!/usr/bin/env python3
"""
הרץ את הסקריפט הזה בתוך תיקיית nivmanor.com (ליד index.html)
הוא יסרוק את תיקיית images/ ויצור קובץ images.json

הרצה: python3 generate_images_json.py
"""

import os
import json

images_dir = "images"
output_file = "images.json"
image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

result = {}

if not os.path.exists(images_dir):
    print(f"שגיאה: תיקייה '{images_dir}' לא נמצאה")
    exit(1)

for folder in sorted(os.listdir(images_dir)):
    folder_path = os.path.join(images_dir, folder)
    if not os.path.isdir(folder_path):
        continue

    files = []
    for f in sorted(os.listdir(folder_path)):
        ext = os.path.splitext(f)[1].lower()
        if ext in image_extensions:
            files.append(f"images/{folder}/{f}")

    if files:
        result[folder] = files
        print(f"  {folder}: {len(files)} תמונות")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\nנוצר: {output_file} עם {len(result)} תיקיות")
