import csv
import random
import string
import os
from datetime import datetime, timedelta

# Helper functions
def generate_user_id():
    return "-".join("".join(random.choices(string.ascii_lowercase + string.digits, k=4)) for _ in range(3))

def generate_sub_id():
    return str(random.randint(1000000000, 9999999999))

def generate_version():
    return f"{random.randint(100, 999)}.{random.randint(0, 9)}"

def generate_recordings():
    return ",".join(str(random.randint(0, 9)) for _ in range(4))

# Parameters
num_records = 10000
num_users = 100
start_time = datetime.strptime("11:00:00", "%H:%M:%S")
end_time = datetime.strptime("15:00:00", "%H:%M:%S")
time_range = (end_time - start_time).seconds

# Crash causes, error messages and info
crash_causes = ["Browser", "UI", "Watchdog", "Connection Timeout", "App 1", "App 2"]
error_messages = ["TMW update", "Connection Error", "Unknown", "UI update", "Authentication Error", "App 1 Error", "App 2 Error"]
error_info = ["TMW", "Client", "App", "Live", "Unknown"]

# Generate unique UserIDs and assign SubIDs
user_sub_map = {}
sub_id_to_users = {}
while len(user_sub_map) < num_users:
    user_id = generate_user_id()
    if user_id not in user_sub_map:
        sub_id = generate_sub_id()
        user_sub_map[user_id] = sub_id
        sub_id_to_users.setdefault(sub_id, []).append(user_id)

# Assign one recorder per SubID
recording_users = {sub_id: random.choice(users) for sub_id, users in sub_id_to_users.items()}

# Generate records
records = []
sequence_tracker = {}

for i in range(num_records):
    timestamp = (start_time + timedelta(seconds=int(i * time_range / num_records))).time().strftime("%H:%M:%S")
    user_id = random.choice(list(user_sub_map.keys()))
    sub_id = user_sub_map[user_id]
    version = generate_version()

    # Decide on record type
    record_type = random.choices(["crash", "error", "recording"], weights=[0.3, 0.4, 0.3])[0]

    if record_type == "crash":
        crash = random.choice(crash_causes)
        record = [timestamp, user_id, sub_id, version, crash, "-", "-", "-", "-"]
    elif record_type == "error":
        errmsg = random.choice(error_messages)
        errinfo = random.choice(error_info)
        record = [timestamp, user_id, sub_id, version, "-", errmsg, errinfo, "-", "-"]
    else:
        if user_id == recording_users[sub_id]:
            seq_key = (sub_id, user_id)
            sequence = sequence_tracker.get(seq_key, 0)
            sequence += 1
            sequence_tracker[seq_key] = sequence
            recordings = generate_recordings()
        else:
            recordings = "-"
            sequence = "-"
        record = [timestamp, user_id, sub_id, version, "-", "-", "-", recordings, sequence]

    records.append(record)

# Sort by timestamp
records.sort(key=lambda x: x[0])

# Write to CSV
header = ["Timestamp", "UserID", "SubID", "Version", "CrashCause", "ErrorMessage", "ErrorInfo", "Recordings", "Sequence"]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# output_file_name = f"new_data_{timestamp}.csv"
file_path_gen = r"C:\Users\malwi\Desktop\Codding_stuff_MW\DataAnalysis_POC\DataAnalysis_POC\input_data11052025_10k.csv"

with open(file_path_gen, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(records)

file_path_gen


# output_file = os.path.join(file_path_gen, output_file_name)