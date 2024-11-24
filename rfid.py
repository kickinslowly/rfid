import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pygame

# Initialize RFID reader
reader = SimpleMFRC522()

# Initialize pygame mixer
pygame.mixer.init()

print("Ready to detect RFID tags!")

try:
    while True:
        print("Waiting for a tag...")
        rfid_id, text = reader.read()
        print(f"Detected RFID ID: {rfid_id}, Text: {text}")

        # Define actions based on RFID ID
        if rfid_id == 7894286177:
            print("Playing hello.mp3...")
            pygame.mixer.music.load("hello.mp3")
            pygame.mixer.music.play()
        elif rfid_id == 291003226748:
            print("Playing example.mp3...")
            pygame.mixer.music.load("nfl.mp3")
            pygame.mixer.music.play()
        else:
            print("Unknown RFID ID!")

        # Wait until playback is done
        while pygame.mixer.music.get_busy():
            continue

finally:
    GPIO.cleanup()
