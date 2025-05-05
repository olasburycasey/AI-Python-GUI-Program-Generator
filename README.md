# AI Python GUI program generator

## Overview

A project that runs generated GUI applications and intends to run them on your own.

## Instructions

1. Run gemini_2-0_flash_run.py
2. You will get a welcome message and a set of options on what to do. The program asks you to type a number between 1 and 4.
3. If you select option 1, the program will ask you if you want the LLM to generate an image, a game, or other application of your choice. You will then be asked to provide a description.
4. If you select option 2, the program will print a list of programs already saved that you want to run and make edits to.
5. If you select option 3, you will be asked to select a saved program to give feedback and a rating.
6. If you select option 4, the program will print a goodbye message and automatically stop running.
7. For options 1 and 2, you will be asked if you want to run the program.
8. If the generated GUI program is new, you will be given the option to save the file in the saved_programs directory.
9. If the generated GUI program was saved before, the new generated code will be modified under the same python file. The new features are auto-saved.
10. For option 3, the program will scan the file of your choice and give it a rating from 1-10 with some additional feedback.
11. After each execution, the program will go back to the main menu.