import time


def mail(
	msg = 'Atenção!\nSeu algorítmo retornou algo.',
	sub = 'Notificação programada',
	from_user = '[GMAIL EMAIL]',
	from_pass = '[GMAIL PASSWORD]',
	to_user):
	import smtplib
	import unidecode
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_user, from_pass)
	msg += '\n\nAtenciosamente,\nDayane.'
	sub = unidecode.unidecode(sub)
	msg = unidecode.unidecode(msg)
	msg = 'Subject: {}\n\n{}'.format(sub, msg)
	if type(to_user) == str:
		to_user = [to_user]
	if type(to_user) == list:
		for user in to_user:
			server.sendmail(from_user, user, msg)
	server.quit

def pdf_mail(
    filepath = None,
    filename = 'doc.pdf',
    msg = 'Atenção!\nSeu algorítmo retornou algo.',
    sub = 'Notificação programada',
    from_user = '[GMAIL EMAIL]',
    from_pass = '[GMAIL PASSWORD]',
    to_user):

    import email, smtplib, ssl
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart


    MSG = MIMEMultipart()
    MSG['Subject'] = sub
    MSG['From'] = from_user
    MSG['To'] = to_user

    MSG.attach(MIMEText(msg))

    part = MIMEBase("application", "octet-stream")
    doc = open(filepath, 'rb')
    c = doc.read()
    part.set_payload(c)
    encoders.encode_base64(part)

    part.add_header(
    "Content-Disposition",
    f"doc; filename= {filename}",
    )
    MSG.attach(part)
    text = MSG.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_user, from_pass)
        server.sendmail(from_user, to_user, text)


def celtext(
	message = 'Atenção!\nSeu algorítmo retornou algo.',
	phone,
	):
	#import unidecode
	from twilio.rest import Client

	account_sid = ""
	auth_token = ""
	msg_id = ''

	#msg = unidecode.unidecode(message)
	msg = message
	client = Client(account_sid, auth_token)

	client.messages.create(
		to = phone,
		messaging_service_sid = msg_id,
		body = msg)

def soundalert(alert = 'mario', sem = 150):
	import winsound
	from ztools.dicts import notes
	if alert == 'mario':
		winsound.Beep(notes['e']*2, int(sem/2))
		winsound.Beep(notes['e']*2, int(sem))
		winsound.Beep(notes['e']*2, int(sem))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['e']*2, int(sem))
		winsound.Beep(notes['g']*2, int(sem)*5)
		winsound.Beep(notes['g'], int(sem)*4)
	elif alert == 'win':
		winsound.MessageBeep()
	elif alert == 'wedding':
		winsound.Beep(notes['c']*2, int(sem))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['c']*2, int(sem)*6)
		time.sleep(1)
		winsound.Beep(notes['c']*2, int(sem))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['c']*2, int(sem)*6)
		time.sleep(1)
		winsound.Beep(notes['c']*2, int(sem))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['c']*2, int(sem/2))
		winsound.Beep(notes['e']*2, int(sem)*4)
		winsound.Beep(notes['e']*2, int(sem))
		winsound.Beep(notes['e']*2, int(sem/2))
		winsound.Beep(notes['e']*2, int(sem/2))
		winsound.Beep(notes['e']*2, int(sem)*4)
		winsound.Beep(notes['e']*2, int(sem))
		winsound.Beep(notes['e']*2, int(sem/2))
		winsound.Beep(notes['e']*2, int(sem/2))
		winsound.Beep(notes['g']*2, int(sem)*4)
		winsound.Beep(notes['g']*2, int(sem))
		winsound.Beep(notes['g']*2, int(sem/2))
		winsound.Beep(notes['g']*2, int(sem/2))
		winsound.Beep(notes['g']*2, int(sem)*4)
		winsound.Beep(notes['g']*2, int(sem))
		winsound.Beep(notes['g']*2, int(sem/2))
		winsound.Beep(notes['g']*2, int(sem/2))
		winsound.Beep(notes['c']*4, int(sem)*5)
		winsound.Beep(notes['b']*2, int(sem*5))
		winsound.Beep(notes['f']*2, int(sem))
		winsound.Beep(notes['a']*2, int(sem*3))
		winsound.Beep(notes['g']*2, int(sem*3))
		winsound.Beep(notes['f']*2, int(sem*3))
		winsound.Beep(notes['d']*2, int(sem*3))
		winsound.Beep(notes['c']*2, int(sem*5))
	
	elif alert == 'numb':
		winsound.Beep(notes['cs']*2, int(sem))
		winsound.Beep(notes['e']*2, int(sem))
		winsound.Beep(notes['cs']*2, int(sem))
		winsound.Beep(notes['fs']*2, int(sem*3))
		winsound.Beep(notes['a']*2, int(sem*3))
		winsound.Beep(notes['gs']*2, int(sem*5))
		time.sleep(0.5)
		winsound.Beep(notes['cs']*2, int(sem))
		winsound.Beep(notes['fs']*2, int(sem))
		winsound.Beep(notes['cs']*2, int(sem))
		winsound.Beep(notes['a']*2, int(sem*3))
		winsound.Beep(notes['gs']*2, int(sem*3))
		winsound.Beep(notes['e']*2, int(sem*5))
		
def telegram(msg = 'Atenção!\nSeu algorítmo retornou algo.',
	tkn = '[TELEGRAM BOT TOKEN]',
	to_user = '[YOUR_TELEGRAM_USER]'):
	import telebot
	bot = telebot.TeleBot(tkn)
	bot.send_message(to_user, msg)