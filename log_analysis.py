import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "logs/keylog.txt"

import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "logs/keylog.txt"

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
            continue  # skip malformed lines
        timestamp, window, key = parts
        data.append({"timestamp": timestamp, "window": window, "key": key})

if not data:
    print("No valid log data found!")
    exit()

df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Count keys per window
window_counts = df['window'].value_counts()

# Plot keys pressed per application
plt.figure(figsize=(10,6))
window_counts.plot(kind='bar', color='skyblue')
plt.title("Keystrokes per Active Window")
plt.ylabel("Number of Keystrokes")
plt.xlabel("Application")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()