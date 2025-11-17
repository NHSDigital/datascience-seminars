# Create Table of Contents in Readme

> [!WARNING]  
> I’m testing the Microsoft copilot AI to document functions – thus treat the docstring and README with caution

## Overview
This project automates the process of generating and updating a **Markdown table of contents** in a `README.md` file based on folder names in a specified directory. It is particularly useful for organizing seminar materials or similar structured content.

---

## ✅ Features
- **Dynamic Folder Listing**: Scans a base directory and lists all subfolders.
- **Table Generation**: Creates a Markdown table with:
  - **Date** (formatted as `YYYY-MM-DD`)
  - **Title**
  - **Clickable Links** to folders
- **README Update**: Inserts the generated table into the `README.md` at a specified anchor point.

---

## 📂 Project Structure
```
.
├── config.py      # Configuration settings
├── main.py        # Entry point for generating and updating README
├── utils.py       # Helper functions for folder listing, table creation, and README update
└── README.md      
```

## ▶️ How It Works
1. **Run the script**:
   ```bash
   python main.py
   ```
2. The script:
   - Lists all folders in `base_path`.
   - Extracts date and title from folder names (expected format: `YYYYMMDD_Title`).
   - Generates a Markdown table sorted by date.
   - Updates `README.md` by inserting the table after the specified anchor.

---

## 📌 Folder Naming Convention
- Expected format: `YYYYMMDD_Title`
  - Example: `20250115_DataScienceBasics`
- If the format is not followed, the date column will be empty.

---

## 🛠 Dependencies
- **Python 3.8+**
- **pandas**
- **os**


---

## 🔍 Example Output in README
```
[place_table_here]: #

| Date       | Link                                      |
|------------|-------------------------------------------|
| 2025-01-15 | [DataScienceBasics](/All_materials/20250115_DataScienceBasics) |
```

