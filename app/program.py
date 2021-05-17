html_content = "Please find the data attached. Have a nice day!"
print("HTML:", html_content)


def send_email(subject= subject, html_content = html_content, pdf= "all_data.pdf"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)
    #attaches the PDF we generated earlier
    file_path = 'all_data.pdf'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName('all_data.pdf')
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

if __name__ == "__main__":
    email_subject = "Your Requested Client Data"
    email_html = f""" 
    <h3> Welcome to Juicy Lifts! </h3>
    <p> Attached to this email you will find a PDF with a workout that addresses your specific fitness needs. Time to hit the gym! </p>
    """
    email_pdf = "all_data.pdf"
    #send my message to users
    send_email(email_subject, email_html, email_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")