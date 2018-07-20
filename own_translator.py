#!usr/bin/python3

from os import path
from textblob import TextBlob
import speech_recognition as sr

print("Welcome to Mudit Translator")

print("""
     Hindi :  'hi'
     english : 'en'
     spanish : 'es'
     """)

to_language=(input("enter language code you want result in...   "))

while True:
   print("""
     Press 1: Real-time translation of audio
     Press 2: Translate a audio file and save as text file
     """)

   ch=(input("what are you thinking"))
   if int(ch) == 1:
      r=sr.Recognizer()
      m=sr.Microphone()
      with m as source:
         print("Silence, One Moment Please")
         r.adjust_for_ambient_noise(source)   #adjusting microphone
         print("speak")  #start speaking
         while True:
             audio=r.listen(source)   #microphone is listening
             try:
               blob=TextBlob(r.recognize_google(audio)) #recognizing audio
               print("your language " + blob.detect_language())
               print(blob.translate(to="{}".format(to_language)))  #translating audio
             except KeyboardInterrupt:
               pass
             except sr.UnknownValueError:
               print("could not understand audio")
             except sr.RequestError as e:
               print("cpuld not request results;{0}".format(e))                                                

   if int(ch) == 2:
      try:
        file_name=(input("Enter your audio file name"))
        #file must be in current working directory
        AUDIO_FILE_EN = path.join(path.dirname(path.realpath(__file__)), "{}.wav".format(file_name))   #opening audio file
        with sr.AudioFile(AUDIO_FILE_EN) as source:
             audio_en = r.record(source)  #reading entire audio file
             blob=TextBlob(r.recognize_google(audio_en))
             fh = open("translate_result.txt", "w") #saving results to txt file
             fh.write(blob.translate(to="{}".format(to_language)))
             fh.close()

      except:
        pass

                
