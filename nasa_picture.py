import requests
import platform     # retrieve system information
import pwd          # access to Unix user account and password database
import os

"""
    Retrieve Nasa image of the day, and download it to current user's Downloads directory, 
    Set saved Nasa image as the desktop background 
"""

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
file_name = 'nasa_picture.png'


def get_filename():
    username = pwd.getpwuid(os.getuid()).pw_name    # get current username, (only works in Unix)
    if platform.system() == "Linux":
        directory = "/home/" + username + "/Downloads/"     # user's Download directory
    elif platform.system() == "Darwin":
        directory = "/Users/" + username + "/Downloads/"

    return os.path.join(directory, file_name)


def download_picture():
    request = requests.get(url)

    if request.status_code != 200:
        print("Not able to retrieve the picture")
        return

    picture_url = request.json()['url']
    if "jpg" not in picture_url:
        print("No image today")
    else:
        picture = requests.get(picture_url, allow_redirects=True)
        filename = get_filename()

        open(filename, 'wb').write(picture.content)

        print(f"Saved picture of the day to {filename}!")


if __name__ == '__main__':
    download_picture()

    filename = get_filename()

    # set background
    if platform.system()=="Linux":
        cmd = "gsettings set org.gnome.desktop.background picture-uri file:" + filename
    elif platform.system()=="Darwin":
        cmd = "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"" + filename +"\"'"
        # use absolute path to the image, and not a path that begins with a user path (~/Downloads/image.jpg)!

    os.system(cmd)
