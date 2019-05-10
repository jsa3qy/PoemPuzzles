#!/bin/sh 
chmod +x install.sh
./install.sh
pip install -r requirements.txt
cd api
chmod +x poem-api.py
chmod +x exact_cover_np
rm -rf exact_cover_np
git clone https://github.com/moygit/exact_cover_np.git
cd exact_cover_np
apt-get install valgrind
make
