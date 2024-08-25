import requests
import time
import winsound
from tkinter import Tk, Label, Button, Frame, PhotoImage
from threading import Thread

API_URL = "https://alerts-history.oref.org.il/Shared/Ajax/GetAlarmsHistory.aspx?lang=en&mode=1"
IMAGE_PATH = "notification_image.png"
SOUND_PATH = "notification_sound.wav"

# Unicode symbols for category icons
CATEGORY_ICONS = {
    "Missiles": "🚀",
    "Drones": "🛩️",
}

def fetch_latest_incidents():
    response = requests.get(API_URL)
    return response.json()

def play_sound():
    winsound.Beep(300, 100)
    winsound.Beep(300, 100)

def show_popup(incident):
    play_sound()

    root = Tk()
    root.overrideredirect(1)
    root.attributes('-topmost', True)  # Keep the window on top

    background_color = "#2E3440"
    text_color = "#D8DEE9"
    accent_color = "#81A1C1"
    root.configure(bg=background_color)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    taskbar_height = 40  
    popup_width = 320
    popup_height = 180
    x = screen_width - popup_width - 10
    y = screen_height - popup_height - taskbar_height - 10

    root.geometry(f"1x1+{x + popup_width // 2}+{y + popup_height // 2}")  

    frame = Frame(root, bg=background_color, padx=10, pady=10)
    frame.pack(fill='both', expand=True)

    try:
        image = PhotoImage(file=IMAGE_PATH)
        image_label = Label(frame, image=image, bg=background_color)
        image_label.image = image
        image_label.pack(side='top', fill='both', expand=True)
    except Exception as e:
        print(f"Error loading image: {e}")

    # Close button
    close_button = Button(frame, text="✖", command=root.destroy, bg=background_color, fg=accent_color,
                          relief='flat', font=("Arial", 14))
    close_button.place(x=popup_width-30, y=10, width=20, height=20)

    def on_enter(event):
        close_button.config(fg='#FF6C6C')

    def on_leave(event):
        close_button.config(fg=accent_color)

    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)

    # Get the icon for attack type
    category_icon = CATEGORY_ICONS.get(incident['category_desc']) 

    # Alert text
    alert_text = (
        f"🔔 Alert: {incident['data']}\n"
        f"📅 Date: {incident['date']}\n"
        f"🕒 Time: {incident['time']}\n"
        f"{category_icon} {incident['category_desc']}"
    )
    alert_label = Label(frame, text=alert_text, bg=background_color, fg=text_color, font=("Arial", 12))
    alert_label.pack(side='left', fill='both', expand=True)

    # Animation
    def animate_popup():
        for size in range(1, 11):
            current_width = int(popup_width * size / 10)
            current_height = int(popup_height * size / 10)
            root.geometry(f"{current_width}x{current_height}+{x + (popup_width - current_width) // 2}+{y + (popup_height - current_height) // 2}")
            root.update_idletasks()
            time.sleep(0.03)

    # Run the animation
    root.after(100, animate_popup)

    root.after(10000, root.destroy)  # Auto-close after 10 seconds
    root.mainloop()

def monitor_incidents():
    seen_ids = set()
    while True:
        incidents = fetch_latest_incidents()
        if incidents:
            latest_incident = incidents[0]
            # Show the initial popup only if the latest incident was within the last 5 minutes
            incident_time = time.strptime(latest_incident['alertDate'], "%Y-%m-%dT%H:%M:%S")
            current_time = time.gmtime()
            time_diff = time.mktime(current_time) - time.mktime(incident_time)
            if latest_incident['rid'] not in seen_ids and time_diff <= 300:  # 5 minutes
                seen_ids.add(latest_incident['rid'])
                show_popup(latest_incident)
        time.sleep(10)  # Poll every 10 seconds

if __name__ == "__main__":
    thread = Thread(target=monitor_incidents)
    thread.start()
