# Student Grade Manager

A simple Python-based Student Grade Manager that allows users to add student records, calculate grades automatically, and view class performance statistics through a menu-driven interface.

## Features

- **Add Students:** Enter student names and marks.
- **Automatic Grading:** Calculate grades based on marks obtained.
- **Multiple Students:** Add as many students as you want.
- **Duplicate Names:** Supports students with the same name.
- **Input Validation:** Handles invalid inputs such as text, negative marks, and marks above 100.
- **Formatted Results:** Display student names, marks, and grades in a neatly aligned table.
- **Class Statistics:** Calculate class average, highest mark, and lowest mark.
- **Interactive Menu:** Add students, view results, or quit the program.

## Grading System

| Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | E |

## Technologies Used

- Python 3
- VS Code
- Git & GitHub

## Project Structure

```text
Student Grade Manager/
│
├── grade_manager.py   # Main Python application
├── .gitignore         # Git ignored files
└── README.md           # Project documentation
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Student-Grade-Manager.git
```

### 2. Navigate to the project folder

```bash
cd Student-Grade-Manager
```

### 3. Run the program

```bash
python3 grade_manager.py
```

No external libraries are required.

## Usage

After running the program, select an option from the menu:

```text
===== STUDENT GRADE MANAGER =====
1. Add Student
2. Show Results
3. Quit

Choose an option:
```

### Example Output

```text
========================================
NAME                 MARK       GRADE
----------------------------------------
David                85.00      B
Priya                92.00      A
John                 76.00      C
========================================

Class Average: 84.33
Highest Mark: 92.00
Lowest Mark:  76.00
Total Students: 3
```

## Data Storage

Student records are stored in a Python list of dictionaries during program execution.

**Note:** Data is stored in memory and resets when the program exits. Persistent storage can be implemented in future versions.


## Author

**Richerd S.**

## License

This project is open-source and available for learning and educational purposes.
