import os
from PIL import Image

# Set this to your dataset root folder
DATASET_DIR = 'Medicinal Leaf dataset'

corrupt_count = 0
fixed_count = 0

def fix_jpeg(path):
    global corrupt_count, fixed_count
    try:
        with Image.open(path) as img:
            img.verify()  # Check for corruption
        # Try to re-open and save if possible
        with Image.open(path) as img:
            img.save(path, 'JPEG')
            fixed_count += 1
    except Exception as e:
        corrupt_count += 1
        print(f'Corrupt: {path} ({e})')

for root, dirs, files in os.walk(DATASET_DIR):
    for file in files:
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
            fix_jpeg(os.path.join(root, file))

print(f'Checked all images. Corrupt: {corrupt_count}, Fixed: {fixed_count}')
