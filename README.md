# RFID Python Scripts

This repository contains Python scripts for interfacing with an **RFID-RC522 reader/writer** using a Raspberry Pi. The scripts allow you to perform actions such as reading RFID tags, writing text to them, and triggering specific actions (e.g., playing audio files) based on RFID tag detection.

---

## Files Included

### 1. `rfid_audio_player.py`
This script reads RFID tags and plays corresponding audio files based on the tag's unique ID. It's useful for applications like interactive displays, audio guides, or educational projects.

#### Features:
- Detects RFID tags and prints their unique IDs and associated text.
- Plays audio files (`hello.mp3`, `nfl.mp3`, etc.) when specific RFID tags are detected.
- Uses **pygame** to handle audio playback.

#### How It Works:
1. The script initializes the RFID reader and pygame mixer.
2. Continuously waits for RFID tags to be scanned.
3. Plays a predefined audio file if the tag's ID matches a specific value.
4. Cleans up GPIO resources when interrupted.

#### Requirements:
- `RPi.GPIO`
- `mfrc522`
- `pygame`
- Audio files in the same directory as the script.

#### Usage:
Run the script:
```bash
python3 rfid_audio_player.py