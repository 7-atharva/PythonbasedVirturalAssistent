import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import math
import pyautogui  # Added import for pyautogui
import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_password():
    speak("Sir, please provide the password.")
    password = take_command()
    return password

def authenticate():
    password = get_password()
    correct_password = "black panther"  # Change this to your desired password

    if password == correct_password:
        speak("Authentication successful. Welcome, Atharva!")
        return True
    else:
        speak("Incorrect password. Please enter the correct password, sir.")
        return False

def wish_me():
    speak("Hello! I am Alexa.")
    speak("Please wait for authentication.")

    authenticated = authenticate()
    if not authenticated:
        exit()

    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("How can I assist you, Atharva?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 2
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query.lower()

def open_youtube(search_query):
    search_url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(search_url)

def google_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def wikipedia_search(query):
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def get_time_and_date():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    speak(f"The current time is {current_time} and today's date is {current_date}")

def open_vscode():
    code_path = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(code_path)

def open_androidstudio():
    code_path1 = "C:\\Program Files\\Android\\Android Studio1\\bin\\studio64.exe"
    os.startfile(code_path1)

def open_paint():
    paint_path = "C:\\Windows\\System32\\mspaint.exe"
    os.startfile(paint_path)

def draw_square():
    speak("Drawing a square...")
    size = 100  # You can adjust the size of the square
    pyautogui.click()  # Click to focus on Paint
    pyautogui.moveTo(500, 500)  # Move to the starting position
    pyautogui.dragRel(size, 0, duration=1)  # Draw the top side
    pyautogui.dragRel(0, size, duration=1)  # Draw the right side
    pyautogui.dragRel(-size, 0, duration=1)  # Draw the bottom side
    pyautogui.dragRel(0, -size, duration=1)  # Draw the left side

def draw_line():
    speak("Drawing a line...")
    length = 200  # You can adjust the length of the line
    pyautogui.click()  # Click to focus on Paint
    pyautogui.moveTo(500, 500)  # Move to the starting position
    pyautogui.dragRel(length, 0, duration=1)  # Draw the line

def draw_circle():
    speak("Drawing a circle...")
    radius = 50  # You can adjust the radius of the circle
    pyautogui.click()  # Click to focus on Paint
    pyautogui.moveTo(500, 500)  # Move to the starting position

    # Draw the circle using polar coordinates
    for angle in range(0, 360, 5):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        pyautogui.dragRel(x, y, duration=0.05)  # Draw a small segment of the circle

def draw_flower():
    speak("Drawing a flower...")
    pyautogui.click()  # Click to focus on Paint
    pyautogui.moveTo(500, 500)  # Move to the starting position

    # Draw the flower using polar coordinates
    for petal in range(6):  # You can adjust the number of petals
        draw_petal()
        pyautogui.rotate(60)  # Rotate for the next petal

def draw_petal():
    radius = 50  # You can adjust the size of the petal
    petal_length = 100  # You can adjust the length of the petal
    pyautogui.dragRel(0, radius, duration=0.1)  # Draw the first half of the petal
    pyautogui.dragRel(petal_length, 0, duration=0.1)  # Draw the petal's length
    pyautogui.dragRel(0, -radius, duration=0.1)  # Draw the second half of the petal
    pyautogui.dragRel(-petal_length, 0, duration=0.1)  # Return to the starting position

def ask_for_drawing():
    speak("Sir, what would you like to draw in Paint? You can say 'square', 'circle',flower or 'line'")
    command = take_command()

    if "square" in command:
        draw_square()    
    elif "circle" in command:
        draw_circle()
    elif "line" in command:
        draw_line()
    elif "flower" in command:
        draw_flower()
        draw_petal()   
    else:
        speak("I'm sorry, I didn't understand. Please say 'square', 'circle', or 'line'.")

def minimize_window():
    pyautogui.hotkey('win', 'd')  # Minimize the current window

def refresh_screen():
    pyautogui.hotkey('f5')  # Refresh the screen

def close_window():
    pyautogui.hotkey('alt', 'f4')  # Close the current window

def close_current_tab():
    speak("Closing the current tab...")
    pyautogui.hotkey('ctrl', 'w')  # Close the current tab

def move_mouse(x, y):
    pyautogui.moveTo(x, y)

def click_mouse():
    pyautogui.click()

def close_window():
    pyautogui.hotkey('alt', 'f4')  # Close the current window

def close_current_tab():
    speak("Closing the current tab...")
    pyautogui.hotkey('ctrl', 'w')  # Close the current tab    

def minimize_window():
    pyautogui.hotkey('win', 'd')  # Minimize the current window

def main():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                continue

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    landmarks = hand_landmarks.landmark

                    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]

                    x, y = int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0])

                    cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

                    move_mouse(x, y)

                    # Check if the thumb is up (click gesture)
                    if thumb_tip.y < index_finger_tip.y:
                        click_mouse()

                    # Check if the thumb is to the right of the index finger (close window gesture)
                    if thumb_tip.x > index_finger_tip.x:
                        close_window()

                    # Check if the thumb is to the left of the index finger (minimize window gesture)
                    if thumb_tip.x < index_finger_tip.x:
                        minimize_window()

            cv2.imshow('Virtual Mouse', frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def listen_and_execute():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said: ", command)

        if "wikipedia" in command:
            speak("Searching Wikipedia...")
            search_query = command.replace("wikipedia", "")
            wikipedia_search(search_query)

        elif "open youtube" in command:
            search_query = command.replace("open youtube and search for", "")
            search_query = search_query.replace("open youtube", "")
            search_query = search_query.strip()
            open_youtube(search_query)

        elif "open google" in command:
            search_query = command.replace("open google and search for", "")
            search_query = search_query.replace("open google", "")
            search_query = search_query.strip()
            google_search(search_query)

        elif "search for" in command and ("youtube" in command or "google" in command):
            search_query = command.replace("search for", "").strip()
            if "youtube" in command:
                open_youtube(search_query)
            elif "google" in command:
                google_search(search_query)

        elif "google search for" in command:
            search_query = command.replace("google search for", "").strip()
            google_search(search_query)

        elif "time" in command or "date" in command:
            get_time_and_date()

        elif "open vs code" in command:
            speak("Wait sir, vs code is opening!")
            open_vscode()

        elif "open android studio" in command:
            speak("Wait sir, android studio is opening!")
            open_androidstudio()

        elif "open paint" in command:
            speak("Opening Paint...")
            open_paint()

        elif "draw a square" in command:
            speak("Drawing a square...")
            draw_square()

        elif "draw a line" in command:
            speak("Drawing a line...")
            draw_line()

        elif "draw a circule" in command:
            speak("Drawing a Circule...")
            draw_circle()  

        elif "draw a flower" in command:
            speak("Drwaing a flowe...")
            draw_flower()
            draw_petal()     

        elif "minimise the current screen" in command:
            speak("Minimizing the current screen...")
            minimize_window()

        elif "refresh the screen" in command:
            speak("Refreshing the screen...")
            refresh_screen()

        elif "close current window" in command:
            if "close the current screen" in command:
                close_window()    
            speak("Closing the current window...")
            close_window()
        
        elif "close current tab" in command:
            speak("Closing the current tab...")
            close_current_tab()    

        #elif "hand gesture control activated " in command:
           # speak("Hands gesture contorl activated ,activate hand gesture control...")
           # hand_gesture_control()

        elif "exit" in command:
            speak("Thanks for using Alexa. Have a good day, sir!")
            exit()

        else:
            print("Command not recognized.")

    except sr.UnknownValueError:
        speak("Could not understand Your audio. please speak Again...!")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")

if __name__ == "__main__":
    wish_me()
    while True:
        listen_and_execute()
        
