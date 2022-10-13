import speech_recognition as sr

mic = sr.Microphone() # Mikrofon tanımladık.
r = sr.Recognizer() # Kayıt edici tanımladık.

"""kod 1 saniye boyunca mikrofonumuzu dinleyerek arkaplan gürültüsünü sayısal olarak r.energy_threshold değişkenine atıyor."""
with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Arka plan gürültüsü:" + str(r.energy_threshold))

    try:
        ses = r.listen(source, timeout=2, phrase_time_limit=5)
        yazi = r.recognize_google(ses, language="tr-tr")
        print(yazi)

    except sr.WaitTimeoutError:
        print("Dinleme zaman aşımına uğradı")

    except sr.UnknownValueError:
        print("Ne dediğini anlayamadım")

    except sr.RequestError:
        print("İnternete bağlanamıyorum")

"""Bu kod mikrofonumuzu dinleyerek bir ses değeri döndürür ve ardından r.recognize_google komutu ile aldığımız 
ses değişkeni yorumlar ve çıktıyı ekrana yazdırır. Şimdi aklınızda bir soru gelmiş olmalı. 
timeout ve phrase_time_limit parametresi ne işe yarıyor? Hemen açıklayalım;

Bu 2 parametrede girilmesi zorunlu parametreler değildir.

"timeout" : Bu parametre aldığı saniye cinsinden sayısal değer kadar bekler ve eğer verilen süre dolarsa 
WaitTimeoutError hatasını döndürür.
"phrase_time_limit" : Aldığı saniye cinsinden sayısal değer ile konuşma başladıktan sonrasında 
ne kadar süre boyunca konuşulacağına karar vermemizi sağlayan parametredir. """

