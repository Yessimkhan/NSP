import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PRO.settings")
import django
django.setup()
import random
from Main.models import Employees
from faker import Faker
fake = Faker()

def saly(value):
    for i in range(value):
        full_name = fake.name()
        job_title = 'Narod'
        date_of_receipt = fake.date_between()
        salary = random.randint(100,200)
        head = random.randint(1101,11101)
        obj = Employees.objects.get_or_create(full_name = full_name,
                                              job_title = job_title,
                                              date_of_receipt = date_of_receipt,
                                              salary = salary,
                                              head = head)
def main():
    no = int(input("qansha: "))
    saly(no)

if __name__ == "__main__":
    main()


