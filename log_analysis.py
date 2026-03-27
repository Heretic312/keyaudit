import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Paths
LOG_FILE = "logs/keylog.txt"
IMAGES_FOLDER = "images"

# Create 'images' folder if it doesn't exist
os.makedirs(IMAGES_FOLDER, exist_ok=True)

# Read log file
data = []
with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        parts = line.split(" | ")
        if len(parts) != 3:
            print(f"Skipping malformed line: {line}")
            continue
        timestamp, window, key = parts
        data.append({"timestamp": timestamp, "window": window, "key": key})

if not data:
    print("No valid log data found!")
    exit()

# Convert to DataFrame
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Count keystrokes per window
window_counts = df['window'].value_counts()

# Plot
plt.figure(figsize=(10,6))
window_counts.plot(kind='bar', color='skyblue')
plt.title("Keystrokes per Active Window")
plt.ylabel("Number of Keystrokes")
plt.xlabel("Application")
plt.xticks(rotation=45)
plt.tight_layout()

# Save figure with timestamp
timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
image_filename = f"keystrokes_{timestamp_str}.png"
plt.savefig(os.path.join(IMAGES_FOLDER, image_filename), dpi=300)

print(f"Bar chart saved to {IMAGES_FOLDER}/{image_filename}")

# Show plot (optional)
plt.show()