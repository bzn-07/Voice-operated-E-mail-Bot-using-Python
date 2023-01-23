import smtplib
import speech_recognition as sr
import pyttsx3
import pyaudio
from email.message import EmailMessage

print("_______________________________________________________")
print("                                                                                                            ")
mail = input("Enter your Mail ID :  ")
print("                                                                                                            ")
password = input("Enter your Password :  ")
print("                                                                                                            ")
print("_______________________________________________________")

dictionary = {}
h = ''


def add_value():
    print(
        "                                                                                                            ")
    a = input("Enter the Nickname :  ")
    print(
        "                                                                                                            ")
    b = input("Enter the Mail i'd :  ")
    print(
        "                                                                                                            ")

    def add_values_in_dict(sample_dict, key, list_of_values):
        if key not in sample_dict:
            sample_dict[key] = list_of_values

            dictionary = sample_dict

        s = input("Do you want to add more ?? : [yes/no] :  ")
        print(
            "                                                                                                            ")
        print("_______________________________________________________")
        print(
            "                                                                                                            ")
        if s == 'yes':
            add_value()

    add_values_in_dict(dictionary, a, b)


add_value()

print("                                                                                                            ")

print("                                                                                                            ")

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone(device_index=0) as source:
            print("_______________________________________________________")
            print(
                "                                                                                                            ")
            print("Listening...... ")
            print(
                "                                                                                                            ")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(reciever, subject, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(mail, password)
    email = EmailMessage()
    email['From'] = mail
    email['To'] = reciever
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)


def get_email_info():
    talk("to whom you want to send email")
    print("_______________________________________________________")
    print(
        "                                                                                                            ")
    name = get_info()
    reciever = dictionary[name]
    print(reciever)
    print("_______________________________________________________")
    print(
        "                                                                                                            ")
    talk("What is the subject of your email?")
    print("_______________________________________________________")
    print(
        "                                                                                                            ")
    subject = get_info()
    talk("tell me the content of your email")
    print("_______________________________________________________")
    print(
        "                                                                                                            ")
    print("_______________________________________________________")
    print(
                "                                                                                                            ")
    print("Listening...... ")
    print(
                "                                                                                                            ")
            
    print("Just to see if the project is working")
    print(
        "                                                                                                            ")
    print("_______________________________________________________")
    print(
        "                                                                                                            ")
    print("Hey your email has sent successfully")
    print("_______________________________________________________")
    print(
        "                                                                                                            ")
    print("_______________________________________________________")
    print(
                "                                                                                                            ")
    print("do you want to send more email?")
    print("_______________________________________________________")
    print(
                "                                                                                                            ")
    print("Listening...... ")
    print(
                "                                                                                                            ")
    print("no")
    
            
    message = get_info()
    print(
        "                                                                                                            ")
    send_email(reciever, subject, message)
    talk("Hey your email has sent successfully")
    print(
        "                                                                                                            ")
    
    talk("do you want to send more email?")
    print(
        "                                                                                                            ")
    print("_______________________________________________________")
    send_more = get_info()
    print(
        "                                                                                                            ")
    if "yes" in send_more:
        get_email_info
        print(
            "                                                                                                            ")


get_email_info()
