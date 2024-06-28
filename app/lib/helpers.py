from fastapi import status

successful_message = {"STATUS": "OK"}, status.HTTP_200_OK
unsuccessful_message = {"STATUS": "ERROR"}, status.HTTP_400_BAD_REQUEST


