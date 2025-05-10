import pandas as pd

file_for_analyze = r"C:\Users\malwi\Desktop\Codding_stuff_MW\DataAnalysis_POC\device_data_sample_GPTcreated.csv"

df = pd.read_csv(file_for_analyze)

users_with_unknown_error = set(df[df["ErrorMessage"] == "Unknown"]["UserID"])
users_with_browser_crash = set(df[df["CrashCause"] == "Browser"]["UserID"])
users_with_both = users_with_unknown_error & users_with_browser_crash

print("Liczba użytkowników z Unknown Error i Browser Crash:", len(users_with_both))
print(users_with_both)