#!/bin/bash

sudo apt install python3-tk
sudo pip install --upgrade youtube_dl
sudo apt install ffmpeg
pip install yt-dlp
pip install customtkinter
pip install Pillow
pip install pydub
pip install colorama
pip install beautifulsoup4
pip install requests
pip install appdirs
pip install tqdm

current_directory=$(pwd)

mkdir -p ~/bin/

if ! grep -q "export PATH=\$HOME/bin:\$PATH" ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

source ~/.bashrc

if [ -d images ]; then
    mv images ~/bin/
else
    echo "Folder 'images' does not exist in current DIR."
fi

if [ -f CeNtis.py ]; then
    mv CeNtis.py ~/bin/
else
    echo "File CeNtis.py does not exist in current DIR."
fi

chmod +x ~/bin/CeNtis.py

echo "Setup completed successfully."

sudo rm -r "$current_directory"

unset current_directory
