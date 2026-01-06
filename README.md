# Professional Scientific Calculator

A robust and visually stunning scientific calculator built with **Flask** (Python) and **Vanilla HTML/CSS/JS**. 

Unlike traditional web simple calculators, this project features a **Horizontal Wide-Screen Layout** optimized for desktop productivity, a premium **Glassmorphism** design with animated backgrounds, and a dedicated **History Side-Panel**. It is production-ready with secure input validation and Degree/Radian support.

![Calculator Preview](https://via.placeholder.com/800x400?text=Run+the+app+to+see+the+beautiful+UI)

## ✨ Features

- **Advanced UI/UX**: Premium Glassmorphism design with animated backgrounds and neon accents.
- **Scientific Functions**: Support for Trigonometry (`sin`, `cos`, `tan`), Logarithms (`log`, `ln`), Powers (`^`), Roots (`√`), and Constants (`π`).
- **Mode Switching**: Toggle between **Degree (DEG)** and **Radian (RAD)** modes for trigonometric calculations.
- **Calculation History**: interactive history list—click any past calculation to reuse it.
- **Secure Backend**: Input is sanitized and validated on the server side to prevent code injection.
- **Keyboard Support**: Type numbers naturally and press `Enter` to calculate.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation

1.  **Clone or Navigate** to the project directory:
    ```bash
    cd "d:/My Projects/scientific-calculator"
    ```

2.  **Install Dependencies** (Flask):
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Run the Flask server:
    ```bash
    python app.py
    ```

2.  **View the Output**:
    Open your web browser and go to:
    👉 **http://127.0.0.1:5000/**

## 🛠️ Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3 (Animations, Flexbox/Grid), JavaScript (Fetch API)
- **Design Font**: 'Outfit' and 'JetBrains Mono' via Google Fonts.

## 📝 Usage Tips

- **Trigonometry**: By default, the calculator is in **DEG** mode (e.g., `sin(90) = 1`). Click the "DEG" button to switch to **RAD** (Radians).
- **History**: Click the trash icon to clear your calculation history.
- **Power**: Use `^` for exponents (e.g., `2^3`).
