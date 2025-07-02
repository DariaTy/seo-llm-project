import csv
from typing import List, Dict

def export_to_csv(data: List[Dict[str, str]], filename: str = "metadata.csv"):
    """Export metadata to a CSV file."""
    if not data:
        print("No data to export.")
        return

    keys = data[0].keys()  # Assume all dictionaries have the same keys
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Metadata exported to {filename}")
