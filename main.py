# pip instal eel
import eel

eel.init('BIT CAVE') #Folder Name

play = input("do you want to enter?")
if play.lower() != "yes":
    quit()
if play.lower() == "yes":
    @eel.expose
    def app(): # App main function
        print('app running')


app()
   
eel.start('main.html',size=(500,600)) # Run app windows

user_quit = input("do you want to quit?")
if user_quit.lower() == "yes":
    quit()




    










