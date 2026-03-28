# Secure Password Generator (GUI-Based)

## Overview

This project is a graphical password generator application built using Python and Tkinter. It allows users to generate strong, secure, and customizable passwords based on various criteria such as length, character types, and complexity level.

The application focuses on usability, security, and flexibility, making it suitable for everyday use as well as educational purposes.

---

## Features

* Graphical User Interface (GUI) using Tkinter
* User-defined password length
* Selection of character types:

  * Uppercase letters (A–Z)
  * Lowercase letters (a–z)
  * Digits (0–9)
  * Symbols (!, @, #, etc.)
* Password complexity levels:

  * Low
  * Medium
  * High (ensures inclusion of all selected character types)
* Option to exclude specific characters
* Clipboard integration for easy copying
* Input validation and error handling
* Randomized secure password generation

---

## Technologies Used

* Python 3.x
* Tkinter (for GUI)
* random (for password generation)
* string (character sets)
* pyperclip (clipboard functionality)

---

## Installation

1. Download or clone the project files
2. Install required dependency:

pip install pyperclip

---

## How to Run

python main.py

---

## Usage Instructions

1. Enter the desired password length
2. Select the character types to include
3. Choose the complexity level
4. Optionally exclude specific characters
5. Click on "Generate Password"
6. Copy the password using the "Copy to Clipboard" button

---

## Security Features

* Ensures minimum password length
* Enforces at least one character type selection
* High complexity mode guarantees stronger passwords
* Random shuffling to avoid predictable patterns
* Custom exclusion of vulnerable or unwanted characters

---

## Limitations

* No password storage functionality
* Clipboard data may be accessible by other applications
* Does not check passwords against known data breaches

---

## Future Enhancements

* Password strength meter
* Encrypted password storage
* Integration with security APIs
* Improved UI using advanced frameworks
* Export passwords to file

---

## Author

Sarthak Jindal

---

## License

This project is for educational purposes only.
