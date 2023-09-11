import pywhatkit as pwk
 
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     for i in range(10):
        pwk.sendwhatmsg_instantly("+9190874 21814", "*IPRTC* Corporation:PNR NO.:T39846883, From:CHENNAI-PT Dr.M.G.R. BS To KUMBAKONAM, Trip Code:2330CHEKUMAB, Journey Date:13/01/2023, Time:13/01/2023,00:30, Seat No.:12,14,15.Class:AC SLEEPER SEATER, Boarding at:CHENNAI-PT Dr.M.G.R. BS.For e-Ticket: https://www.IPRTC.in/IPRTCOnline/vt.do?PNR=T39876787 Please carry your photo ID during journey. T&C apply. www.iprtc.in",10)
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")