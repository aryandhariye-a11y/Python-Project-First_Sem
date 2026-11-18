# Project Summary: Hospital Management System

## Overview
The **Hospital Management System** is a menu-driven console application developed in **Python 3**. Designed as part of the **Bachelor of Technology in Computer Science and Engineering** curriculum at **Rungta International Skills University (School of Computer Science and Engineering)**, the system manages hospital patient records in memory using core programming constructs.

---

## Core Objectives & Concepts
* **Programming Language:** Python 3 (contained within a single `.py` file).
* **Key Concepts Applied:** Nested dictionaries, modular functions, record management, and CRUD (Create, Read, Update, Delete) operations.
* **Data Architecture:** Stores each patient record as a dictionary nested inside a primary dictionary keyed by unique auto-incrementing Patient IDs starting at `P101`. Data persists in memory during runtime without external file dependencies.

---

## Functional Scope
1. **Add Patient (`add_patient`)**: Captures `Name`, `Age`, `Disease`, and `Doctor`. Automatically assigns an ID (`P101`, `P102`, etc.).
2. **View All Patients (`view_patients`)**: Displays all stored patient records or notifies the user if no records exist.
3. **Search Patient (`search_patient`)**: Retrieves and displays a specific patient's details using their Patient ID.
4. **Update Patient (`update_patient`)**: Modifies existing details (such as updating a diagnosis) for a valid Patient ID.
5. **Delete Patient (`delete_patient`)**: Removes a record by ID and reports the updated total patient count.

---

## Validation & Error Handling
* **Input Validation:** Ensures patient names are non-empty and verifies that ages are numeric values strictly between `0` and `120` before saving.
* **Boundary & Edge Cases:** Handles minimum valid ages (e.g., `0`), rejects non-numeric age entries, and outputs clear status messages when searching, updating, or deleting non-existent IDs.
