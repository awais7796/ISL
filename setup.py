import os
import numpy as np
import cv2

def create_directories():
    # Base directory structure
    base_dir = "D:/test_data_2.0"
    subdirs = ["Gray_imgs", "Gray_imgs_with_drawing", "Binary_imgs"]
    
    # Create main directories
    for subdir in subdirs:
        path = f"{base_dir}/{subdir}"
        if not os.path.exists(path):
            os.makedirs(path)
        
        # Create A-Z subdirectories
        for letter in range(65, 91):  # ASCII values for A-Z
            letter_dir = f"{path}/{chr(letter)}"
            if not os.path.exists(letter_dir):
                os.makedirs(letter_dir)

def create_white_image():
    # Create white background image
    white = np.ones((400,400), np.uint8) * 255
    cv2.imwrite("white.jpg", white)

def main():
    # Create required directories
    create_directories()
    
    # Create white background image
    create_white_image()
    
    print("Setup completed successfully!")
    
    # Run the application
    choice = input("Enter 1 for data collection or 2 for sign language recognition: ")
    
    if choice == "1":
        print("Starting data collection...")
        os.system("python data_collection_binary.py")
    elif choice == "2":
        print("Starting sign language recognition...")
        os.system("python final_pred.py")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 