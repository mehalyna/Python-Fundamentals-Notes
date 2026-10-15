# Python Fundamentals — Course Notebooks

This repository contains Jupyter notebooks used as supporting materials for the
Python Fundamentals course. Use them alongside the course sessions to review
examples, run code, and practice the concepts covered in class.

## How to use the notebooks

1. Follow the order and instructions provided by your instructor. Course
   materials may be added or updated as the course progresses.
2. Open a notebook in JupyterLab, Jupyter Notebook, or Visual Studio Code with
   the Python and Jupyter extensions installed.
3. Run cells from top to bottom. Read the explanations, try the examples, and
   change the code to explore what happens.
4. Complete exercises in your own copy of the notebook. Keep your work locally
   or in your own fork so that updates to the course materials do not overwrite
   it.

GitHub can display notebooks for reading, but you need a Jupyter environment to
run their code.

## Run notebooks locally

Install Python, then clone this repository and move into its folder:

```bash
git clone https://github.com/mehalyna/Python-Fundamentals-Notes.git
cd Python-Fundamentals-Notes
```

Create and activate a virtual environment:

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install JupyterLab and start it from the repository folder:

```bash
python -m pip install jupyterlab
python -m jupyter lab
```

Your browser will open JupyterLab, where you can navigate to and open a course
notebook. The `.venv` environment and generated Jupyter checkpoint files are
excluded from Git.

## Working with notebooks

- Run cells in order, especially when a later example depends on variables
  defined earlier.
- Experiment freely, but keep an original copy if you want to compare your
  changes with the course examples.
- Save your work regularly. Notebooks you change in your local checkout remain
  on your computer; share or submit them using the method specified by your
  instructor.
- If a notebook or instruction is missing or unclear, check with your
  instructor for the latest course guidance.
