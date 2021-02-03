# rest_django

Elements Candidate Assignment - Web Backend
 The Setting
A customer would like to have a native mobile application that displays a simple data set. The data consists of:
Image;
Title;
Description (optional).
The data set is hosted in Google Docs as a spreadsheet: https://docs.google.com/spreadsheet/ccc? key=0Aqg9JQbnOwBwdEZFN2JKeldGZGFzUWVrNDBsczZxLUE&usp=drive_web#gid=0
The spreadsheet is accessible as a CSV file through the following link: https://docs.google.com /spreadsheet/ccc? key=0Aqg9JQbnOwBwdEZFN2JKeldGZGFzUWVrNDBsczZxLUE&single=true&gid=0&output=csv
The customer is responsible for the contents of this spreadsheet and therefor the data is not always reliable. For example, the size of the images is not guaranteed to be optimized for use in a mobile application.
The Task
Because of the CSV potentially being moved to another location on another server or maybe being replaced by another source entirely, an API should be implemented in between. Build a RESTful JSON API in Python/Django that will load the contents of the CSV, transforms this into a structure that will be used by the mobile application and serves the result.
Things you have to take into consideration:
Application structure;
Performance;
Image cache;
Exception handling;
Working in a DTAP (Development/Testing/Acceptance/Production) environment.
Optional Components:
Response cache;
Scalability, when the application should be served from multiple servers.
Remarks
PLEASE don't make the solution public anywhere (private repositories on Github or similar are OK)
You can build everything yourself or use existing library components. This is mainly a test to see how you would implement a development challenge.
Try to make error handling as graceful as possible. The user should not be bugged with error messages. Good luck!
