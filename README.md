# Screen Text
A Python script that captures a screenshot, extracts text using OCR, and copies it to the clipboard with a hotkey trigger.

## Installation

1. **Install Python**:
   If you haven't already installed Python, download and install it from the official website:
   - [Download Python](https://www.python.org/downloads/)

   Make sure to check the box "Add Python to PATH" during installation.

2. **Clone the repository**:
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/ian2102/screen-text.git
   ```

3. **Install required dependencies**:
   Navigate to the project directory and install the required Python libraries using `pip`:
   ```bash
   cd screen-text
   pip install pytesseract pillow pyperclip keyboard
   ```

4. **Install Tesseract-OCR**:
   The script uses Tesseract for OCR. Download and install it from the following link:
   - [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

   After installation, make sure to update the path to the `tesseract.exe` in the script (`screen_text.py`) as per your installation directory.

## Running the Script

1. Open a terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd path/to/screen-text
   ```

3. Run the script:
   ```bash
   python screen_text.py
   ```

4. Press **Windows + Shift + C** to take a screenshot and extract text. The extracted text will be copied to your clipboard.
