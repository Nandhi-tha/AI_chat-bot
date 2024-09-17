import os
import sys
import SQL_Command
import recipe_generator
import Info_extract
import interview_QA
import product_ad
import essay_outline
import code_generation
import summarizer
import resume_maker
import AI

def title_bar():
    os.system('cls')  # Clear screen
            #title bar
    print("\n\t********************************************")
    print("\t*                                          *")
    print("\t*      🤖💬 AI Chat Bot Interface 🚀🧠     *")
    print("\t*                                          *")
    print("\t********************************************\n")


def Menu():
    while True:
        title_bar()
        print("WELCOME MENU")
        print("[1] Generate SQL command ")
        print("[2] Generate essay outline ")
        print("[3] Recipe Generator")
        print("[4] Extract information from paragraph")
        print("[5] Product Advertisement")
        print("[6] Interview Question and Answers")
        print("[7] Python code generator")
        print("[8] Meeting summarizer")
        print("[9] Resume Maker")
        print("[10] Other Queries")
        print("[11] Quit")

        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                SQL()
            elif choice == 2:
                essay()
            elif choice == 3:
                recipe()
            elif choice == 4:
                information()
            elif choice == 5:
                ad()
            elif choice == 6:
                interview()
            elif choice == 7:
                code()
            elif choice == 8:
                summary()
            elif choice == 9:
                resume()
            elif choice == 10:
                AI_bot()
            elif choice == 11:
                print("Thank You")
                sys.exit()
            else:
                print("Invalid Choice. Enter 1-11")
                input("Press Enter key to try again...")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 11.")
            input("Press Enter key to try again...")

def SQL():
    SQL_Command.sql_command_generation()
    input("Press Enter key to return to menu")

def essay():
    essay_outline.essay_writer()
    input("Press Enter key to return to menu")

def recipe():
    recipe_generator.generate_recipe()
    input("Press Enter key to return to menu")

def information():
    Info_extract.extract_info()
    input("Press Enter key to return to menu")

def ad():
    product_ad.advertisement()
    input("Press Enter key to return to menu")

def interview():
    interview_QA.QA_interview()
    input("Press Enter key to return to menu")

def code():
    code_generation.python_code()
    input("Press Enter key to return to menu")

def summary():
    summarizer.meeting_summary()
    input("Press Enter key to return to menu")

def resume():
    resume_maker.resume_generator()
    input("Press Enter key to return to menu")

def AI_bot():
    AI.chat_bot()
    input("Press Enter key to return to menu")

Menu()
