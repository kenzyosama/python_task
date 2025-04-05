import random
import webbrowser

def open_random_website():
    websites = ["https://www.google.com", "https://www.youtube.com"]
    webbrowser.open(random.choice(websites))

class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = max(0, min(100, healthRate))  

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10  

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)  

    def send_mail(self, recipient, subject, body):
        print(f"Email sent to {recipient} with subject '{subject}' and body '{body}'")

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = max(0, min(100, fuelRate))  
        self.velocity = max(0, min(200, velocity))  

    def run(self, distance, velocity):
        self.velocity = velocity
        while distance > 0 and self.fuelRate > 0:
            self.fuelRate -= 10  
            distance -= 10
        self.stop(distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped with {remaining_distance} km remaining!")
        else:
            print("Arrived at destination!")

class Office:
    employeesNum = 0  

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.emp_id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        self.employees = [emp for emp in self.employees if emp.emp_id != empId]
        Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        employee = self.get_employee(empId)
        if employee:
            employee.salary -= deduction

    def reward(self, empId, reward):
        employee = self.get_employee(empId)
        if employee:
            employee.salary += reward

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if employee:
            is_late = self.calculate_lateness(9, moveHour, employee.distanceToWork, employee.car.velocity)
            if is_late:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num