# PoemPuzzles
Repo for code related to puzzle poetry research

Hi all!

In the master branch are two primary folders: api and front-end
the "run.sh" script is used to get the whole system running in one shot.

api: includes the back-end code for this Sonnet Tiling App!
front-end: includes all front end infrastructure for the app

OVERVIEW
how to get started running this locally:
1) clone repo 
2) install dependencies 
4) ./run.sh

1) clone repo: 'git clone' + the link to this repo 

DEPENDENCY INSTALLATION AND SET UP
2) cd into the repo (e.g. `cd PoemPuzzles`)
3) run `./install.sh`
4) hit Y whenever asked 
5) once the install script completes run the following commands: `cd api`, `chmod -x poem-api.py`, `rm -r exact_cover_np`
6) `git clone https://github.com/moygit/exact_cover_np.git`
7) `cd exact_cover_np`
8) sudo apt-get install valgrind
9) run `make`, if there are no errors, you are good to go. If there are errors, then you may have missed a dependency. Try and follow the errors to figure it out. 
10) `cd ..` (make sure you’re in the api directory)
11) `pip install -r requirements.txt`
12) the back end set up should now be complete, running `python poem-api.py` should successfully get the backend served. 


how to use the frontend
  1) in the PoemPuzzles directory, `pip install flask`
  2) to create a new frontend directory, run `npx create-react-app puzzle-frontend` (run `npm install npx` if npx is not recognized)
  3) delete `src/` folder of new project and replace with `src/` folder from repo: 
        `cd front-end`
        `rm -r src`
        `cd ..`
        `mv /front-end/src /puzzle-frontend`
      
  4) cd into `puzzle-frontend` and run `npm install styled-components`
  5) make sure that in the script run.sh, that if "front-end" is replaced with "puzzle-frontend" if it is not already

  To run frontend, run `npm start` from the frontend directory

Notes:
- Frontend uses local addresses to call backend functions. To change the base url that the frontend calls, update the variable `api_url` at the beginning of `PoemInput.js`
  - API runs locally at http://localhost:5000, frontend runs locally at http://localhost:3000
- We have not had success running this on a Windows machine, so OS X or other Unix based OSes are preferred for this reason
