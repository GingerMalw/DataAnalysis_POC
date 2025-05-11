import pandas as pd

# from _csv_generator import file_path_gen
file_path_gen = r"C:\Users\malwi\Desktop\Codding_stuff_MW\DataAnalysis_POC\DataAnalysis_POC\input_data11052025.csv"

df = pd.read_csv(file_path_gen)

users_with_unknown_error = set(df[df["ErrorMessage"] == "Unknown"]["UserID"])
users_with_browser_crash = set(df[df["CrashCause"] == "Browser"]["UserID"])
users_with_both = users_with_unknown_error & users_with_browser_crash

amount_Unknown = df[(df["UserID"].isin(users_with_both)) & (df["ErrorMessage"] == "Unknown")]
amount_Browser = df[(df["UserID"].isin(users_with_both)) & (df["CrashCause"] == "Browser")]               

print("Liczba użytkowników z Unknown Error i Browser Crash:", len(users_with_both))
# print("List ID:", users_with_both)
print("Liczba Unknown Error:", len(amount_Unknown), "Liczba Browser Crash:", len(amount_Browser))

with open("DataAnalysis_POC\AI_output1.txt", "r") as plik:
    AI_output = plik.read()
AI_ID = {line.strip() for line in AI_output.strip().splitlines() if line.strip()}

print("Liczba użytkowników z Unknown Error i Browser Crash (AI):", len(AI_ID))
# print("List ID (AI):", users_with_both)

def validation_diff(set1, set2):
    return users_with_both.symmetric_difference(AI_ID)

ID_diff = validation_diff(users_with_both, AI_ID)
print("Ilość:" , len(ID_diff), " Elementy różniące się:", ID_diff)