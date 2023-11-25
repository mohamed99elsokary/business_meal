from TaqnyatSms import client


def send_sms(phone: str, text: str):
    api_token = "Bearer 6faea28d8537ca40aae05692ce053916"
    sender_name = "BusinesMeal"
    taqnyat = client(api_token)
    taqnyat.sendMsg(text, [phone], sender_name, scheduled=[])
