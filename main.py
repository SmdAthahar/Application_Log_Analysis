import pandas as pd

# STEP 1: Read the application log file
with open("application.log", "r", encoding="utf-8") as file:
    log_entries = file.readlines()

# STEP 2: Count total log entries
total_entries = len(log_entries)

# STEP 3: Initialize counters
error_count = 0
warning_count = 0
info_count = 0

# STEP 4: Create empty lists
error_entries = []
warning_entries = []
info_entries = []

# STEP 5: Identify and separate log entries
for entry in log_entries:
    if entry.startswith("ERROR"):
        error_count += 1
        error_entries.append(entry)
    elif entry.startswith("WARNING"):
        warning_count += 1
        warning_entries.append(entry)
    elif entry.startswith("INFO"):
        info_count += 1
        info_entries.append(entry)

# STEP 6: Display application log summary
print("\n========== APPLICATION LOG SUMMARY ==========")
print("Total log entries:", total_entries)
print("INFO occurrences:", info_count)
print("WARNING occurrences:", warning_count)
print("ERROR occurrences:", error_count)

# STEP 7: Create errors.txt
with open("errors.txt", "w", encoding="utf-8") as file:
    file.writelines(error_entries)
print("\nerrors.txt created successfully!")

# STEP 8: Create warnings.txt
with open("warnings.txt", "w", encoding="utf-8") as file:
    file.writelines(warning_entries)
print("warnings.txt created successfully!")

# STEP 9: Create info.txt
with open("info.txt", "w", encoding="utf-8") as file:
    file.writelines(info_entries)
print("info.txt created successfully!")

# STEP 10: Load log entries into a Pandas DataFrame
log_df = pd.DataFrame({
    "log_entry": [entry.strip() for entry in log_entries]
})

# STEP 11: Extract log levels
log_df["log_level"] = log_df["log_entry"].str.split(" - ").str[0]

# STEP 12: Perform frequency analysis
frequency = log_df["log_level"].value_counts()

print("\n========== LOG FREQUENCY ANALYSIS ==========")
print(frequency)

# STEP 13: Convert frequency results into a DataFrame
frequency_df = frequency.reset_index()
frequency_df.columns = ["log_level", "count"]

# STEP 14: Export frequency analysis to CSV
frequency_df.to_csv("log_frequency.csv", index=False)

print("\nlog_frequency.csv created successfully!")
print("\n========== PROJECT COMPLETED SUCCESSFULLY ==========")
