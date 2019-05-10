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

DEPENDENCY INSTALLATION AND SET UP
  1) clone repo if not done already: 'git clone' + the link to this repo 
  2) cd into the repo (e.g. `cd PoemPuzzles`)
  3) run `./setup_backend.sh`, If there are errors, then you may have missed a dependency. Try and follow the errors to figure it out (see common error below) 
  common errors: `valgrind: command not found`, so `sudo apt-get install valgrind` and run `./setup_backend.sh` again
  
  4) the back end set up should now be complete, running `python poem-api.py` in the api directory should successfully get the backend served. 

`./run_backend.sh` to run the backend!

how to use the frontend
  1) `./setup_frontend.sh`
  
`./run_frontend.sh` to run the backend!

if you get a bunch of errors (like Error: Cannot find module '@csstools/normalize.css') try running `npm install` and then the run_frontend.sh script again

  To run frontend, run `npm start` from the frontend directory (`puzzle-frontend`) 

SOME ERRORS YOU MIGHT SEE:
- if you're getting an error that your port is already in use that you're trying to run the back end on:
  `lsof -t -i :5000`
  `kill -9 ` + PID numbers shown 
 

Notes:
- Frontend uses local addresses to call backend functions. To change the base url that the frontend calls, update the variable `api_url` at the beginning of `PoemInput.js`
  - API runs locally at http://localhost:5000, frontend runs locally at http://localhost:3000
- We have not had success running this on a Windows machine, so OS X or other Unix based OSes are preferred for this reason
