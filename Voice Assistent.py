import pyttsx3
''''
 1)It is pre built in module in python.
 2)"pyttsx3" stands for "python text to speech version_3".
 3)It is used to convert text to speech.
'''
import datetime     # This Module is Used to Find Current Date,Time,Hours,Minutes and Seconds.
import speech_recognition as sr
# This Module is Used to Recognise our speech or audio.
# "as" is Keyword in python used to refer short name.
import wikipedia     # this module is used for user questions search in wikipedia
import webbrowser    # this module is used for open webbrowser 
import os
# this module with methods for interacting with the operating system, like creating files and directories,management of files and directories,input, output, etc..

sounds=pyttsx3.init("sapi5")
# sapi5 stands for speech API5 and this Teachnology provided by Microsoft.
# sounds is Variable.
# pyttsx3.init("sapi5") class support many and diffrent "sounds" eg:humans sounds and animal sounds etc....
# "sapi5" for windows
# sapi5   =  windows
# nsss    =  mac os
# espeak  =  evey other platform

gender_voice=sounds.getProperty("voices")
# getproperty is used for get voices frome "sapi5".
# "voices" contain two voices "0 index is male" and "1 index is female".
sounds.setProperty("voice",gender_voice[1].id)
# setproperty is used for set one voice to sounds.
# "voice" means singular it set only one voice.
# "gender_voice[1].id" you set 1st index voice and id attribute is always defined it is default.

def speak(audio):
    sounds.say(audio)     # say function is used to Read the Text in setted voice.
    sounds.runAndWait()   # It is used to don't finish the code and it is waiting for another command.

def wishme():
    hour=int(datetime.datetime.now().hour)
    # datetime module - datetime class - now() funtion - hour nested funtion.
    # It is used to find the current hour.
    if hour>=0 and hour<12:
        print("Good morning Boss 🥱")
        speak("Good morning Boss")
        print()
    elif hour>=12 and hour<16:
        print("Good Afternoon Boss 🥰")
        speak("Good Afternoon Boss")
        print()
    elif hour>=16 and hour<21:
        print("Good Evening Boss 😘")
        speak("Good Evening Boss")
        print()
    else:
        print("Good Night Boss 😴")
        speak("Good Night Boss")
        print()

def takecommand():
    with sr.Microphone() as source:
    # "with" Keyword is to automrtically close your file when the code is executed.
        print("I am Listening  Your Voice........")
        sr.Recognizer().pause_threshold=1   # seconds of non-speakingaudio after a word is considering complete.
        sr.Recognizer().adjust_for_ambient_noise(source,duration=1)  # It is used to remove unwanted noise in your audio with 1_Seconds.
        audio=sr.Recognizer().listen(source)
        # listen method is used for listen audio via sr.Microphone().
        # Microphone() is used for accept sound.
    try:
        print("Wait a Few Minitues Guys")
        query=sr.Recognizer().recognize_google(audio,language="en-in") 
        # It use internet because this "recognize_google" funtion  is only available in internet.
        # "en-in" means "english india".
        # It is used to change your audio in english india.
        print("User Said :",query)
        print() # It is used for empty line.
    except Exception as e:
    # if any error in your query it handle the error autometically.
        print(e)
        # it is used to print what  error occured.
        query="Say that Again Please"
        print(query)
        speak(query)
    return query
    # The return keyword is used to return your query in function calling.

if __name__ == "__main__":
    # it is used to check this file is main file or imported file.
    # the "if" condition is only true if the file is main otherwise it will "false" the condition.
    wishme()  #It calling the wishme() function.
    print("I am your Voice Assistent, My Name is Alpha")
    # your Perssonal Assistent Name is "Alpha"
    speak("I am your Personal Assistent, My Name is Alpha")
    while True:  # "while True" is infinitly run the loop when the condition is false.
        print("Say 'HELLO Alpha' to Use   Me")
        speak("Say 'HELLO Alpha' to Use   Me")
        print("Say 'CLOSE Alpha' to Close Me")
        speak("Say 'CLOSE Alpha' to Close Me")
        print()
        commands_1=takecommand().lower()
        # it calling the "takecommand()" function and that function return "query" value.
        # "lower()" function is used to convert your returned "query" value in lower case.

        if "hello alpha" in commands_1:
            print("I am ready to Work Boss")
            speak("I am ready to Work Boss")
            print("Please Tell what Can i do")
            speak("Please Tell what Can i do")
            print()
            print("You Search  Wikipedia Please Tell 'Your Command + Wikipedia'")
            speak("You Search  Wikipedia Please Tell 'Your Command + Wikipedia'" )
            print("Use YouTube Please Tell 'OPEN YOUTUBE'")
            speak("Use YouTube Please Tell 'OPEN YOUTUBE'")
            print("Use Google  Please Tell 'OPEN GOOGLE'")
            speak("Use Google  Please Tell 'OPEN GOOGLE'")
            print("Use Music   Please Tell 'PLAY MUSIC'")
            speak("Use Music   Please Tell 'PLAY MUSIC'")
            print("Use VScode  Please Tell 'OPEN VSCODE'")
            speak("Use VScode  Please Tell 'OPEN VSCODE'")
            print("Use Chrome  Please Tell 'OPEN CHROME'")
            speak("Use Chrome  Please Tell 'OPEN CHROME'")
            print("You want to Know the Current Time Please tell 'The Time'")
            speak("You want to Know the Current Time Please tell 'The Time'")
            print("You take rest please tell 'TAKE REST' I am also take rest")
            speak("You take rest please tell 'TAKE REST' I am also take rest")
            print()
            while True:    # "while True" is infinitly run the loop whenever the condition is False.
                print("Please tell what can i do ?")
                speak("Please tell what can i do")
                print()
                commands_2=takecommand().lower()
                # it calling the "takecommand()" function and that function return "query" value.
                # "lower()" function is used to convert your returned "query" value in lower case.
                if "wikipedia" in commands_2:
                    speak("search in wikipedia")
                    commands_2=commands_2.replace("wikipedia","searching....")
                    # the replace function is used to replace the word.
                    #if user question contain wikipedia name replace searching....
                    #eg : pyhton wikipedia replace python searching....
                    results=wikipedia.summary(commands_2,sentences=2)
                    #wikipedia modul contain summary() method is used for to search your commands 2_line of sentence in google.
                    speak("According to wikipedia")
                    print(results)
                    speak(results)

                elif "open youtube" in commands_2:
                    speak("Know YouTube is opening")
                    webbrowser.open("youtube.com")
                    #webbrowser module contain open() method is uded to open("user said website")

                elif "open google" in commands_2:
                    speak("Know Google is opening")
                    webbrowser.open("google.com")
                    #webbrowser module contain open() method is uded to open("user said website")

                # Making ALPHA to "play music"
                elif "play music" in commands_2:
                    speak("Know Music is Playing")
                    music="C:\\Program Files\\information\\songs\\love songs"
                    # It is a path of the music file in your computer
                    # Use double slash insead of single slash because single slash is escape sequence.
                    songs=os.listdir(music)
                    # "listdir" function is used to change your song in list by list.
                    os.startfile(os.path.join(music,songs[4]))
                    # "startfile" function is used to start your file in the operating system
                    # "join" function is used to auto correct your path if any symbols or slashes mistakenly given.
                    # songs[4] is listed song index value.  

                elif "open vs code" in commands_2:
                    speak("Know VScode is opening")
                    openpath01="C:\\Users\\Rasu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    # It is a path of the VScode file in your computer
                    # Use double slash insead of single slash because single slash is escape sequence.
                    os.startfile(openpath01)
                    # "startfile" function is used to start your file in the operating system

                elif "open chrome" in commands_2:
                    speak("Know Chrome is opening")
                    openpath02="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    # It is a path of the chrome file in your computer
                    # Use double slash insead of single slash because single slash is escape sequence.
                    os.startfile(openpath02)
                    # "startfile" function is used to start your file in the operating system

                elif "the time" in commands_2:
                    time=datetime.datetime.now().strftime("%H:%M") 
                    #"strftime()" function is used to manually Format your time.
                    print("Know the Time is",time)
                    speak(time)

                elif "take rest" in commands_2:
                    print("Thanks for give me a time to take rest.")
                    speak("Thanks for give me a time to take rest")
                    print()
                    break  # "break" keyword is used to End this loop and go to Upper loop.

                else:
                    print("sorry you could say Wrong Command.")
                    speak("sorry you could say Wrong Command")
                    print()

        elif "close alpha" in commands_1:
            print("Ok,I know you are very happy to use me. Know,I am going to sleep. Good Bye, See You Again.")
            speak("Ok,I know you are very happy to use me. Know,I am going to sleep. Good Bye, See You Again")
            exit()  # "exit()" function is used to terminate this program.
        
        else:
            print("sorry you could say Wrong Command.")
            speak("sorry you could say Wrong Command")