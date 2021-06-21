# CogniTensor_security

Model Features:
- Face-Recognition system.
- An Automatic Entry-Log maintenance system for maintaining the entry log with name, date, and time of access.
- Mail-notification system for Burglary or unauthorized access attempt.
- Incorporated some functionality of pyaudio in the model to give the ability to speak out commands.
- Accepts password through voice commands.



Modules: 
Main File: Test.py
•	Voice.py
•	EntryReg.py
•	mailgen.py

	Voice.py: 
This function of this module is to provide speech recognition capabilities to my model. This module was built so that my model have the capability to speak and take voice inputs from the user.

	EntryReg.py:
The function of this module is to maintain an entry log-file. This csv file maintains the name of user who gained access, date of access and the time of access automatically.

	mailgen.py: 
The function of this module is to establish a SMTP connection in order to facilitate mail facilities from my IDE. 



Description:
This is a prototype security model build with python using OpenCV. This model is capable of face-recognition, speech-recognition, automatically maintaining an entry log-file (csv) with the name of user who gained access, date of access and the time of access, accepting password through voice commands, Mail-notification system for Burglary or unauthorized access attempt. 
In order to validate a user, we need to feed the images of the user in the “valid” folder saved as the name of the user.

When the main file i.e. Test.py is run, all the encodings are done and the model gives a voice command to look into the camera. When the user looks into the camera, the matching is done with all the encodings and then validates the user.
Now, if the user is a valid user, the model will greet the user (good morning, good afternoon or good evening according to the time) followed by the user’s name else if the user is not a valid user, an email will be sent to already mentioned recipients with a notification of burglary or unauthorized access attempt.
 
If the user is valid and successfully clears the face-recognition, the user’s name along with the date and time of access is stored in a csv file named “EntryLog”.

Once, the user passes the faces recognition, the models asks for the password to enter through voice command. This password can be changed easily by changing just a variable named “pas” in the Voice.py module.
 
As the password is set as “train” for now, the model will only validate if the user gives this password through the voice command to the model. If the user fails to provide the right password, an email will be sent to already mention recipients with a notification of burglary or unauthorized access attempt. 
