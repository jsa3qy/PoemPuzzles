# PoemPuzzles
Repo for code related to puzzle poetry research

Git flow:
master has everything
if you want to add something to master, let's make a branch called trunk (git branch trunk)
off of trunk make a branch called doit (where you will do the think you want to do)
build on doit and PR against trunk. Then once you merge with trunk make sure that it works and then PR against master

---------------------

the important thing is that we are using python 2.7.x from the beginning and for everything.

0) clone PoemPuzzles, and then 'rm -r exact_cover_np' if it's already in there and then git clone the exact_cover_np repo --> cd into this exact cover repo
github clone-able links:
https://github.com/jsa3qy/PoemPuzzles.git
https://github.com/moygit/exact_cover_np.git

1) run make and probably get the valgrind error
2) if homebrew is not installed, install it and then run 'brew install valgrind'
3) you'll probably get an error about pandas so run 'python -m pip install --user pandas==0.22.0'
it has to be 0.22.0 to work. If you get a dateutil error it's because pandas version is too new.
4) you'll probably run into a numpy version error on the next make, which is solved with:
sudo pip install --upgrade --ignore-installed --install-option '--install-data=/usr/local' numpy



At this point "make" should successfully work in the exact_cover_repo, running all the tests in a few seconds.



5) cd back into PoemPuzzles and run pip install -r requirements.txt

6) python main.py



Let me know if something is not working!
