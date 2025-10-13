# Copilot Instructions for waterlooccc

## Project Overview
This repository contains a large collection of Waterloo CCC (Canadian Computing Competition) problems and solutions, organized by year, division (Junior/Senior), and language (Python, Java, text input/output). The codebase is primarily for educational and practice purposes, with a focus on algorithmic problem solving and dynamic programming.

## Directory Structure
- Each year (e.g., `2011/`, `2012/`, ...) contains subfolders for `Junior` and `Senior` problems.
- Problems are named by convention (e.g., `J1.py`, `S1.py`, `J5.java`).
- Some years include `.t` files for text-based input/output, and `.pdf` files for official problem statements.
- The `template/` folder contains reusable Python scripts and reference materials.
- The root contains general-purpose scripts (e.g., `dynamicProgramming.py`, `2016s5-circleoflife.py`).

## Key Patterns and Conventions
- **File Naming:** Problem files follow the format `[J|S][number][optional suffix].[py|java|t]`.
- **Input Handling:** Many Python scripts read from standard input or from provided `.t` files. See `template/input.py` for reusable input patterns.
- **Dynamic Programming:** Solutions often use memoization and tabulation. See `dynamicProgramming.py` for common approaches.
- **No Central Build/Test System:** There is no global build or test runner. Run individual scripts directly (e.g., `python 2012/Junior/J1.py`).
- **Java Problems:** Java files are not organized as packages; compile/run with `javac`/`java` from their respective folders.
- **Reference Materials:** The `template/` folder and various PDFs provide context and problem statements.

## Developer Workflows
- **Run Python Solution:**
  ```zsh
  python <path-to-problem>.py < <input-file>
  ```
- **Run Java Solution:**
  ```zsh
  cd <year>/<division>
  javac S1.java && java S1
  ```
- **Debugging:** Add print statements or use the `sandbox.py` in `template/` for quick experiments.
- **Adding New Problems:** Place new files in the appropriate year/division folder, following the naming convention.

## Integration Points
- No external dependencies or package managers are used.
- All scripts are standalone; no cross-file imports except for templates.
- For input/output conventions, refer to `template/input.py` and `.t` files.

## Examples
- See `2011/Junior/J1.py` for a simple input/output pattern.
- See `dynamicProgramming.py` for advanced DP techniques.
- See `template/input.py` for reusable input logic.

## Tips for AI Agents
- Always follow the year/division/problem naming and placement conventions.
- Prefer using existing templates for input handling and common algorithms.
- When in doubt, check similar problems from previous years for solution patterns.
- Do not introduce external dependencies unless explicitly requested.

---
_Last updated: October 12, 2025_
