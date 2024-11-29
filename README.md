# RFID Python Scripts

This repository contains Python scripts for interfacing with an **RFID-RC522 reader/writer** using a Raspberry Pi. The scripts allow you to:
1. Detect RFID tags and trigger actions such as audio playback (`rfid_audio_player.py`).
2. Read and write text to RFID tags interactively (`rfid_read_write.py`).

---

## Features

- **RFID Detection**: Reads RFID tag IDs and their associated text.
- **Audio Playback**: Plays specific audio files based on RFID tag IDs.
- **Text Writing**: Writes new text to RFID tags after user confirmation.
- **Interactive Menu**: Guides the user through different options (read, write, quit).

---

## Prerequisites

### Hardware Setup:
1. Connect the **RC522 RFID module** to the Raspberry Pi:
   - `SDA`: GPIO 8 (Pin 24)
   - `SCK`: GPIO 11 (Pin 23)
   - `MOSI`: GPIO 10 (Pin 19)
   - `MISO`: GPIO 9 (Pin 21)
   - `GND`: Ground (Pin 6)
   - `RST`: GPIO 25 (Pin 22)
   - `3.3V`: 3.3V Power (Pin 1)
2. Ensure all connections are secure.

### Software Setup:
1. Install required Python libraries:
   ```bash
   pip install RPi.GPIO mfrc522 pygame
   ```
2. Prepare audio files (e.g., `hello.mp3`, `nfl.mp3`) and place them in the same directory as the scripts.

---

## Usage Instructions

### Running the Scripts:
To run any script, use:
```bash
sudo python3 <script_name>.py
```

### `rfid_audio_player.py`
This script plays specific audio files based on the scanned RFID tag's unique ID.

1. Run the script:
   ```bash
   sudo python3 rfid_audio_player.py
   ```
2. Place an RFID tag near the reader.
3. The script will:
   - Print the tag ID and text.
   - Play the corresponding audio file if the tag ID is recognized.
   - Output "Unknown RFID ID!" for unrecognized tags.

4. The audio will play until complete. To stop the script, press `Ctrl+C`.

### `rfid_read_write.py`
This script provides an interactive interface to read from and write to RFID tags.

1. Run the script:
   ```bash
   sudo python3 rfid_read_write.py
   ```
2. Follow the menu prompts:
   - Press `r` to read the RFID tag.
   - Press `w` to write new text to a tag:
     - Scan the tag.
     - Confirm overwriting existing text.
     - Enter new text when prompted.
   - Press `q` to quit the script.

3. The script will guide you through the process and display the results.

---

## Notes
- **GPIO Cleanup**: Both scripts ensure proper cleanup of GPIO resources on exit.
- **Root Privileges**: Scripts must be run with `sudo` to access GPIO pins.
- **Audio Playback**: Ensure that the audio files match the tag IDs in `rfid_audio_player.py`.

---

## Example RFID IDs (for `rfid_audio_player.py`)
- **ID: `7894286177`** → Plays `hello.mp3`
- **ID: `291003226748`** → Plays `nfl.mp3`
- **Unknown IDs** → Print "Unknown RFID ID!"

Modify the script to add your own tag IDs and corresponding audio files.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance functionality or fix bugs.

---

## License
This project is licensed under the MIT License.