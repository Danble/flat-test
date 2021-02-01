# flat-test
GitPython Fullstack Project

Requirements:
* Have git installed
* Have Python 3.6+ installed 
* Have npm 6.13.4 installed
* Have node 12.16.1 installed
* Have virtualenv installed

# Instructions:

1) Clone this repo -> `git clone https://github.com/Danble/flat-test.git`
## Backend instructions
2) Go to flat-back folder -> `cd flat-back/`
3) Create virtualenv -> `virtualenv flat-back`
4) (Windows) activate virtualenv -> `./flat-back/Scripts/activate`
   (Linux) activate virtualenv -> `source flat-back/bin/activate`
5) Install dependencies -> `pip install gitdb gitpython flask`
6) Inside flat-back/flaskr/ folder clone the repo we are going to work with -> `git clone https://github.com/Danble/fullstack-interview-test.git`. You can link other branches or create your own branches inside this repo and they will be displayed when you run the frontend.
7) Go one folder back and run backend -> `python flaskr/app.py` 

## Fronted instructions
8) From the git root go to flat-front folder -> `cd flat-front/`
9) Install dependencies -> `npm install`
10) Run frontend -> `npm run serve`
