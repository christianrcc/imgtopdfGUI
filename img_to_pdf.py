import customtkinter
import os
import random 
from PIL import Image
# This is a simple program that converts images to pdfs. It uses the PIL library to open images and save them as pdfs.
# It also uses the customtkinter library to create the GUI.

location = ""
def get_img_path():
    global location # This is the location of the images
    location = entry1.get() 
    
    try: # This is to check if the location is valid and that no errors occur
        os.chdir(location)
    except FileNotFoundError:
        label1.configure(text="Invalid location. Please enter a valid location", text_color="red")
    except NotADirectoryError:
        label1.configure(text="Invalid location. Please enter a valid location", text_color="red")
    except PermissionError:
        label1.configure(text="Invalid location. Please enter a valid location", text_color="red")
    except OSError:
        label1.configure(text="Invalid location. Please enter a valid location", text_color="red")
    
    if os.path.exists(location): # If the location is valid, the label will change to "Location is valid"
        label1.configure(text="Location is valid", text_color="green")
    else: # If the location is not valid, the label will change to "Invalid location. Please enter a valid location" and the location will be set to an empty string
        label1.configure(text="Invalid location. Please enter a valid location", text_color="red")
        location = ""

def img_to_pdf():
    images = [] # This is a list of images that will be converted to a pdf
    if location != "": # If the location is valid, the images in the location will be opened and added to the list
        for img in os.listdir(location):
            if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
                images.append(Image.open(location + "/" + img))
    if len(images) != 0: # If there are no images in the location, the label will change to "No images found"
        word = "" # This is the name of the pdf file
        for i in range(10): # This generates a random name for the pdf file
            num = random.randint(48, 57)
            word += chr(num)
        for i in range(10):
            num = random.randint(65, 90)
            word += chr(num)
        word += ".pdf"
        
        images[0].save(word, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]) # This saves the images as a pdf
        for img in images:
            img.close()
        
        # This deletes the images in the location
        for img in os.listdir(location):
            if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
                os.remove(location + "/" + img)
        
        label2.configure(text="PDF has been created") # This changes the label to confirm that the pdf has been created
    else:
        label2.configure(text="No images found") # This changes the label to "No images found"
    
    

customtkinter.set_appearance_mode("Light") # This sets the appearance mode of the GUI to light
customtkinter.set_default_color_theme("dark-blue") # This sets the default color theme of the GUI to dark-blue
    
root = customtkinter.CTk() # This creates the root window
root.geometry("800x400") # This sets the size of the root window
root.title("Image to PDF Converter") # This sets the title of the root window 

frame = customtkinter.CTkFrame(root) # This creates a frame in the root window
frame.pack(fill="both", expand=True) # This packs the frame in the root window

canvas = customtkinter.CTkCanvas(frame) # This creates a canvas in the frame
canvas.pack(fill="both", expand=True) # This packs the canvas in the frame
 
label1 = customtkinter.CTkLabel(canvas, text="Enter location of image files", font=("Arial", 24)) # This creates a label in the canvas
label1.pack(padx=10, pady=10) # This packs the label in the canvas 

entry1 = customtkinter.CTkEntry(canvas, placeholder_text="Enter location of image files", font=("Arial", 12), width=250) # This creates an entry in the canvas 
entry1.pack(padx=10, pady=10) # This packs the entry in the canvas 

button1 = customtkinter.CTkButton(canvas, text="Browse", font=("Arial", 16), command=get_img_path) # This creates a button in the canvas 
button1.pack(padx=10, pady=10) # This packs the button in the canvas 

label2 = customtkinter.CTkLabel(canvas, text="This will turn current images into a pdf", font=("Arial", 24)) # This creates a label in the canvas 
label2.pack(padx=10, pady=10) # This packs the label in the canvas 

button2 = customtkinter.CTkButton(canvas, text="Convert", font=("Arial", 16), command=img_to_pdf) # This creates a button in the canvas
button2.pack(padx=10, pady=10) # This packs the button in the canvas

root.mainloop() # This runs the root window

    