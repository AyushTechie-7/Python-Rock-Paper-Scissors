import os

# Absolute path to the image folder
img_folder = r"C:\Users\Ayush Choudhar\OneDrive\Desktop\PYTHON PROJECT\Rock-Paper-Scissors-Game\RockPaperScissorsImages"

# List of images to check
img_files = ["Male.jpg", "Female.jpg", "computer.png"]

# Check each image
for img in img_files:
    img_path = os.path.join(img_folder, img)  # Combine folder path with image file
    if os.path.exists(img_path):
        print(f"✅ Found: {img_path}")
    else:
        print(f"❌ Not Found: {img_path}")
