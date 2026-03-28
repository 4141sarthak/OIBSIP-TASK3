# 🔐 Secure Password Generator (GUI-Based)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

This project is a **secure and customizable password generator** built using Python and Tkinter. It provides a user-friendly graphical interface that allows users to generate strong passwords based on selected criteria such as length, character types, and complexity levels.

The application is designed with a focus on **security, usability, and flexibility**, making it ideal for both practical use and academic projects.

---

## ✨ Features

* Interactive Graphical User Interface (GUI)
* Custom password length selection
* Character type options:

  * Uppercase (A–Z)
  * Lowercase (a–z)
  * Numbers (0–9)
  * Symbols (!, @, #, etc.)
* Password complexity levels:

  * Low
  * Medium
  * High (ensures strong password rules)
* Exclude specific characters
* Clipboard copy functionality
* Input validation with error handling
* Randomized secure password generation

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Tkinter** (GUI framework)
* **random** (secure random generation)
* **string** (character sets)
* **pyperclip** (clipboard support)

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/OIBSIP-TASK3.git
```

2. Navigate to the project folder:

```
cd OIBSIP-TASK3
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

```
python main.py
```

---

## 🧑‍💻 Usage

1. Enter desired password length
2. Select character types
3. Choose complexity level
4. (Optional) Exclude specific characters
5. Click **Generate Password**
6. Copy using **Copy to Clipboard**

---

## 🔐 Security Features

* Enforces minimum password length
* Requires at least one character type
* High complexity ensures strong password composition
* Random shuffling prevents predictable patterns
* Custom exclusion improves control

---

## 📁 Project Structure

```
OIBSIP-TASK3/
│── main.py
│── requirements.txt
│── README.md
│── LICENSE
│── Project Report.pdf
│── Screenshots/
```

---

## ⚠️ Limitations

* No password storage system
* Clipboard data may be temporarily accessible
* No integration with breach-check APIs

---

## 🚀 Future Enhancements

* Password strength meter
* Encrypted password manager
* Modern UI using CustomTkinter
* Export passwords to file
* API integration for security checks

---

## 👨‍💻 Author

**Sarthak Jindal**

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Acknowledgment

This project was developed as part of an internship task to demonstrate practical implementation of Python GUI and cybersecurity concepts.
