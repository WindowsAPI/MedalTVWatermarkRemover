# MedalWatermarkRemover

Medal.tv Desktop App Watermark Remover for Windows 10/11.

# Features

- Automatically detects Medal.tv video windows.

- Extracts the raw video URL.

- Downloads the video without a watermark.

# Installation

1. Prerequisites

- Ensure you have Python 3.8+ installed. You can download it from python.org

2. Setup

- Clone the repository or download the source code.

- ```git clone https://github.com/WindowsAPI/MedalWatermarkRemover.git```
  
- cd MedalWatermarkRemover

3. Install the required dependencies.

- ```pip install -r requirements.txt```

4. Run the script.

- python nw.py

5. Usage

- Run nw.py and run the Start Download button.
  
- Open Medal.tv, go to the clip you want to download without watermark, and click the download with watermark button.

- The script will detect the Medal video and extract the watermark free clip.

- The video will be saved in the same directory as the script.

6. Known Syntax Issue: COM Error

- You may see the following error message in the terminal:

- ```QWindowsContext: OleInitialize() failed: "COM error 0xffffffff80010106 RPC_E_CHANGED_MODE (Unknown error 0x080010106)"```

- This does not affect functionality and can be ignored. It occurs because PyQt5 and pywinauto both attempt to initialize COM differently.

7. Troubleshooting

- If the program does not detect the Medal.tv window, ensure it is visible and active.

- If the download fails, check your internet connection and try again.

- If you encounter permission errors, try running the script as an administrator.
