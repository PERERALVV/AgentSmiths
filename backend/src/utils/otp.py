import smtplib
from email.message import EmailMessage
import random
from database.database import user_collection
from database.database import forgot_password_collection

def generate_otp():
    return random.randint(100000, 999999)  # Generate a random 6-digit OTP

def email_alert(subject, to):
    otp = generate_otp()  # Generate the OTP
    body_with_otp = f"Your OTP is: {otp}\n"  # Include OTP in the email body
    
    # Check if the email exists in fogotPassword table
    existing_record = forgot_password_collection.find_one({"email": to})
    print(existing_record)
    if existing_record:
        # Update the OTP for the existing email
        forgot_password_collection.update_one({"email": to}, {"$set": {"otp": otp}})
    else:
        # Insert a new record with the OTP
        forgot_password_collection.insert_one({"email": to, "otp": otp})
    
    msg = EmailMessage()
    msg.set_content(body_with_otp)
    msg['Subject'] = subject
    msg['To'] = to

    user = "ayeshaasarak@gmail.com"
    msg['From'] = user
  

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Enable TLS encryption
        server.login(user, password)  # Log in to the server

        # Send email
        server.send_message(msg)
        print("Email sent to:", to)

    except Exception as e:
        print(f"Email could not be sent. Error: {e}")

    finally:
        server.quit()  # Always quit the server connection after sending

