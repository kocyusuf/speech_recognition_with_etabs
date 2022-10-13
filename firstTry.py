import speech_recognition as sr
import comtypes.client
from gtts import gTTS
import os
import time
from playsound import playsound


class SpeakWithEtabs():
    def __init__(self):

        self.ETABSObject = comtypes.client.GetActiveObject("CSI.ETABS.API.ETABSObject")
        self.SapModel = self.ETABSObject.SapModel
        self.speech_recording()


    def speech_recording(self):
        mic = sr.Microphone()
        r = sr.Recognizer()


        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Arka plan gürültüsü:" + str(r.energy_threshold))
            language = "tr"
            myText = "Lütfen konuşun."
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("komut.mp3")
            time.sleep(3)
            playsound("komut.mp3")
            os.remove("komut.mp3")
            try:
                ses = r.listen(source, timeout=2, phrase_time_limit=5)
                yazi = r.recognize_google(ses, language="tr-tr")
                print(yazi)
                if "malzeme tanımla" in yazi:
                    self.define_material()
                if "malzeme kaldır" in yazi:
                    self.delete_material()

            except sr.WaitTimeoutError:
                print("Dinleme zaman aşımına uğradı")

            except sr.UnknownValueError:
                print("Ne dediğini anlayamadım")

            except sr.RequestError:
                print("İnternete bağlanamıyorum")

    def define_material(self):
        mic = sr.Microphone()
        r = sr.Recognizer()
        print("define material !")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Arka plan gürültüsü:" + str(r.energy_threshold))
            language = "tr"
            myText = "Malzeme adını söyleyiniz"
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("defineMat.mp3")
            time.sleep(3)
            playsound("defineMat.mp3")
            os.remove("defineMat.mp3")

            try:
                ses = r.listen(source, timeout=2, phrase_time_limit=5)
                yazi = r.recognize_google(ses, language="tr-tr")
                print(yazi)
                if "25" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.AddMaterial("C25/30", 2, "Europe", "EN 1992-1-1 per EN 206-1", "C25/30")
                    self.SapModel.PropMaterial.SetMPIsotropic("C25/30", 30000, 0.20, 0.00001)
                elif "30" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.AddMaterial("C30/37", 2, "Europe", "EN 1992-1-1 per EN 206-1", "C30/37")
                    self.SapModel.PropMaterial.SetMPIsotropic("C30/37", 32000, 0.20, 0.00001)
                elif "35" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.AddMaterial("C35/45", 2, "Europe", "EN 1992-1-1 per EN 206-1", "C35/45")
                    self.SapModel.PropMaterial.SetMPIsotropic("C35/45", 33000, 0.20, 0.00001)
                elif "40" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.AddMaterial("C40/50", 2, "Europe", "EN 1992-1-1 per EN 206-1", "C40/50")
                    self.SapModel.PropMaterial.SetMPIsotropic("C40/50", 34000, 0.20, 0.00001)
                elif "45" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.AddMaterial("C45/55", 2, "Europe", "EN 1992-1-1 per EN 206-1", "C45/55")
                    self.SapModel.PropMaterial.SetMPIsotropic("C45/55", 36000, 0.20, 0.00001)
                elif "50" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.AddMaterial("C50/60", 2, "Europe", "EN 1992-1-1 per EN 206-1", "C50/60")
                    self.SapModel.PropMaterial.SetMPIsotropic("C50/60", 37000, 0.20, 0.00001)
                else:
                    print(f"Üzgünüm {yazi} malzemesini tanımlayamadım.")

            except sr.WaitTimeoutError:
                print("Dinleme zaman aşımına uğradı")

            except sr.UnknownValueError:
                print("Ne dediğini anlayamadım")

            except sr.RequestError:
                print("İnternete bağlanamıyorum")
        self.try_again()

    def delete_material(self):
        mic = sr.Microphone()
        r = sr.Recognizer()
        print("delete material !")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Arka plan gürültüsü:" + str(r.energy_threshold))
            language = "tr"
            myText = "Malzeme adını söyleyiniz."
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("deleteMat.mp3")
            time.sleep(3)
            playsound("deleteMat.mp3")
            os.remove("deleteMat.mp3")

            try:
                ses = r.listen(source, timeout=2, phrase_time_limit=5)
                yazi = r.recognize_google(ses, language="tr-tr")
                print(yazi)
                if "25" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.Delete("C25/30")

                elif "30" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.Delete("C30/37")

                elif "35" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.Delete("C35/45")

                elif "40" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.Delete("C40/35")

                elif "45" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.Delete("C45/55")

                elif "50" in yazi:
                    print("True")
                    self.SapModel.PropMaterial.Delete("C50/60")

                else:
                    print(f"Üzgünüm {yazi} malzemesini silemedim.")
            except sr.WaitTimeoutError:
                print("Dinleme zaman aşımına uğradı")

            except sr.UnknownValueError:
                print("Ne dediğini anlayamadım")

            except sr.RequestError:
                print("İnternete bağlanamıyorum")

        self.try_again()

    def try_again(self):
        mic = sr.Microphone()
        r = sr.Recognizer()
        print("try again !")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Arka plan gürültüsü:" + str(r.energy_threshold))
            language = "tr"
            myText = "Tekrar denemek ister misiniz?"
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("tryAgain.mp3")
            time.sleep(3)
            playsound("tryAgain.mp3")
            os.remove("tryAgain.mp3")

            try:
                ses = r.listen(source, timeout=2, phrase_time_limit=5)
                yazi = r.recognize_google(ses, language="tr-tr")
                print(yazi)
                if "elbette" in yazi or "evet" in yazi:
                    self.speech_recording()

                if "hayır" in yazi or "istemiyorum" in yazi:
                    language = "tr"
                    myText = "Güle güle."
                    output = gTTS(text=myText, lang=language, slow=False)
                    output.save("by.mp3")
                    time.sleep(3)
                    playsound("by.mp3")
                    os.remove("by.mp3")
            except sr.WaitTimeoutError:
                print("Dinleme zaman aşımına uğradı")

            except sr.UnknownValueError:
                print("Ne dediğini anlayamadım")

            except sr.RequestError:
                print("İnternete bağlanamıyorum")


SpeakWithEtabs()