#!/bin/bash

# 1. Install Python Dependencies
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

# 2. Create 'bin' Directory if it doesn't exist
mkdir -p ~/bin/

# 3. Add 'export PATH' to .bashrc if not already present
if ! grep -q "export PATH=\$HOME/bin:\$PATH" ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
fi

# 4. Source .bashrc to apply changes immediately
source ~/.bashrc

if [ -d images ]; then
    mv images ~/bin/
else
    echo "Der Ordner 'images' existiert nicht im aktuellen Verzeichnis."
fi

if [ -d CeNtis.py ]; then
    mv CeNtis.py ~/bin/
else
    echo "Die Datei CeNtis.py existiert nicht im aktuellen Verzeichnis."
fi

# 5. Navigate to the Home Directory
#cd ~/bin/

# 6. Git Clone Repository
#git clone https://github.com/prowiz77/CeNtis.git

# 7. Copy CeNtis.py to 'bin' Directory
#cp ~/bin/CeNtis/CeNtis.py ~/bin/
#cp -r ~/bin/CeNtis/images/ ~/bin/

# 8. Make CeNtis.py Executable
chmod +x ~/bin/CeNtis.py

echo "Setup completed successfully."

sudo rm -r "$current_directory"

unset current_directory
