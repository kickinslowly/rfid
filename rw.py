import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def main():
    # Initialize RFID reader
    reader = SimpleMFRC522()

    try:
        while True:
            print("\nWhat would you like to do?")
            print("Enter 'r' to read from an RFID tag.")
            print("Enter 'w' to write to an RFID tag.")
            print("Enter 'q' to quit.")
            action = input("Your choice: ").strip().lower()

            if action == 'r':
                # Read RFID tag
                print("Place your RFID tag near the reader to read.")
                rfid_id, text = reader.read()
                print(f"Tag ID: {rfid_id}")
                print(f"Text: {text}")

            elif action == 'w':
                # Write to RFID tag
                print("Place your RFID tag near the reader to write.")
                rfid_id, existing_text = reader.read()
                print(f"Tag ID: {rfid_id}")
                print(f"Existing text: {existing_text}")
                overwrite = input("Do you want to overwrite the text? (y/n): ").strip().lower()
                if overwrite == 'y':
                    new_text = input("Enter the new text to write: ").strip()
                    print("Writing to the RFID tag...")
                    reader.write(new_text)
                    print("Write complete!")
                else:
                    print("Text write operation canceled.")

            elif action == 'q':
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid input. Please enter 'r', 'w', or 'q'.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
