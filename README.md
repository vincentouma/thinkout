# THINKOUT

## Description
This is a web application that allows users to sign up, log in ad post pitches which other users can ccomment on, upvote or downvote. They can choose which category to write a pitch in and can view and comment on other users' pitches.

### Author
Vincent Ouma

## Prerequisites
1. python3.6
2. pip
3. Virtual environment(virtualenv)

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In your terminal:

    $ git clone https://github.com/amwaniki/pitches.git
    $ cd pitches
    
Creating the virtual environment

    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
    $ curl https://bootstrap.pypa.io/get-pip.py | python
    
Installing Flask and other Modules

    $ python3.6 -m pip install Flask
    $ python3.6 -m pip install Flask-Bootstrap
    $ python3.6 -m pip install Flask-Script
    
Run the application:

    $ chmod a+x start.sh
    $ ./start.sh
    
Testing the Application
To run the tests for the class files:

    $ python3.6 manage.py test
    
## Technologies Used
1. Python 3.6
2. Flask

## BDD
|Behaviour	             | Input	                         | Output                                                |
|------------------------|---------------------------------|-------------------------------------------------------|
|View Categories	       | Click on category               | A list of pitches in that category is displayed       |
|Add a new pitch         | click on pitch                  | Authentification page is displayed and user can pitch |
|Add a comment           | Click on comment                | Comment form is displayed and user can comment        |
|Upvote pitch            | Click on upvote                 | Pitch gets +1 upvote                                  |
|Downvote pitch          | Click on downvote               | Pitche gets +1 downvote                               |

## Contact Information

Email:vinceoumah@gmail.com


## License
MIT License Copyright (c) {2019} VINCENT OUMA

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
