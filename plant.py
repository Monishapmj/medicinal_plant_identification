		MEDICINAL PLANT IDENTIFICATION                             
 FRONT END DESIGN
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageOps
import webbrowser
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import csv
import os
import hashlib
# File to store user credentials
USER_DATA_FILE = "users.csv"

# Ensure user data file exists
if not os.path.exists(USER_DATA_FILE):
with open(USER_DATA_FILE, "w") as file:
file.write("username,password\n")

# Hash password for secure storage
def hash_password(password):
return hashlib.sha256(password.encode()).hexdigest()

# Ensure results file exists
SAVED_RESULTS_FILE = "plant_predictions.csv"
if not os.path.exists(SAVED_RESULTS_FILE):
with open(SAVED_RESULTS_FILE, mode="w", newline="") as file:
writer = csv.writer(file)
writer.writerow(["Plant", "Confidence", "Description"])

# Plant descriptions and details
plant_info = {
# Plant information goes here (same as in the original code)
"Aloe vera": {
"description": "Aloe vera is a herb with succulent leaves that are arranged in a rosette. The leaves are grey to green and sometimes have white spots on their surfaces.",
"medicinal_uses": "Helps heal burns, improves skin health, and aids digestion.",
"remedies": "Apply aloe gel on burns or mix with water to create a digestive drink.",
"cultural_significance": "Often used in rituals and as a symbol of health and protection.",
"video": "C:\\Users\\ramac\\Downloads\\aloe.mp4"
},
"Betel": {
"description": "Betel or Sireh is a climbing vine with glossy, heart-shaped leaves.",
"medicinal_uses": "Used for oral health, digestion, and reducing headaches.",
"remedies": "Chew betel leaves with lime for digestion or make a paste for headaches.",
"cultural_significance": "Symbolizes hospitality in South Asian cultures.",
"video": "C:\\Users\\ramac\\OneDrive\\Pictures\\video\\betel.mp4"
},
"Castor":{
"description": "Castor is a fast-growing, tropical plant known for its large, glossy leaves and oil-rich seeds.",
"medicinal_uses":"Castor oil is used as a laxative, anti-inflammatory, and for treating skin and joint ailments.",
"remedies": "It is commonly applied for hair growth, skin hydration, and relieving constipation.",
"cultural_significance": "Castor holds importance in traditional rituals and Ayurvedic practices for purification and healing.",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\castor.mp4"
},
"Curry":{
"description":"Curry leaves are aromatic, small, green leaves from a tropical tree, widely used in South Asian cuisine for their unique flavor.",
"medicinal_uses":"Curry leaves are known for their ability to aid digestion, regulate blood sugar levels, and improve heart health.",
"remedies":"They are used in traditional remedies to treat diarrhea, nausea, and hair loss, often in the form of powders, pastes, or decoctions.",
"cultural_significance":"Curry leaves hold a special place in Indian culture, symbolizing health and prosperity, and are often used in Ayurveda for their therapeutic properties.",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\curry.mp4"
},
"Guava":{
"description":"Guava is a tropical fruit-bearing tree known for its sweet, fragrant fruit with edible seeds and rich nutritional value.",
"medicinal_uses":"Guava is valued for its high vitamin C content, aiding immunity, improving digestion, and regulating blood sugar levels.",
"remedies":"Guava leaves are used in traditional remedies to treat diarrhea, toothaches, and skin infections, often brewed as a tea or applied as a paste.",
"cultural_significance":"Guava symbolizes health and vitality in various cultures and is often associated with traditional healing practices and rituals.",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\guava.mp4"
},
"Neem":{
"description":"Neem is a fast-growing, evergreen tree known for its bitter leaves, seeds, and bark with potent medicinal properties.",
"medicinal_uses":"Neem is used to treat skin conditions, boost immunity, and act as an antimicrobial, anti-inflammatory, and blood purifier.",
"remedies":"Neem leaves, oil, and bark are used in traditional remedies for acne, dandruff, wound healing, and managing diabetes.",
"cultural_significance":"Neem is revered in many cultures for its symbolic association with purity, protection, and its role in Ayurvedic and spiritual practices",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\neem.mp4"
},
"Onion":{
"description":"Onion is a bulbous vegetable with a pungent aroma, widely used in culinary practices and known for its layered structure.",
"medicinal_uses":"Onions are valued for their antioxidant, anti-inflammatory, and antimicrobial properties, supporting heart health and immunity.",
"remedies":"Onion juice is traditionally used to treat colds, coughs, hair fall, and skin pigmentation, often applied topically or consumed raw.",
"cultural_significance":"Onions hold culinary and cultural importance worldwide, symbolizing endurance and versatility, and are used in traditional healing practices.",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\onion.mp4"
},
"Papaya":{
"description":"Papaya is a tropical fruit-bearing plant known for its sweet, orange flesh, black seeds, and high nutritional content.",
"medicinal_uses":"Papaya aids digestion, boosts immunity, improves skin health, and is used to manage conditions like constipation and inflammation.",
"remedies":"Papaya fruit, seeds, and leaves are traditionally used to treat indigestion, wounds, and even dengue fever, often consumed or applied directly.",
"cultural_significance":"Papaya is considered a symbol of nourishment and healing in various cultures and is deeply integrated into traditional medicine and rituals.",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\papaya.mp4"
},
"Spinach1":{
"description":"Spinach is a leafy green vegetable rich in nutrients, known for its tender leaves and versatility in culinary dishes.",
"medicinal_uses":"Spinach is packed with iron, vitamins, and antioxidants, supporting eye health, bone strength, and overall immunity.",
"remedies":"Spinach is used in traditional remedies to treat anemia, promote digestion, and detoxify the body when consumed as juice or soup.",
"cultural_significance":"Spinach symbolizes strength and vitality, often featured in folklore and valued in traditional diets for its health-promoting properties",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\spinach.mp4"
},
"Tulsi":{
"description":"Tulsi, also known as Holy Basil, is a sacred aromatic herb with small green leaves, revered for its spiritual and medicinal properties.",
"medicinal_uses":"Tulsi is known for its adaptogenic, antimicrobial, and anti-inflammatory properties, supporting respiratory health, stress relief, and immunity.",
"remedies":"Tulsi leaves are used in traditional remedies to treat colds, coughs, fever, and skin infections, often consumed as tea or applied as a paste.",
"cultural_significance":"Tulsi holds a divine status in Indian culture, symbolizing purity, protection, and prosperity, and is deeply integrated into Ayurvedic and spiritual practices",
"video":"C:\\Users\\ramac\\OneDrive\\Pictures\\video\\tulsi.mp4"
}
}

# Class mapping
class_names = {
0: 'Aloe vera',
1: 'Betel',
2: 'Castor',
3: 'Curry',
4: 'Guava',
5: 'Neem',
6: 'Onion',
7: 'Papaya',
8: 'Spinach1',
9: 'Tulsi'
}

# Image specifications
IMG_HEIGHT = 224
IMG_WIDTH = 224

# Load the trained model
MODEL_PATH = 'ayurvedic_plant_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

last_prediction = None

def predict_plant(image_path):
img = image.load_img(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)
predictions = model.predict(img_array)
predicted_class = class_names[np.argmax(predictions)]
confidence = np.max(predictions)
return predicted_class, confidence

def save_results():
global last_prediction
if last_prediction is None:
messagebox.showwarning("No Prediction", "No prediction available to save!")
return
predicted_class, confidence, description = last_prediction
try:
with open(SAVED_RESULTS_FILE, mode="a", newline="") as file:
writer = csv.writer(file)
writer.writerow([predicted_class, f"{confidence:.2f}", description])
messagebox.showinfo("Success", "Results saved successfully!")
except Exception as e:
messagebox.showerror("Error", f"Failed to save results: {e}")

def load_image():
global last_prediction
file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
if not file_path:
return
try:
img = Image.open(file_path)
img_resized = ImageOps.contain(img, (300, 300))
img_tk = ImageTk.PhotoImage(img_resized)
panel.config(image=img_tk)
panel.image = img_tk

predicted_class, confidence = predict_plant(file_path)
result_label.config(text=f"Predicted: {predicted_class}\nConfidence: {confidence:.2f}")

plant_data = plant_info.get(predicted_class, {})
description = f"Description: {plant_data.get('description', 'No description available.')}\n\n" \
f"Medicinal Uses: {plant_data.get('medicinal_uses', 'No information available.')}\n\n" \
f"Remedies: {plant_data.get('remedies', 'No remedies available.')}\n\n" \
f"Cultural Significance: {plant_data.get('cultural_significance', 'No information available.')}"
description_label.config(state=tk.NORMAL)
description_label.delete(1.0, tk.END)
description_label.insert(tk.END, description)
description_label.config(state=tk.DISABLED)

last_prediction = (predicted_class, confidence, plant_data.get('description', 'No description available.'))

video_url = plant_data.get("video", None)
if video_url:
video_button.config(state=tk.NORMAL, command=lambda: open_video(video_url))
else:
video_button.config(state=tk.DISABLED)
except Exception as e:
messagebox.showerror("Error", f"Failed to process image:\n{e}")

def reset_image():
panel.config(image="")
panel.image = None
result_label.config(text="Result will be displayed here")
description_label.config(state=tk.NORMAL)
description_label.delete(1.0, tk.END)
description_label.config(state=tk.DISABLED)

def open_excel_file():
try:
if os.name == 'nt':
os.startfile(SAVED_RESULTS_FILE)
else:
subprocess.call(['open', SAVED_RESULTS_FILE])
except Exception as e:
messagebox.showerror("Error", f"Failed to open file: {e}")


def open_video(url):
webbrowser.open(url)

def exit_application():
root.destroy()

def show_about():
about_window = tk.Toplevel(root)
about_window.title("About the Project")
about_window.geometry("400x200")
about_text = "This project identifies medicinal plants and provides details like descriptions, medicinal uses, and remedies.\n\n" \
"Developed using TensorFlow, Keras, and Tkinter."
about_label = tk.Label(about_window, text=about_text, font=("Arial", 12), wraplength=350, justify="center")
about_label.pack(pady=20)

def plant_prediction_interface():
global panel, result_label, description_label, video_button

for widget in root.winfo_children():
widget.destroy()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save Results", command=save_results)
file_menu.add_command(label="Exit", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

title_label = tk.Label(root, text="Medicinal Plant Identification", font=("Arial", 20, "bold"), bg="RoyalBlue", fg="white")
title_label.pack(pady=10)

panel_frame = tk.Frame(root, bd=2, relief=tk.GROOVE, bg="white")
panel_frame.pack(pady=10)
panel = tk.Label(panel_frame, bg="white")
panel.pack()

button_frame = tk.Frame(root, bg="RoyalBlue")
button_frame.pack(pady=10)

load_button = tk.Button(button_frame, text="Load Image", command=load_image, font=("Arial", 12), bg="#4CAF50", fg="white")
load_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(button_frame, text="Reset Image", command=reset_image, font=("Arial", 12), bg="orange", fg="white")
reset_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(button_frame, text="Save Result", command=save_results, font=("Arial", 12), bg="blue", fg="white")
save_button.grid(row=0, column=2, padx=10)

open_button = tk.Button(button_frame, text="Activate Spreadsheet", command=open_excel_file, font=("Arial", 12), bg="purple", fg="white")
open_button.grid(row=0, column=3, padx=10)

result_label = tk.Label(root, text="Result will be displayed here", font=("Arial", 12), fg="black", bg="RoyalBlue")
result_label.pack(pady=10)

description_label = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), height=10, bg="#F0F0F0", fg="black", state=tk.DISABLED)
description_label.pack(pady=10)


video_button = tk.Button(root, text="Visualize Demo", state=tk.DISABLED, font=("Arial", 12), bg="green", fg="white")
video_button.pack(pady=10)

def launch_plant_prediction():
global root
root = tk.Tk()
root.title("Medicinal Plant Identification")
root.geometry("800x800")
root.configure(bg="RoyalBlue")
plant_prediction_interface()
root.mainloop()

# Login/Signup Logic
def login_signup():
global root
root = tk.Tk()
root.title("Login/Signup")
root.geometry("400x300")
root.configure(bg="RoyalBlue")

title_label = tk.Label(root, text="Login / Signup", font=("Arial", 20, "bold"), bg="RoyalBlue", fg="white")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="white", bd=2, relief=tk.RIDGE)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

username_label = tk.Label(frame, text="Username:", font=("Arial", 12), bg="white")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
username_entry = tk.Entry(frame, font=("Arial", 12), width=25)
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label = tk.Label(frame, text="Password:", font=("Arial", 12), bg="white")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
password_entry = tk.Entry(frame, font=("Arial", 12), width=25, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

def login():
username = username_entry.get()
password = password_entry.get()
hashed_password = hashlib.sha256(password.encode()).hexdigest()
try:
with open("users.csv", "r") as file:
users = file.readlines()# Read all lines into the 'users' variable
except FileNotFoundError:
messagebox.showerror("Error", "User data file not found!")
return

for user in users[1:]:  # Skip the header row if it exists
try:
stored_username, stored_password = user.strip().split(",")
if stored_username == username and stored_password == hashed_password:
messagebox.showinfo("Success", "Login successful!")
root.destroy()
launch_plant_prediction()
return
except ValueError:
continue  # Skip malformed lines

messagebox.showerror("Error", "Invalid username or password.")

def signup():
username = username_entry.get().strip()
password = password_entry.get().strip()

if not username or not password:
messagebox.showwarning("Error", "All fields are required!")
return

hashed_password = hash_password(password)
with open(USER_DATA_FILE, "r") as file:
users = file.readlines()

for user in users:
if user.split(",")[0] == username:
messagebox.showerror("Error", "Username already exists!")
return

with open(USER_DATA_FILE, "a") as file:
file.write(f"{username},{hashed_password}\n")

messagebox.showinfo("Success", "Signup successful! You can now log in.")
username_entry.delete(0, tk.END)
password_entry.delete(0, tk.END)

login_button = tk.Button(frame, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", command=login)
login_button.grid(row=2, column=0, padx=10, pady=20, sticky="w")
signup_button = tk.Button(frame, text="Signup", font=("Arial", 12), bg="blue", fg="white", command=signup)
signup_button.grid(row=2, column=1, padx=10, pady=20, sticky="e")
root.mainloop()

# Run Login/Signup Interface
login_signup()
