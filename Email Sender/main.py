import smtplib

# Your email credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"

# Email list
recipients = [
    "example1@gmail.com",
    "example2@gmail.com"
]

subject = "Test Email"
message = "Hello, this is a test email sent using Python!"

def send_email():
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        for recipient in recipients:
            full_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(EMAIL, recipient, full_message)
            print(f"✅ Sent to {recipient}")

        server.quit()
        print("🎉 All emails sent!")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    send_email()