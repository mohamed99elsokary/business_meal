from TaqnyatSms import client


def send_sms(phone: str, text: str):
    bearer = "**************************0adc2b"
    taqnyat = client(bearer)
    taqnyat.sendMsg(text, [phone], "sender_name")
