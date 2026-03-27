# KeyAudit - Linux Python Keylogger Project

## Overview
This is a Linux keylogger built in Python for "educational purposes" (Not sure why I put quotation marks on that part). It captures keystrokes along with timestamps and active window titles, storing logs in a readable format for analysis. The project includes tools to visualize and analyze keystroke data. This project is not prod ready and honestly not very portable due to the dependencies. I just wanted something custom for my in house needs.


---

## Features
- Captures all keystrokes, including special keys like Enter, Tab, Shift, etc.
- Logs the active application/window when a key is pressed.
- Records timestamps for all keystrokes.
- Stores logs in a dedicated `logs/` folder.
- Analysis script (`log_analysis.py`) visualizes key activity per application.

---

## Dependencies
- Python 3.x
- `pynput` – for key capturing
- `pandas` – for data processing
- `matplotlib` – for visualization
- `xdotool` – for active window detection on Linux

Install dependencies:

```bash
sudo apt install xdotool python3-pynput python3-pandas python3-matplotlib
or
pip install -r requirements.txt
```
## Usage

## Run Keylogger
```bash
python3 keyaudit.py
```
- Press ESC to stop the keylogger.
- Logs are saved in logs/keylog.txt in the format:

```bash
2026-03-27 14:22:01 | Terminal | H
2026-03-27 14:22:01 | Terminal | e
```
## Analyze Logs
```bash
python3 log_analysis.py
```
- Generates a bar chart showing the number of keystrokes per active application.
