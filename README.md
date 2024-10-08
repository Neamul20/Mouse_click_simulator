﻿# Mouse_click_simulator

# MouseClicker: Automated Mouse Click Simulation Tool

Mouse_click_simulator is a Python script designed to automate mouse clicks at a user-specified location on the screen. This tool is ideal for tasks that require repetitive clicking, such as gaming, testing applications, or any other scenario where manual clicking can be tedious. 

## Features

- **Capture Click Position**: Waits for a user to click on the desired screen location, which will be used as the target for automated clicks.
- **Customizable Click Parameters**: Users can specify the number of clicks (`-c`) and the delay between clicks (`-i`) through command-line arguments.
- **Multi-Threaded Execution**: Clicking and key-listening processes run on separate threads, ensuring that the script remains responsive during execution.
- **Stop by ESC Key**: Allows users to stop the clicking process anytime by pressing the ESC key.

## Usage

```bash
python mouse_clicker.py -c 100 -i 0.5
```

- `-c` (optional): Number of clicks to perform (default is 200).
- `-i` (optional): Delay between clicks in seconds (default is 0.0).

## How It Works

1. **Capture Click Position**: The script waits for the user to left-click on the screen to capture the position where the clicks will occur.
2. **Perform Clicks**: The script simulates the specified number of clicks at the captured position with the defined delay.
3. **Stop by ESC**: Pressing the ESC key will immediately stop the clicking process.

This script is particularly useful for automating repetitive tasks that require high-speed or precise clicking.
