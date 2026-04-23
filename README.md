# Inventory Management System v2

## Overview
A modular inventory management system built in Python, featuring both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** using Tkinter.

This project simulates real-world inventory operations such as product tracking, stock updates, and expiration monitoring, with a clean separation between business logic and user interfaces.

---

## Key Features

- Add and manage products
- Register stock (product output)
- View current inventory
- Detect products nearing expiration
- Modular architecture (core, CLI, GUI)
- Dual interface:
  - CLI for quick operations
  - GUI for user-friendly interaction
- Persistent storage using CSV

---

## Project Structure
- core/ # Business logic (data handling, operations, reports)
- cli/ # Command-line interface
- gui/ # Tkinter graphical interface

---

## Technologies Used

- **Python 3**
- **Tkinter** (GUI)
- **CSV**
- Modular architecture

---

## How to Run

### Option 1: Run CLI
```bash
python -m cli.main

```
---

### Option 2: Run GUI
```bash
python gui/app.py
```

---

## Use Case

This system simulates inventory management for a logistics or retail environment, allowing users to:

Track stock levels
Manage product lifecycle
Monitor expiration dates
Generate basic operational insights

---

## Purpose

This project was developed to:

- Practice modular software design
- Implement real-world data handling workflows
- Understand Python package structure and imports
- Build multi-interface applications (CLI + GUI)

---

## Future Improvements
- Database integration
- REST API backend
- User authentication system
- Dashboard with analytics
