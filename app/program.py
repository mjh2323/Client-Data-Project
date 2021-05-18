#program.py

# program.py

import os
import base64
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId)
from fpdf import FPDF


#opening message 

print()
print('------------------------------------------------------------------')
print("Welcome - please select a few options before receiving your data.")
print('------------------------------------------------------------------')
print()


#send email function 

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>

subject = "Your Requested Client Data"

html_content = "Please find the data attached. Have a nice day!"


def send_email(subject= subject, html_content = html_content, pdf= "CLIENT_DATA.pdf"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)
    #attaches the PDF we generated earlier
    file_path = 'CLIENT_DATA.pdf'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName('CLIENT_DATA.pdf')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
    
    #send email
    try:
        response = client.send(message)
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None


#Collect user inputs 

while True:
    print("You can view all data, or select by region or company.")
    Choice_1 = input("If you would like to see all data, please enter ALL. Otherwise, enter OTHER. ")
    if Choice_1 == "ALL" or "all":
        print("An email with all client data attached will be in your inbox shortly.")
        break
    elif Choice_1 == "OTHER" or "other":
        Choice_2 = input("Would you like to specify by region or company? ")
        
        if Choice_2 == "Region" or "region" or "REGION":
            print("The regions are as follows: (New York, NY; San Francisco, CA; Hong Kong; Chicago, IL; London, UK; Washington, DC). ")
            region_choice = input("Please select a region from the list above. ")
            print("You have selected {region_choice}. An email will be in your inbox shortly.")
            break
        elif Choice_2 == "Company" or "company" or "COMPANY":
            print("The companies present include: (Company ABC; Biz Co; Money Corp; 123 Co).")
            company_choice = input("Please select a company from the list above. ")
            print("You have selected {company_choice}. An email will be in your inbox shortly.")
            break
        else:
            print("Please choose from the list above.")
    else: 
        print("Please choose from the list above.")


if Choice_1 == "ALL" or "all":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "CLIENT_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "New York, NY":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "NewYork_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "London, UK":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "London_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "San Francisco, CA":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "SanFrancisco_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "Washington, DC":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "DC_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "Hong Kong":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "HK_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "Chicago, IL":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "Chicago_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")
    

if company_choice == "Company ABC":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "ABC_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif company_choice == "Biz Co":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "BizCo_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif company_choice == "123 Co":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "123Co_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif company_choice == "Money Corp":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Your data is attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    email_pdf = "MoneyCorp_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")
    

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Requested Client Data"

html_content = "Please find the data attached. Have a nice day!"
print("HTML:", html_content)

  



