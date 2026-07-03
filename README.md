# ⚡ Smart Duplicate File Finder

A beautiful, high-performance desktop application built with **Python** and **CustomTkinter** designed to hunt down and safely delete identical duplicate files choking your hard drive. 

Unlike primitive scanners that only look at file names, this utility utilizes advanced **MD5 cryptographic digital fingerprint hashing** to analyze the deep internal contents of your files. If two files are identical, it catches them instantly—even if they have completely different names!

---

## 🛒 Download Standalone Application
If you don't want to run raw Python scripts or handle terminal dependencies, you can download the fully compiled, plug-and-play standalone Windows executable (`.exe`) instantly:

* **[Download on Gumroad](PASTE_YOUR_GUMROAD_LINK_HERE)**
* **[Download on Itch.io](PASTE_YOUR_ITCHIO_LINK_HERE)**

---

## 🚀 Key Features

* **Deep Hashing Engine:** Uses secure `hashlib` MD5 scanning to isolate true duplicate images, videos, documents, and archive folders.
* **Original File Safety:** Wipes out unnecessary file clones while keeping your original source files completely secure.
* **Real-Time Data Analytics:** Instantly calculates exactly how many duplicate files were caught and precisely how many Megabytes of storage space you will reclaim.
* **Fluid Dark Theme:** Designed with a beautiful, responsive dark-mode graphical user interface.
* **No Setup Required:** The compiled version runs instantly with a single double-click.

---

## 🛠️ Built With

* **Python 3** - Core backend calculation logic and file operations.
* **CustomTkinter** - Responsive modern graphical user interface widgets.
* **PyInstaller** - Standalone binary executable generation compilation.

---

## 💻 Manual Developer Installation
If you prefer to run the raw source code locally on your machine via your code terminal editor:

1. Clone this repository to your disk layout:
   ```bash
   git clone https://github.com
   ```
2. Install the necessary interface framework:
   ```bash
   pip install customtkinter
   ```
3. Run the visual application file:
   ```bash
   python gui_duplicate_finder.py
   ```

