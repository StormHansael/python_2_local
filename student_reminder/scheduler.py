# scheduler.py
import schedule
import time

def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger):
    """Schedule reminder delivery for each student at their preferred time."""
    for student in students_manager.get_students():
        reminder = reminder_generator(student['name'], student['course'])

        """Logs generation of new reminders"""
        logger(student, f"Generated reminder: {reminder}")

        """Logs shceduling of reminders based on student props"""
        logger(student, f"Scheduled daily reminder at {student['preferred_time']}")
        
        schedule.every().day.at(student['preferred_time']).do(
            lambda s=student, r=reminder: (reminder_sender(s['email'], r), logger(s, r))
        )

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
