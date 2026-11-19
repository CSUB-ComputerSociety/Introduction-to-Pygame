# Introduction-to-Pygame

The CSUB Computer Society is hosting an introduction to pygame workshop, where students will be learning how to use pygame modules to build
three small mini games and a challenge.

## Installation of Python 
For a windows computer, follow these steps to install python to your local machine.
1. Head to the official Python Installer website https://www.python.org/downloads/windows/
2. Open the downloaded file
3. Follow the prompts for python
4. Open CommandPrompt
5. Install python by typing in py install 3
6. Verify that python is installed by python --version and python -m pip --version

## Installing pygame to local machine 
Once python has been installed, it is time to install Pygame
1. Run python -m pip install -U pygame
2. Once downloaded check it is installed by python -m pygame.examples.aliens

## Python virtual environment
If pip command is not working, create a virtual python environment in command prompt
1. python -m venv .venv
2. once created, access it by source venv/bin/activate
3. To deactivate, simply type deactivate and enter

## Scripts Folder
The main scripts that will be followed and talked about are in this folder. The scripts were used from https://coddy.tech/docs/pygame/pygame-examples . After reviewing and understanding how the modules work, then the students will be given time to add a new feature, or add a visual aspect to the program. 
1. Catch_the_coins.py
2. snake.py
3. pong.py

## Challenge
Once all of the scripts have been made and understood, the challenge that students should attempt is to create a designated home menu, that includes three clickable buttons that have the name of the game. Once the button is clicked, the screen should go into that new game. Once the player dies, they can either continue playing or go back to the home menu to play a different game.

