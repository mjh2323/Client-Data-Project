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

email_pdf = {"CLIENT_DATA.pdfa", "NewYork_Data.pdf","London_Data.pdf", "SanFrancisco_Data.pdf", "Chicago_Data.pdf", "HK_Data.pdf", "Chicago_Data.pdf", "ABC_DATA.pdf", "BizCo_DATA.pdf", "123Co_DATA.pdf", "MoneyCorp_DATA.pdf",}

PDF_NAME = None

def send_email(subject= subject, html_content = html_content, pdf = email_pdf):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)
    #attaches the PDF we generated earlier
    file_path = email_pdf
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName(PDF_NAME)
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

company_choice = None
region_choice = None

print("You can view all data, or select by region or company.")
Choice_1 = input("If you would like to see all data, please enter ALL. Otherwise, enter OTHER. ")
if Choice_1 == "ALL":
    print("An email with all client data attached will be in your inbox shortly.")
elif Choice_1 == "OTHER":
    print("You have selected Other.")
    Choice_2 = input("Would you like to specify by region or company? ")
    if Choice_2 == "Region":
        print("The regions are as follows: (New York, NY; San Francisco, CA; Hong Kong; Chicago, IL; London, UK; Washington, DC). ")
        region_choice = input("Please select a region from the list above. ")
        print("An email will be in your inbox shortly.")
        
    elif Choice_2 == "Company":
        print("The companies present include: (Company ABC; Biz Co; Money Corp; 123 Co).")
        company_choice = input("Please select a company from the list above. ")
        print("An email will be in your inbox shortly.")
      
    else:
        print("Please choose from the list above.")
else: 
    print("Please choose from the list above.")


if Choice_1 == "ALL":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "CLIENT_DATA.pdf"
    email_pdf = "CLIENT_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "New York, NY":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "NewYork_Data.pdf"
    email_pdf = "NewYork_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "London, UK":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "London_Data.pdf"
    email_pdf = "London_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "San Francisco, CA":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "SanFrancisco_Data.pdf"
    email_pdf = "SanFrancisco_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "Washington, DC":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "DC_Data.pdf"
    email_pdf = "DC_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "Hong Kong":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "HK_Data.pdf"
    email_pdf = "HK_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif region_choice == "Chicago, IL":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "Chicago_Data.pdf"
    email_pdf = "Chicago_Data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")
    

if company_choice == "Company ABC":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "ABC_DATA.pdf"
    email_pdf = "ABC_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif company_choice == "Biz Co":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "BizCo_DATA.pdf"
    email_pdf = "BizCo_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif company_choice == "123 Co":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "123Co_DATA.pdf"
    email_pdf = "123Co_DATA.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

elif company_choice == "Money Corp":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> You Data is Attached! </h3>
    <p> Attached to this email you will find a PDF with the data you have requested. </p>
    <p> Have a great day! </p>
    """
    PDF_NAME = "MoneyCorp_DATA.pdf"
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

  




