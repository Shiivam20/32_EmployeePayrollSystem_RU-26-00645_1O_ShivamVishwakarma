# Employee Payroll System

A console-based Object-Oriented Python application built to automate employee and manager salary calculations, deductions, input validation, and payslip archiving.

**Problem Statement:** PS No. 32 — Employee Payroll System  
**Institution:** Rungta International Skills University (School of Computer Science and Engineering)  
**Program:** B.Tech Computer Science and Engineering (First Semester)

---

## Overview

This program calculates net salaries from basic pay, overtime hours, and role-based bonuses while applying statutory deductions (Provident Fund and Income Tax). Each processed record is formatted into a clean payslip, displayed in the console, and appended to `payroll.txt`.

### Key Features
* **Object-Oriented Design:** Uses inheritance (`Manager` extending `Employee`) and method overriding to cleanly separate standard employee and managerial pay rules.
* **Automated Salary & Deduction Rules:**
  * **Overtime Pay:** ₹200 per hour
  * **Manager Bonus:** 10% of basic salary
  * **Provident Fund (PF):** 12% of basic salary
  * **Income Tax:** 10% of gross salary if gross exceeds ₹50,000; otherwise ₹0
  * **Net Salary:** `Gross Salary - PF - Tax`
* **Input Validation:** Prevents crashes and invalid calculations by enforcing positive basic salaries and non-negative numeric overtime hours.
* **Batch Processing & File Handling:** Processes multiple employees in a single session and appends all payslips persistently to `payroll.txt`.

---
