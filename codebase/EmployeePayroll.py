class Employee:
    def __init__(self, emp_id, name, basic, overtime_hours):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.overtime_hours = overtime_hours
        self.overtime_pay = 0
        self.bonus = 0
        self.gross = 0
        self.pf = 0
        self.tax = 0
        self.net = 0

    def calculate_gross(self):
        # Overtime is Rs. 200 per hour
        self.overtime_pay = self.overtime_hours * 200
        self.gross = self.basic + self.overtime_pay + self.bonus
        return self.gross

    def calculate_net(self):
        self.calculate_gross()
        # PF = 12% of basic
        self.pf = 0.12 * self.basic
        # Tax = 10% of gross if gross is above 50000, else 0
        self.tax = 0.10 * self.gross if self.gross > 50000 else 0
        # Net = Gross - PF - Tax
        self.net = self.gross - self.pf - self.tax
        return self.net

    def get_payslip_text(self):
        lines = [
            "----------------------------------------",
            f"ID: {self.emp_id} | Name: {self.name} ({self.__class__.__name__})",
            f"Basic: {self.basic:g}",
            f"Overtime: {self.overtime_pay:g} | Gross: {self.gross:g}",
            f"PF: {self.pf:g} | Tax: {self.tax:g}",
            f"Net Salary: {self.net:g}",
            "----------------------------------------"
        ]
        return "\n".join(lines)


class Manager(Employee):
    def calculate_gross(self):
        # Manager adds a 10% bonus on basic
        self.bonus = 0.10 * self.basic
        return super().calculate_gross()

    def get_payslip_text(self):
        lines = [
            "----------------------------------------",
            f"ID: {self.emp_id} | Name: {self.name} ({self.__class__.__name__})",
            f"Basic: {self.basic:g}",
            f"Overtime: {self.overtime_pay:g} | Bonus: {self.bonus:g} | Gross: {self.gross:g}",
            f"PF: {self.pf:g} | Tax: {self.tax:g}",
            f"Net Salary: {self.net:g}",
            "----------------------------------------"
        ]
        return "\n".join(lines)


def print_and_save_payslip(emp, filename="Payroll.txt"):
    payslip = emp.get_payslip_text()
    print("\n" + payslip)
    with open(filename, "a", encoding="utf-8") as file:
        file.write(payslip + "\n")


def get_valid_basic():
    while True:
        val = input("Enter Basic Salary: ").strip()
        try:
            basic = float(val)
            if basic <= 0:
                print("Invalid basic salary. Enter a positive number.")
            else:
                return basic
        except ValueError:
            print("Invalid basic salary. Enter a positive number.")


def get_valid_overtime():
    while True:
        val = input("Enter Overtime hours: ").strip()
        try:
            hours = float(val)
            if hours < 0:
                print("Invalid overtime hours. Enter a non-negative number.")
            else:
                return hours
        except ValueError:
            print("Invalid overtime hours. Enter a non-negative number.")


def main():
    print("=== Employee Payroll System ===")
    while True:
        role = input("\nEnter role (Employee / Manager): ").strip().lower()
        if role not in ("employee", "manager"):
            print("Invalid role. Please enter 'Employee' or 'Manager'.")
            continue

        emp_id = input("Enter ID: ").strip()
        name = input("Enter Name: ").strip()
        basic = get_valid_basic()
        overtime_hours = get_valid_overtime()

        if role == "manager":
            staff = Manager(emp_id, name, basic, overtime_hours)
        else:
            staff = Employee(emp_id, name, basic, overtime_hours)

        staff.calculate_net()
        print_and_save_payslip(staff)

        again = input("\nDo you want to add another employee? (y/n): ").strip().lower()
        if again != 'y':
            print("All payslips have been saved to payroll.txt. Exiting...")
            break


if __name__ == "__main__":
    main()