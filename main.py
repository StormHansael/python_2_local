# main.py

# Imports from modules
from student_reminder.students_manager import StudentsManager
from student_reminder.reminder_generator import generate_reminder
from student_reminder.reminder_sender import send_reminder
from student_reminder.logger import log_reminder
from student_reminder.scheduler import schedule_reminders

# Create an instance of manager to automate remider procces
def main():
    manager = StudentsManager()
    schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)

if __name__ == "__main__":
    main()