import tkinter as tk
import threading
from tkinter import ttk
from PIL import Image, ImageTk
import speech_to_text
import Voice_Commands
from pathlib import Path
TRINITY_DIR = Path(__file__).resolve().parent.parent
# Trinity GUI using Tkinter
root = tk.Tk()
root.title("Trinity")
root.tk.call("tk", "appname", "Trinity")

root.geometry("1080x1920")
root.config(bg="black")

# Loading and resizing images for the GUI
Trinity_T_Image_original = Image.open(TRINITY_DIR / "Trinity_Images" / "Trinity_T_Image.png")
Trinity_T_Image = Trinity_T_Image_original.resize((500, 700), Image.Resampling.LANCZOS)
Command_List_Button = Image.open(TRINITY_DIR / "Trinity_Images" / "Command_List_Button.png")
Command_List_Button = Command_List_Button.resize((200, 100), Image.Resampling.LANCZOS)
Sound_ON_Icon = Image.open(TRINITY_DIR / "Trinity_Images" / "sound_on_icon.png")
Sound_ON_Icon = Sound_ON_Icon.resize((100, 100), Image.Resampling.LANCZOS)
Sound_OFF_Icon = Image.open(TRINITY_DIR / "Trinity_Images" / "sound_off_icon.png")
Sound_OFF_Icon = Sound_OFF_Icon.resize((100, 100), Image.Resampling.LANCZOS)


    

#Defining image labels for the GUI
img1 = ImageTk.PhotoImage(Trinity_T_Image)
img2 = ImageTk.PhotoImage(Command_List_Button)
img2_hover = ImageTk.PhotoImage(
    Command_List_Button.resize((220, 110), Image.Resampling.LANCZOS)
)
img3 = ImageTk.PhotoImage(Sound_ON_Icon)
img4 = ImageTk.PhotoImage(Sound_OFF_Icon)


# Function to open the command list window
def open_command_list():
    command_list = tk.Toplevel(root)
    command_list.title("Command List")
    command_list.geometry("900x700")

    style = ttk.Style()
    style.configure(
        "Treeview", 
        background="black",
        foreground="#C1086B", 
        fieldbackground="black")
    
    style.configure(
        "Treeview.Heading", 
        background="black", 
        foreground="#C1086B")

    Command_List = ttk.Treeview(
    command_list,
    columns=("number", "command", "description"),
    show="headings"

)
    
    # Adding the command list with default commands
    Command_List.heading("number", text="#")
    Command_List.heading("command", text="Command")
    Command_List.heading("description", text="Description")

    Command_List.column("number", width=40, anchor="center")
    Command_List.column("command", width=180)
    Command_List.column("description", width=400)

    Command_List.insert("", tk.END, values=("1", '"hello"', "Plays a greeting audio file."))
    Command_List.insert("", tk.END, values=("2", '"trinity exit"', "Plays a goodbye audio file when the user says 'trinity exit'."))
    Command_List.insert("", tk.END, values=("3", '"trinity open brave" / "trinity open browser"', "Launches the Brave browser application."))
    Command_List.insert("", tk.END, values=("4", '"trinity open youtube"', "Opens YouTube in Brave."))
    Command_List.insert("", tk.END, values=("5", '"trinity open steam"', "Opens the Steam store in Brave."))
    Command_List.insert("", tk.END, values=("6", '"trinity open discord"', "Launches the Discord application."))
    Command_List.insert("", tk.END, values=("7", '"trinity open spotify"', "Launches the Spotify application."))
    Command_List.insert("", tk.END, values=("8", '"trinity open github"', "Opens GitHub in Brave."))
    Command_List.insert("", tk.END, values=("9", '"trinity open reddit"', "Opens Reddit in Brave."))
    Command_List.insert("", tk.END, values=("10", '"trinity flip a coin"', "Randomly picks Heads or Tails and prints the result."))
    Command_List.insert("", tk.END, values=("11", '"trinity give me a number"', "Generates a random integer between 1 and 100 and prints it."))
    Command_List.insert("", tk.END, values=("12", '"trinity look up ..."', "Searches Brave for the text after the trigger phrase."))
    Command_List.pack(fill=tk.BOTH, expand=True)

global sound_enabled

sound_enabled = tk.BooleanVar(root, value=True)



def toggle_sound():
    sound_enabled.set(not sound_enabled.get())
    sound_button.config(image=img3 if sound_enabled.get() else img4)
    Voice_Commands.global_sound_enabled = sound_enabled.get()
    if not sound_enabled.get():
        print("Sound is disabled.")
    else:
        print("Sound is enabled.")
    

# Creating the main GUI elements and placing them on the root window
trinity_image_label = tk.Label(
    root,
    image=img1,
    bg="black",
    bd=0,
    highlightthickness=0
)
# Creating the command list button and its hover effects
command_list_button = tk.Button(
    root,
    image=img2,
    command=open_command_list,
    bg="black",
    activebackground="black",
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief=tk.FLAT,
    overrelief=tk.FLAT
)
sound_button = tk.Button(
    root,
    image=img3,
    command=toggle_sound,
    bg="black",
    activebackground="black",
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    relief=tk.FLAT,
    overrelief=tk.FLAT
)


# Functions to handle the hover effects for the command list button
def enlarge_command_button(_event):
    command_list_button.config(image=img2_hover)


def restore_command_button(_event):
    command_list_button.config(image=img2)


command_list_button.bind("<Enter>", enlarge_command_button)
command_list_button.bind("<Leave>", restore_command_button)
trinity_image_label.place(relx=0.5, rely=0.5, anchor="center")
command_list_button.place(relx=0.9, rely=0.9, anchor="center")
sound_button.place(relx=0.1, rely=0.9, anchor="center")
threading.Thread(target=Voice_Commands.VoiceCommands, daemon=True).start()

#Code for the GUI terminal
def Terminal():
    terminal_text = tk.Text(root, width=40, height=5, borderwidth=0, relief="solid", highlightbackground="#C1086B", bg="black", fg="white", font=("Helvetica", 12))
    terminal_text.place(relx=0.8, rely=0.8, anchor="center")
    listening_message_shown = False
    processing_message_shown = False

    def update_terminal():
        nonlocal listening_message_shown, processing_message_shown

        if speech_to_text.startup and not listening_message_shown:
            terminal_text.insert(tk.END, "Listening... Speak now!\n")
            terminal_text.see(tk.END)
            listening_message_shown = True
        elif not speech_to_text.startup:
            listening_message_shown = False

            

        if speech_to_text.processing and not processing_message_shown:
            terminal_text.insert(tk.END, "Processing...\n")
            terminal_text.see(tk.END)
            processing_message_shown = True
        elif not speech_to_text.processing:
            processing_message_shown = False

        if Voice_Commands.command_exicuted ==True:
            terminal_text.insert(tk.END, "Command executed \n")
            terminal_text.see(tk.END)
            Voice_Commands.command_exicuted = False

            

        root.after(100, update_terminal)

    update_terminal()


Terminal()

# Starting the voice commands thread and running the main GUI loop
root.mainloop()


 