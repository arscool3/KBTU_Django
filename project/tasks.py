import dramatiq

@dramatiq.actor
def send_email(recipient, subject, message):
    # Здесь можно добавить логику отправки электронной почты
    print(f"Sending email to {recipient} with subject '{subject}' and message: '{message}'")

@dramatiq.actor
def generate_report(report_data):
    # Здесь можно добавить логику генерации отчета
    print(f"Generating report with data: {report_data}")