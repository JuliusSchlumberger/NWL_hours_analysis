# NWL Hours Analysis

This repository contains a standardized workflow to analyze the claimed **klus-hours** for the NWL.  
The analysis is used as input for the annual board report and ensures that:

- The same calculation steps are applied every year  
- Historical data (since 2011) remains consistent  
- Figures are automatically generated and reproducible  

This README explains the full process in clear, practical steps — especially for users with limited coding experience.

---

# 📌 What This Repository Does

The repository allows you to:

1. Update the historical dataset with the most recent year of claimed hours  
2. Automatically generate:
   - A **category breakdown** of hours for the selected year  
   - A **historical development plot** (2011 – present)  

The output consists of two figures that can be directly used in the annual report.

---

# 🧭 Step 0 – Getting Started with GitHub & Python

If you are not familiar with GitHub or Python, don’t worry. You only need some basic setup.

---

## 🔹 What is GitHub?

GitHub is a platform where code and projects are stored. This repository lives here:

https://github.com/JuliusSchlumberger/NWL_hours_analysis

Helpful introduction: https://docs.github.com/en/get-started/quickstart/hello-world

---

## 🔹 Installing Python

You need Python installed on your computer.

### Recommended: Install Anaconda (Beginner-Friendly)

Anaconda includes Python and helpful tools.

1. Download Anaconda:  
   https://www.anaconda.com/products/distribution
2. Install it with default settings.
3. After installation, you can use:
   - **Anaconda Navigator** (graphical interface), or  
   - **Anaconda Prompt** (command line)

Alternative: Install Python directly  
https://www.python.org/downloads/

---

# 📥 Step 1 – Cloning the Repository

Cloning means copying the repository to your computer.

---

## Option A – Using GitHub Desktop (Easiest)

1. Install GitHub Desktop:  
   https://desktop.github.com/
2. Open it
3. Click **File → Clone Repository**
4. Paste the repository URL:
   ```
   https://github.com/JuliusSchlumberger/NWL_hours_analysis
   ```
5. Choose a local folder
6. Click **Clone**

---

## Option B – Using the Command Line

If Git is installed:

```bash
git clone https://github.com/JuliusSchlumberger/NWL_hours_analysis.git
cd NWL_hours_analysis
```

Git installation guide:  
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

---

# 🐍 Step 2 – Create the Project Environment

This repository includes an `environment.yml` file.  
This file defines all required Python packages and ensures that the analysis runs consistently across different machines.

⚠ **Important:**  
The `environment.yml` file must remain inside the cloned repository folder.  
You must run the environment creation command **from inside that folder**, otherwise Conda will not find the file.

First, navigate to the repository directory.

If you just cloned it and are still in the same terminal session, you can use:

```bash
cd NWL_hours_analysis
```

If you opened a new terminal, you need to provide the full path to the folder where the repository was cloned.

Replace `<PATH_TO_FOLDER>` with the location on your computer.

**Windows example:**
```bash
cd <PATH_TO_FOLDER>\NWL_hours_analysis
```

Example:
```bash
cd C:\Users\YourName\Documents\NWL_hours_analysis
```

**Mac/Linux example:**
```bash
cd <PATH_TO_FOLDER>/NWL_hours_analysis
```

Example:
```bash
cd /Users/YourName/Documents/NWL_hours_analysis
```

You can verify you are in the correct folder by checking that you see:

```
environment.yml
```

Now create the environment:

```bash
conda env create -f environment.yml
```

This will automatically:
- Create a virtual environment
- Install Python
- Install all required packages (pandas, matplotlib, openpyxl, etc.)

You only need to create the environment once. 

To be able to conduct the analysis, activate the environment:

```bash
conda activate simple_env
```

---


# 📊 Step 3 – Prepare the Data

To create the yearly analysis, follow these steps carefully.

---

## 1️⃣ Request the Backlog

Ask the webadmin (Bart) to provide the backlog of claimed klus-hours for the past year.

Make sure the file contains:
- All recorded entries for the past year
- Time values (usually in minutes)
- Categories (if applicable)

---

## 2️⃣ Convert Minutes to Hours

The system requires hours, not minutes.

Convert:

```
hours = minutes / 60
```

You can do this in Excel:

If minutes are in column A:

```
=A2/60
```

Drag the formula down for all rows.

---

## 3️⃣ Update the Historical Excel File

Open:

```
overzicht_sinds_2011.xlsx
```

Add the entries for the new year:

- Insert the new year in the correct rows
- Ensure:
  - Data are not duplicated (especially regarding the beginning of the new year
  - Units are proper for the klus-hours in **hours** and for the dates
  - No formatting is broken
  - No accidental column shifts

⚠ Important:
Do not change historical data unless correcting an error.

Save the file.

---

# ▶️ Step 4 – Run the Analysis

Now the automated part begins.

Open:

```
run_analysis.py
```

Inside the file, locate the parameter:

```python
year_of_analysis = XXXX
```

Change it to the new year, for example:

```python
year_of_analysis = 2024
```

Save the file.

---

## Run the Script

From inside the repository folder:

```bash
python <PATH_TO_FOLDER>\run_analysis.py
```

If you are using Anaconda:

```bash
conda activate nwl_analysis
python <PATH_TO_FOLDER>\run_analysis.py
```

---

# 📈 Output

Running the script generates two figures:

---

## 1️⃣ Yearly Category Breakdown

Shows how the total hours are divided across categories for the selected year.

## 2️⃣ Historical Development (Since 2011)

Shows how total claimed hours developed over time.

---

# 🛠 Troubleshooting

## Module Not Found Error

Install required packages:

---

## Excel File Not Found

Make sure:
- `overzicht_sinds_2011.xlsx` is in the same folder as `run_analysis.py`
- The filename has not been changed

---

## Figures Do Not Update

Check:
- The correct `year_of_analysis`
- The Excel file contains the new year
- Data is in hours (not minutes)

---

# 📂 Repository Structure

```
NWL_hours_analysis/
│
├── overzicht_sinds_2011.xlsx   # Historical dataset
├── run_analysis.py             # Main analysis script
└── README.md                   # This file
```

---

# 🔁 Annual Workflow Summary

Each year:

1. Request backlog from webadmin  
2. Convert minutes → hours  
3. Update `overzicht_sinds_2011.xlsx`  
4. Set `year_of_analysis` in `run_analysis.py`  
5. Run the script  
6. Insert figures into annual report  

Total time required: ~15–30 minutes once familiar.

---

# 📬 Questions?

If anything is unclear, contact the owner of the repository by opening an issue in the repository.

---

# ✅ Final Notes

This repository ensures that:

- The NWL annual hour reporting is consistent  
- Historical records remain structured  
- The process is easy to repeat every year  

Even with limited coding skills, following this README step-by-step will allow you to generate the required analysis reliably.
