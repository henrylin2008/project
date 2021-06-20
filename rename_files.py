# Rename files in a directory into ordered number + .webp (extension) (ex: 1.webp, 2.webp, etc..)
import os

def main():
    base_dir = "Local_dir"
    for count, file in enumerate(os.listdir(base_dir)):  # rename file starts with 1.webp
        dst = base_dir + str(count+1) + ".webp"
        os.rename(base_dir + file, dst)
    print("Files rename successfully!")


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
