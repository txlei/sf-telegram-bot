import boto3
import config 
from prettytable import PrettyTable

def create_html_table():
  table = PrettyTable()
  table.field_names = ["Name", "Service Feedbac"] 
  table.add_row(["Jill","Smith", 50])

def verify_email_identity():
    ses_client = boto3.client("ses", region_name=config.AWS_REGION)
    response = ses_client.verify_email_identity(
        EmailAddress=config.EMAIL_FROM
    )
    print(response)

def send_html_email(subject):
    ses_client = boto3.client("ses", region_name=config.AWS_REGION)
    CHARSET = "UTF-8"

    HTML_EMAIL_CONTENT = """
        <html>
            <head></head>
            <h1 style='text-align:center'>This is the heading</h1>
            <p>Hello, world</p>
            </body>
        </html>
    """

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                # config.EMAIL_TO
                config.EMAIL_FROM
            ],
            # "CcAddresses": config.EMAIL_CC
            "CcAddresses": config.EMAIL_FROM
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": CHARSET,
                    "Data": HTML_EMAIL_CONTENT,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": subject,
            },
        },
        Source=config.EMAIL_FROM,
    )