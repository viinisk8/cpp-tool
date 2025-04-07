# 🚀 C++ Project CLI Generator

A command-line interface (CLI) tool built with Python to streamline and accelerate the creation of C++ projects.

## ✨ Features

- 📁 Automatically generates project folder structure (`Config`, `Source`, `Build`, `Libs`)
- 📄 Creates `.cpp` and `.h` files directly via terminal
- 📑 Manages configuration using JSON files
- 🧭 Folder navigation fully in-terminal (supports ↑ ↓ W A E Q keys)
- 🛠️ Automatically compiles the project using Visual Studio (cl.exe)

## 🎥 Demo

![Demo](path/to/your_gif.gif)

## 🧪 Available Commands

- `start` – Sets up the initial project structure and configuration  
- `add` – Adds new `.cpp` and `.h` files to the project  
- `run` – Compiles all files using Visual Studio's compiler  
- `finish` – Exits the program

## ▶️ How to Use

```bash
python cpp.py

## 📁 Project Structure

📦 YourProject
├── 📁 Build
├── 📁 Config
│   ├── 📄 Config.json
│   ├── 📄 Files.json
│   └── 📄 Libs.json
├── 📁 Libs
├── 📁 Source
└── 📄 YourProject.cpp

## ⚙️ Requirements
- Python 3.x
- Visual Studio with cl.exe and vcvars64.bat available
- Python keyboard library (pip install keyboard)
