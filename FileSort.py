import os
import shutil
import sys
import time
import random
USER = 'user'

os.chdir(f'/home/{USER}/Downloads/')


def file_sort():
    working_dir = os.getcwd()
    files = os.listdir()
    for file in files:
        try:
            if '.part' in file:
                time.sleep(15)
            elif '.mp3' in file:
                time.sleep(15)
                shutil.move(working_dir + '/' + file, f'/home/{USER}/Music/')
            elif '.jpg' in file or '.png' in file:
                shutil.move(working_dir + '/' + file, f'/home/{USER}/Pictures/')
            elif '.mp4' in file:
                time.sleep(15)
                shutil.move(working_dir + '/' + file, f'/home/{USER}/Videos/')
            elif '.txt' in file or '.docx' in file:
                shutil.move(working_dir + '/' + file, f'/home/{USER}/Documents/')
            elif '.ovpn' in file:
                shutil.move(working_dir + '/' + file, f'/home/{USER}/VPN/')
            print(f"Sorted {file}")
        except shutil.Error:
            try:
                name = file[:file.index('.') + len('.')]
                ext = file[file.index('.') + len('.'):]
                tag = random.randint(100, 999)
                os.rename(file, name + str(tag) + ext)
            except shutil.Error:
                pass


if __name__ == '__main__':
    try:
        while True:
            file_sort()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)
