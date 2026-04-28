# 12 Computer Concepts You Should Know Before Taking Intro to Python
April 2026

What your computer literacy course taught you that directly applies to programming.

Every semester I meet students who are eager to learn Python but struggle in the first two weeks, not because Python is hard, but because some foundational computer concepts were never fully absorbed. These aren't advanced topics. They are things covered in any computer literacy or information technology fundamentals course. But when they are shaky, everything in programming gets harder.

Here are the twelve concepts I expect students to know walking into Intro to Python. If any of these feel unfamiliar, spend thirty minutes reviewing them before the first day of class. It will pay off.

## 1. Files and Folders

A file is a named collection of data stored on a computer. A folder (also called a directory) is a container that organizes files. You need to understand how to create, rename, move, copy, and delete both. In Python, you will constantly be telling the computer where to find a file or where to save one. If you do not know how your own file system is organized, that becomes an immediate obstacle.

Get comfortable creating a dedicated folder for your coursework before the semester starts. Name it something logical. Know exactly where it lives.

## 2. File Paths

A file path is the address of a file on your computer. An absolute path starts from the root of the drive, such as `C:\Users\YourName\Documents\project\data.csv` on Windows or `/home/yourname/project/data.csv` on Mac or Linux. A relative path describes a location relative to where you currently are, such as `data/data.csv`.

Python programs reference files by their paths constantly. If you have never thought about the difference between absolute and relative paths, this concept alone is worth an hour of your time before class begins.

## 3. File Extensions and File Types

A file extension is the suffix at the end of a filename that indicates what kind of data it contains — `.py` for Python source code, `.txt` for plain text, `.csv` for comma-separated data, `.pdf` for documents. Extensions tell the operating system which program should open the file.

In Python, your code files will always be `.py`. You will also read and write `.txt` and `.csv` files regularly. Understanding that a `.docx` Word file and a `.txt` plain text file are fundamentally different kinds of files matters more than it sounds.

## 4. The Operating System

The operating system (OS) is the software that manages all of a computer's hardware and provides a foundation for all other software to run on. Windows, macOS, and Linux are the three you are most likely to encounter. The OS manages memory, runs applications, handles file storage, and controls input and output.

As a Python programmer, you need to know which OS you are working on because file paths, terminal commands, and some Python behaviors differ between them. You do not need to be an expert, but you should know what an OS is and what it does.

## 5. Hardware Basics: CPU, RAM, and Storage

The **CPU** (Central Processing Unit) is the brain of the computer — it executes instructions. **RAM** (Random Access Memory) is short-term memory that holds data the computer is actively using. **Storage** (a hard drive or SSD) is long-term memory where files are saved permanently.

When your Python program runs slowly, or crashes with a memory error, understanding these three components helps you reason about why. When you open your development environment, load a dataset, and run a script simultaneously, you are using all three at once.

## 6. Binary and How Computers Store Data

At the lowest level, computers store all data as binary, sequences of 0s and 1s called bits. Eight bits make a byte. Everything on your computer including text, images, numbers,and code are ultimately stored as binary.

You do not need to convert binary by hand in this course, but understanding that a computer represents all data as numbers, and that even text characters are stored as numeric codes (like ASCII or Unicode), explains a lot of behavior you will encounter in Python when working with strings and data types.

## 7. Input and Output

Input is any data that goes into a computer: keyboard, mouse, microphone, camera, file, network. Output is any data that comes out: monitor, printer, speakers, file, network.

In Python, `input()` reads from the keyboard and `print()` writes to the screen. Reading a file is input. Writing a file is output. This is not just vocabulary — thinking clearly about where data comes from and where it goes is a fundamental programming habit.

## 8. Application Software vs. System Software

System software (like the OS) manages the hardware and keeps the computer running. Application software is what users interact with to accomplish tasks, i.e., a browser, a word processor, a game, a Python script.

Python programs you write are application software. Understanding this distinction helps you understand what Python actually is: a tool for writing software that runs on top of an operating system, using the resources the OS manages.

## 9. Text Editors vs. Word Processors

A word processor like Microsoft Word saves files in a rich format that includes fonts, colors, margins, and layout. A text editor like Notepad, VS Code, or IDLE saves files as plain text, just characters, nothing else.

Python source code must be written in a plain text editor. If you ever save a `.py` file from Word, it will not work. This distinction confuses students every semester. Know the difference before you write your first line of code.

## 10. Keyboard Shortcuts

Programming involves a lot of text manipulation, and keyboard shortcuts make you dramatically faster. Every student entering this course should know:

- **Ctrl+C / Ctrl+V**  - copy and paste
- **Ctrl+Z**  - undo
- **Ctrl+S**  - save
- **Ctrl+F** - find
- **Ctrl+A**  - select all
- **Alt+Tab** - switch between open windows
#### In Browser
- **Ctrl + Shift + R** - (or Cmd + Shift + R on Mac) performs a hard refresh (also called a force reload).
Hard refresh (Ctrl+Shift+R) — forces the browser to ignore the cache and re-download every file from the server fresh. You'll always see the latest version of the page.
- **Ctrl + Shift + Delete** (or Cmd + Shift + Delete on Mac) - Clear cach + refresh

These seem basic, but students who rely entirely on the mouse spend two or three times as long on mechanical tasks, which steals attention from the actual programming.

## 11. Cloud Storage and Local Storage

Local storage means files saved directly on your computer's hard drive. Cloud storage means files saved to a remote server and accessible via the internet, i.e., Google Drive, OneDrive, Dropbox. Many students save exclusively to cloud folders without fully understanding where those files actually live on their local machine.

Python programs run on your local machine and reference local file paths. If your files live inside a OneDrive or Google Drive folder, the path to those files still exists locally, but it can be long and confusing. Know where your files are saved and understand the difference between the two.

## 12. Basic Troubleshooting and Problem-Solving

Every computer user should have a basic troubleshooting mindset: read the error message, search for it online, try the simplest fix first (restart, update, re-read what you typed). This is not a technical skill — it is a habit of mind.

In programming, error messages are not failures. They are information. Students who have been taught to read error messages carefully and search for solutions independently will learn Python twice as fast as those who stop and wait for help at the first red text. Your computer literacy course should have introduced this mindset. Programming will demand it every single day.

---

None of these twelve concepts require deep expertise. But they do require familiarity. If you walk into Intro to Python with all twelve solid, you will spend your mental energy on the actual craft of programming — not on basic confusion about where a file is saved or what a path means.

If you want to test yourself, open your file manager, navigate to a folder three levels deep, write down its full path, and then open that same folder in a plain text editor. If that takes you less than two minutes, you are ready.
