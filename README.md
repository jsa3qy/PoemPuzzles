# PoemPuzzles
Repo for code related to puzzle poetry research

Hi all!

In the master branch are two primary folders: api and front-end
the "run.sh" script is used to get the whole system running in one shot.

api: includes the back-end code for this Sonnet Tiling App!
front-end: includes all front end infrastructure for the app

how to get started running this locally:
1) clone repo 
2) install dependencies 
    - `pip install flask`
3) run `chmod -x manage.py` from `api` directory
4) ./run.sh

how to use the frontend
  1) to create a new frontend directory, run `npx create-react-app puzzle-frontend`
  2) delete `src/` folder of new project and replace with `src/` folder from repo
  3) run `npm install styled-components`

  To run frontend, run `npm start` from the frontend directory

Notes:
- Frontend uses local addresses to call backend functions. To change the base url that the frontend calls, update the variable `api_url` at the beginning of `PoemInput.js`
  - API runs locally at http://localhost:5000, frontend runs locally at http://localhost:3000
- We have not had success running this on a Windows machine, so OS X or other Unix based OSes are preferred for this reason
