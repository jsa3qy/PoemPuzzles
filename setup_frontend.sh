#!/bin/sh                                                                                                                                                                                                   
sudo npm i -g npx
pip install flask
npx create-react-app puzzle-frontend
cd puzzle-frontend
rm -r src
cd ..
mv front-end/src puzzle-frontend/
npm install styled-components
cd ..