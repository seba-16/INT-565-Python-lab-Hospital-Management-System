""" Name - Sebabrata Pramanik
Roll No. - RK24MLA28
Reg No. -  12412041
Section -  K24ML
"""
#"Scenario: Hospital Management System
# Design a Patient class that stores name, age, illness, and admission_date. 
# Write methods to admit a patient, discharge a patient, 
# and calculate the hospital stay charges based on the number of days admitted.
# Objective: Integrating date and time with object methods."

#codes

from datetime import datetime

class Patient:
    def __init__(self):
        self.name = None
        self.age = None
        self.illness = None
        self.admission_date = None
        self.discharge_date = None

    def admit_patient(self):
        #patient name
        while True:
            self.name = input("Enter patient name: ").strip()
            if self.name == "":
                print("Sorry: Patient name cannot be empty. Please try again.")
            elif not all(char.isalpha() or char.isspace() for char in self.name):
                print("Please Enter a valid name.") 
  
            else:
                break

        # patient age 
        while True:
            try:
                self.age = int(input("Enter patient age: "))
                if self.age <= 0:
                    print("Sorry: Age must be a positive number. Please try again.")
                else:
                    break
            except ValueError:
                print("Sorry: Age must be a valid number. Please try again.")

        #patient illness 
        while True:
            try:
              self.illness = input("Enter patient's illness: ").strip()
              if self.illness == "":
                  print(" Illness field cannot be empty. Please try again.")
              elif any(char.isdigit() for char in self.illness):
                  print("Illness cannot contain numbers. Please try again.")
              else:
                  break
            except ValueError:
                print("Sorry: Give correct input. Please try again.")

        # admission date or default to today's date
        while True:
            admission_date_str = input("Enter admission date (DD-MM-YYYY) or press Enter to use today's date: ").strip()
            if admission_date_str == "":
                self.admission_date = datetime.now()
                print(f"No date provided. Using today's date: {self.admission_date.strftime('%d-%m-%Y')}")
                break
            else:
                try:
                    self.admission_date = datetime.strptime(admission_date_str, '%d-%m-%Y')
                    print(f"Patient {self.name} admitted on {self.admission_date.strftime('%d-%m-%Y')}")
                    break
                except ValueError:
                    print("Error: Invalid date format. Please use DD-MM-YYYY.")

    def discharge_patient(self):
        if self.admission_date is None:
            print("Patient has not been admitted yet.")
        else:
            while True:
                discharge_date_str = input("Enter discharge date (DD-MM-YYYY) or press Enter to use today's date: ").strip()

                if discharge_date_str == "":
                    self.discharge_date = datetime.now()
                    print(f"No date provided. Using today's date: {self.discharge_date.strftime('%d-%m-%Y')}")
                    break
                else:
                    try:
                        self.discharge_date = datetime.strptime(discharge_date_str, '%d-%m-%Y')
                        if self.discharge_date < self.admission_date:
                            print("Sorry: Discharge date cannot be earlier than admission date. Please try again.")
                        else:
                            print(f"Patient {self.name} discharged on {self.discharge_date.strftime('%d-%m-%Y')}")
                            break
                    except ValueError:
                        print("Invalid date format. Please use DD-MM-YYYY.")

    def calculate_stay_charges(self):
        if self.admission_date is None:
            print("Patient has not been admitted yet.")
            return 0
        if self.discharge_date is None:
            print("Patient has not been discharged yet.")
            return 0

        while True:
            try:
                daily_rate = float(input("Enter daily rate (in rupees): "))
                if daily_rate <= 0:
                    print("Daily rate must be a greater than zero. Please try again.")
                else:
                    break
            except ValueError:
                print("Daily rate must be a valid number. Please try again.")

        # Calculating the number of days stayed
        stay_duration = (self.discharge_date - self.admission_date).days
        if stay_duration == 0:
            stay_duration = 1  # Charge for at least one day

        total_charges = stay_duration * daily_rate
        print(f"Total hospital charges for {self.name}: ₹{total_charges:.2f}")
        return total_charges

patient_ = Patient()
patient_.admit_patient()
patient_.discharge_patient()
patient_.calculate_stay_charges()

