# Leap Year Checker

A simple Python script that determines whether a given year is a leap year or not.

## Author

Udorilwela Ratshikhopha

---

## Description

This program prompts the user to enter a year and then checks whether it qualifies as a leap year based on the standard Gregorian calendar rules:

- A year divisible by **400** is a leap year.
- A year divisible by **4** but **not by 100** is a leap year.
- All other years are **not** leap years.

---

## Requirements

- Python 3.x

---

## How to Run

```bash
python udorilwelasub3.py
```

You will be prompted to enter a year:

```
Enter a year below:
2024
2024 is a leap year
```

---

## Example Output

| Input | Output |
|-------|--------|
| `2000` | `2000 is a leap year` |
| `1900` | `1900 is not a leap year` |
| `2024` | `2024 is a leap year` |
| `2023` | `2023 is not a leap year` |

---

## Leap Year Rules (Gregorian Calendar)

1. If a year is divisible by **400** → **Leap year**
2. If a year is divisible by **100** but not 400 → **Not a leap year**
3. If a year is divisible by **4** but not 100 → **Leap year**
4. Otherwise → **Not a leap year**
