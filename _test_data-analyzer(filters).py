import pandas as pd
# from tabulate import tabulate

# from _csv_generator import file_path_gen
file_path_gen = r"C:\Users\malwi\Desktop\Codding_stuff_MW\DataAnalysis_POC\DataAnalysis_POC\input_data11052025_10k.csv"

df = pd.read_csv(file_path_gen)

# General file check:
crash_counts = df.groupby(["CrashCause"]).size()
error_counts = df.groupby(["ErrorMessage"]).size()
error_info_counts = df.groupby(["ErrorMessage","ErrorInfo"]).size()

# print("General Crash amounts: \n", crash_counts)
# print("\n General Error amounts: \n",error_counts)
# print("\n General data for Error with Info amounts: \n",error_info_counts)

# Checking for specific combination:
users_with_unknown_error = set(df[df["ErrorMessage"] == "Unknown"]["UserID"])
users_with_browser_crash = set(df[df["CrashCause"] == "Browser"]["UserID"])
users_with_both = users_with_unknown_error & users_with_browser_crash

filteredID = df[df["UserID"].isin(users_with_both)]
crash_counts_filtered = filteredID.groupby(["CrashCause"]).size()
print("Crash amounts for filtered data: \n", crash_counts_filtered)

selected_message = "Unknown"
error_filter = df[
    (df["ErrorMessage"] == selected_message) & 
    (df["UserID"].isin(users_with_both))
    ]
error_info_counts_filtered = error_filter.groupby(["ErrorMessage","ErrorInfo"]).size()
print("\n Error with Info amounts for filtered data: \n",error_info_counts_filtered)