#Learning How to use GUI

#You're supposed to import tk
import tkinter as tk

#Creates a Window
window = tk.Tk()

#Sets The size of the Window
window.geometry("500x500")

#Sets the Icon of the window
window.wm_iconbitmap('favicon.ico')

#Sets the title of the window
#window.title("Scummy Hero Super Mario 64")

#Stores a variable called rules
Rules = tk.Label(window, text="Rules")

#Create a text entry
Oh_no = tk.Entry(window)

#Create a button
OHNOOOOOOOO = tk.Button(window, text="OHNOOOOOOOO")

#Puts in the variable into our window
Rules.pack()
Oh_no.pack()
OHNOOOOOOOO.pack()

#Creates the Actual window
window.mainloop()

# ^-^ is the testing window, time to recreate a login screen.
#__________________________________________________
while True:
	#Creates Window
	window = tk.Tk()

	#Sets Window size

	window.geometry("1000x1100")
	#Adds New Icon to the window

	#window.wm_iconbitmap('faviconFacebook.ico')#faviconFacebook.ico  #Mariobest.ico

	window.configure(background="blue")

	window.title("Welcome!")

	#facebook = tk.PhotoImage(file="Newfacebook.gif")
	#w = tk.Label(window, image=facebook)

	#What to do.

	Greeting = tk.Label(window, text="Welcome, Please Login to recieve your Facebook Status")

	#Apology
	Sorry = tk.Label(window, text="We're sorry, our updated servers are down")
	Sorrycont = tk.Label(window, text="You can still login")
	#Username

	Username = tk.Label(window, text="Username:", bg="blue")

	Username_Text_Entry = tk.Entry(window)

	#Password

	Password = tk.Label(window, text="Password:", bg="blue")

	Password_Text_Entry = tk.Entry(window)

	#The Scammings

	Name = tk.Label(window, text="Name Please:", bg="blue")
	Name_Text_Entry = tk.Entry(window)

	Social_security_number = tk.Label(window, text="Social Security Number required for Security", bg="blue")
	Social_security_number_Text_Entry = tk.Entry(window)

	Credit_card_issue = tk.Label(window, text="MasterCard Or VISA ", bg="blue")
	Credit_card_issue_Text_Entry = tk.Entry(window)

	Other = tk.Label(window, text="Credit Card Number", bg= "blue")
	Other_Text_Entry = tk.Entry(window)

	PIN_NUMBER = tk.Label(window, text="PIN NUMBER")
	PIN_NUMBER_TEXT_ENTRY = tk.Entry(window)

	CVC = tk.Label(window, text="CVC (FOUND TO CREDIT CARD)")
	CVC_TEXT_ENTRY = tk.Entry(window)

	TankYou = tk.Label(window, text="Thank you friend ( ͡° ͜ʖ ͡°) ")

	#Login Button

	Login = tk.Button(window, text="Login", fg="red", bg="white")

	#Joke
	joke = tk.Label(window, text="WE ARE DEFINTLY NO SCAMMING MY NAME IS STEVE ROBERTSON CREATOR OF FACEBOO0K")
	#Time To Pack

	w.pack()
	Greeting.pack()
	Sorry.pack()
	Sorrycont.pack()
	Username.pack()
	Username_Text_Entry.pack()
	Password.pack()
	Password_Text_Entry.pack()
	Name.pack()
	Name_Text_Entry.pack()
	Social_security_number.pack()
	Social_security_number_Text_Entry.pack()
	Credit_card_issue.pack()
	Credit_card_issue_Text_Entry.pack()
	Other.pack()
	Other_Text_Entry.pack()
	CVC.pack()
	CVC_TEXT_ENTRY.pack()
	Login.pack()
	TankYou.pack()
	joke.pack()

# NOTE: Some pictures the program is unable to obtain, I'll try to commit them somewhere

	#_____________________
	#To Load Window
	window.mainloop()
