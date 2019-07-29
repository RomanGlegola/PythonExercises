import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

adres_email = 'haaritsubaki@gmail.com'
haslo_email = 'mko0nji9bhu8'

tytul_polski = 'Tester Manualny - Roman Glegola dla firmy '
tytul_angielski = 'Manual Tester - Roman Glegola for company '

try:
    textfile = 'Tresc_wiadomosci_PL.txt'
    with open(textfile, 'r') as fp:
        #tworzymy obiekt MIMEText w paramatrze podając zawartość pliku
        #jest to obiekt odpowiadający za treść maila
        text = MIMEText(fp.read())
    print('Plik odczytany')
except:
    print('Błąd pliku')

msg = MIMEMultipart()

#ustawiamy nagłówki niezbędne do poprawnej wysyłki maila
#nadawca
msg['From'] = adres_email

#odbiorca
msg['To'] = ['romanglegola@gmail.com']

#temat
msg['Subject'] = tytul_polski

#dołączamy treść maila do naszej wiadomości
msg.attach(text)

try:
    # tworzymy obiekt dzięki któremy wyślemy wiadomość
    # w konstruktorze podajemy adres serwera dzięki któremy będziemy wysyłać wiadomość
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()

    # podany serwer wymaga uwierzytelnienia więc wywołujemy metodę do logowania
    server.login(adres_email, haslo_email)

    # wywłamy wiadomość, moetoda msg.as_string() zamienia obiekt MIMEMultipart ze wszystkim załącznikami
    # na wiadomość zgodną z RFC do wysłania wiadomośći
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # zamykamy nasze połaczenie z serwerem
    # analogicznie do otwierania plików można użyć tutaj konstrukcji with-as
    # dzięki czemu server.quit() wykona się samo po wyjściu z bloku with i nie trzeba tej metody jawnie wykonywać
    server.quit()

    # potwierdzamy wysłanie wiadmości komunikatem
    print('Wiadomość wysłana')
except:
    # informujemy o błędzie występującym przy wysyłaniu wiadomości
    print('Błąd wysyłania')
