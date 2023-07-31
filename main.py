import base64
from copyleaks.copyleaks import Copyleaks
from copyleaks.exceptions.command_error import CommandError
from copyleaks.models.submit.document import FileDocument

# Replace with your Copyleaks API credentials
EMAIL_ADDRESS = 'bhargav.thota2003@gmail.com'
API_KEY = '2d00ed27-53ce-48e9-91bc-060a272af021'

# Authenticate with Copyleaks API
try:
    auth_token = Copyleaks.login(EMAIL_ADDRESS, API_KEY)
except CommandError as ce:
    response = ce.get_response()
    print(f"An error occurred (HTTP status code {response.status_code}):")
    print(response.content)
    exit(1)

print("Logged in successfully!\nToken:")
print(auth_token)

def submit_document_for_plagiarism_check(auth_token,file_path):

    scan_id = 12345  # Set a unique scan ID

    try:
        with open(file_path, 'rb') as file:
            file_content_base64 = base64.b64encode(file.read()).decode('utf-8')
            file_submission = FileDocument(file_content_base64, file.name)

        Copyleaks.submit_file(auth_token, scan_id, file_submission)
        print("File submitted for plagiarism check.")
        print("You will be notified once the scan is completed.")
    except CommandError as ce:
        response = ce.get_response()
        print(f"An error occurred (HTTP status code {response.status_code}):")
        print(response.content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = input("Enter the file path: ")
submit_document_for_plagiarism_check(auth_token, file_path)
