import pandas as pd

from csv_generator import file_path_gen

df = pd.read_csv(file_path_gen)

users_with_unknown_error = set(df[df["ErrorMessage"] == "Unknown"]["UserID"])
users_with_browser_crash = set(df[df["CrashCause"] == "Browser"]["UserID"])
users_with_both = users_with_unknown_error & users_with_browser_crash

print("Liczba użytkowników z Unknown Error i Browser Crash:", len(users_with_both))
print(users_with_both)