import PySimpleGUI as sg
from datetime import datetime
import pyttsx3
now = datetime.today()

global age_year
global age_month
global age_day

converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 1)

def Text_to_speech(msg):
    converter.say(msg)
    converter.runAndWait()
    return "Voice:  "

def fortune_teller(event,values):
    color = str(values["inp1"])

    if color == "black" or color == "white":
        number = int(values["inp2"])
        if number == 1:
            sg.popup(Text_to_speech("You'll 100% get what you want, be patient!")+"You'll 100% get what you want, be patient!",image=sg.EMOJI_BASE64_HAPPY_WINK,keep_on_top=True)
        elif number == 2:
            sg.popup(Text_to_speech("You will become a millionaire at the age of 35!")+"You will become a millionaire at the age of 35!",image=sg.EMOJI_BASE64_HAPPY_JOY,keep_on_top=True)
        elif number == 3:
            sg.popup(Text_to_speech("You will be hungry again in 10 minutes!")+"You will be hungry again in 10 minutes!",image=sg.EMOJI_BASE64_HAPPY_RELIEF,keep_on_top=True)
        elif number == 4:
            sg.popup(Text_to_speech("You will become famous and everyone will love you!")+"You will become famous and everyone will love you!",image=sg.EMOJI_BASE64_HAPPY_HEARTS,keep_on_top=True)
        else:
            txt = "Numbers 1,2,3,4 are the only numbers allowed"
            sg.popup(Text_to_speech(txt) + txt, image=sg.EMOJI_BASE64_WEARY, keep_on_top=True)

    elif color == "pink" or color == "purple":

        number = int(values["inp2"])
        if number == 1:
            ast="All your hardwork will soon pay off !"
            sg.popup(Text_to_speech(ast)+ast,image=sg.EMOJI_BASE64_HAPPY_THUMBS_UP,keep_on_top=True)
        elif number == 2:
            ast="You will soon gain something you have always wanted "
            sg.popup(Text_to_speech(ast)+ast,image=sg.EMOJI_BASE64_HAPPY_WINK,keep_on_top=True)
        elif number == 3:
            ast="Good news of a long-awaited event will soon arrive !"
            sg.popup(Text_to_speech(ast)+ast,image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE,keep_on_top=True)
        elif number == 4:
            ast="Don’t worry about money. The best things in life are free.!"
            sg.popup(Text_to_speech(ast)+ast,image=sg.EMOJI_BASE64_HAPPY_CONTENT,keep_on_top=True)
        else:
            txt="Numbers 1,2,3,4 are the only numbers allowed"
            sg.popup(Text_to_speech(txt)+txt,image=sg.EMOJI_BASE64_WEARY,keep_on_top=True)

    elif color == "blue" or color == "red":

        number = int(values["inp2"])
        if number == 1:
            ans="Your present plans are going to succeed"
            sg.popup(Text_to_speech(ans)+ans,image=sg.EMOJI_BASE64_HAPPY_JOY,keep_on_top=True)
        elif number == 2:
            ans="Error 404 ! Fortune not found.."
            sg.popup(Text_to_speech(ans)+ans,image=sg.EMOJI_BASE64_DREAMING,keep_on_top=True)
        elif number == 3:
            ans="You will have very good luck today!"
            sg.popup(Text_to_speech(ans)+ans,image=sg.EMOJI_BASE64_HAPPY_LAUGH,keep_on_top=True)
        elif number == 4:
            ans="Someone has googled you recently!"
            sg.popup(Text_to_speech(ans)+ans,image=sg.EMOJI_BASE64_HAPPY_GASP,keep_on_top=True)
        else:
            ans = "Numbers 1,2,3,4 are the only numbers allowed"
            sg.popup(Text_to_speech(ans) + ans, image=sg.EMOJI_BASE64_WEARY, keep_on_top=True)

    else:
      ms = "Colors [black, white, blue, red,pink , purple] are only allowed"
      sg.popup(Text_to_speech(ms) + ms, image=sg.EMOJI_BASE64_WEARY, keep_on_top=True)



def age_calc(event, values):
    month= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    birth_year = int(values["_IN1_"])
    birth_month = int(values["_IN2_"])
    birth_day = int(values["_IN3_"])
    if(birth_year>=0 and birth_month<=12 and birth_month>=0 and birth_day<=31 and birth_day>=0):
      current_year = now.year
      current_month = now.month
      current_day = now.day
      if (birth_day > current_day) :
         current_day = current_day + month[birth_month - 1]
         current_month = current_month - 1

      if (birth_month > current_month):
         current_year = current_year - 1
         current_month = current_month + 12



      age_year = current_year - birth_year
      age_month = abs(current_month - birth_month)
      age_day = abs(current_day - birth_day)

      ans = "You are\n\n   " + str(age_year) + ":Years\n\n  " + str(age_month) + ":months \n\n  " + str(age_day) + ":days  old"
      sg.popup(Text_to_speech(ans) + ans, keep_on_top=True,font="_12")

    else:
      sg.popup('HEY DUDE! SOMETHING WENT WRONG. PLEASE ENTER VALID DATE', image=sg.EMOJI_BASE64_WEARY, keep_on_top=True)


sg.theme('SandyBeach')
tab1_layout = [
    [sg.Text("Self Introduction")],
    [sg.Text('  ')],
    [sg.Text('HI I AM BOT HERE!'), sg.Image(data=sg.EMOJI_BASE64_HAPPY_HEARTS)],
    [sg.Text('  ')],
    [sg.Text("WHAT'S YOUR NAME?")],
    [sg.Text('  ')],
    [sg.Image(data=sg.EMOJI_BASE64_HAPPY_BIG_SMILE), sg.Input(size=(30, 30), key='-INPUT-', border_width=10),
     sg.Button('Enter')],
    [sg.Text(size=(70, 1), key='-OUTPUT-')],
    [sg.Text('  ')],
    [sg.Button('Time')],
    [sg.Text('  ')],

    [sg.Text("PROGRAMMED BY JTN..")]
]

tab2_layout =[
    [sg.T('This tab calcuates your exact age.')],
    [sg.Text('  ')],
    [sg.Text('AGE PREDICTOR'), sg.Image(data=sg.EMOJI_BASE64_HAPPY_HEARTS)],
    [sg.Text('  ')],
    [sg.Text("Enter your year of birth:\n"), sg.Input(size=(20, 30), key="_IN1_")],
    [sg.Text("Enter your month of birth:\n"), sg.Input(size=(20, 30), key="_IN2_")],
    [sg.Text("Enter your date of birth:\n"), sg.Input(size=(20, 30), key="_IN3_")],
    [sg.Text("WANT TO KNOW YOUR AGE?",)],
    [sg.Image(data=sg.EMOJI_BASE64_HAPPY_BIG_SMILE), sg.Button('YES', key='_YES_'),
                         sg.Button('NO',key='_NO_')],
    [sg.Text("PROGRAMMED BY JTN..")]
               ]

tab3_layout = [
    [sg.T('HEY!I AM A FORTUNE TELLER..')],
    [sg.Text('  ')],
    [sg.Text('Let me tell you about your Fortune!'), sg.Image(data=sg.EMOJI_BASE64_PONDER)],
    [sg.Text('  ')],
    [sg.Text("You will select a color and a number and I will tell you what the future holds for you!")],
    [sg.Text(" ")],
    [sg.Text("Select a colour (black, white, blue, red,pink,purple) :\n"), sg.Input(size=(20, 30), key="inp1")],
    [sg.Text("Select a number [1, 2, 3, 4]:\n"), sg.Input(size=(20, 30), key="inp2")],
    [sg.Text("Press YES to know your fortune..")],
     [sg.Image(data=sg.EMOJI_BASE64_HAPPY_BIG_SMILE), sg.Button('yes'),
                         sg.Button('NO')],
    [sg.Text("PROGRAMMED BY JTN..")]
]


tab4_layout = [
    [sg.T('Questioning Bot')],
    [sg.Text('  ')],
    [sg.Text('HI I AM BOT HERE!'), sg.Image(data=sg.EMOJI_BASE64_HAPPY_HEARTS)],
    [sg.Text('  ')],
    [sg.Image(data=sg.EMOJI_BASE64_HAPPY_WINK)], [sg.Text("CHOOSE ME A QUESTION I'LL ANS YOU")],
    [sg.Text('  ')],
    [sg.Text(' 1.'), sg.Button('Are you a robot?', key='1st')],
    [sg.Text('2. '), sg.Button('How are you?', key='2nd')],
    [sg.Text('  ')],
    [sg.Text("PROGRAMMED BY JTN..")]
]

tab5_layout = [
    [sg.T('Rating tab')],
    [sg.Text('  ')],
    [sg.Text('YOUR FEEDBACK BOOST US'),sg.Image(data=sg.EMOJI_BASE64_HAPPY_JOY)],[sg.Text('  ')],
    [sg.Image(data=sg.EMOJI_BASE64_HAPPY_WINK), sg.Text('RATE US WITHIN 5 STARS....')],[sg.Text('  ')],
    [sg.Radio('1', 'rate'), sg.Image(data=sg.EMOJI_BASE64_SAD),
     sg.Radio('3', 'rate'),sg.Image(data=sg.EMOJI_BASE64_HAPPY_STARE),
     sg.Radio('5', 'rate'), sg.Image(data=sg.EMOJI_BASE64_HAPPY_HEARTS)],[sg.Text('  ')],
    [sg.Button('EXIT')],[sg.Text('  ')], [sg.Text("PROGRAMMED BY JTN..")]]

layout = [[sg.TabGroup([[sg.Tab(' 1 ', tab1_layout, element_justification='center'),
                         sg.Tab(' 2 ', tab2_layout, element_justification='center'),
                         sg.Tab(' 3 ', tab3_layout, element_justification='center'),
                         sg.Tab(' 4 ', tab4_layout, element_justification='center'),
                         sg.Tab(' 5 ', tab5_layout, element_justification='center')]])]]

window = sg.Window('TETE A TETE WITH BOT:)', layout,font=('Times',15,'roman'), icon=sg.EMOJI_BASE64_HAPPY_BIG_SMILE, titlebar_text_color='Purple' , keep_on_top=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        sg.theme('DarkBlue6')
        sg.popup(Text_to_speech("HEY A FRIENDLY REMAINDER\n\n Distance make us Stronger\n\nTough times don't Last\n\nSTAY HOME STAY SAFE\n\n'THANK YOU!'")+"HEY A FRIENDLY REMAINDER\n\nDistance make us Stronger\n\nTough times don't Last\n\nSTAY HOME STAY SAFE\n\n'THANK YOU!'",font="_10", image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE, keep_on_top=True)
        break
    elif event == 'Enter':
        sg.theme('DarkBlue6')
        sg.popup(Text_to_speech('HELLO ' + values['-INPUT-'] + " ! GLAD  TO MEET YOU !")+'HELLO ' + values['-INPUT-'] + " ! GLAD  TO MEET YOU !",font="_12", image=sg.EMOJI_BASE64_HAPPY_JOY,
                 keep_on_top=True)
    elif event == 'Time':
        sg.theme('DarkBlue6')
        sg.popup('Date and Time:' + str(now),font="_12", image=sg.EMOJI_BASE64_HAPPY_WINK, keep_on_top=True)
    elif event == '_YES_':
        sg.theme('DarkBlue6')
        age_calc(event, values)
    elif event == '_NO_':
        sg.theme('DarkBlue6')
        sg.popup(Text_to_speech('OOPS ! you have missed this interesting part')+'OOPS ! you have missed this interesting part',font="_12", image=sg.EMOJI_BASE64_WEARY, keep_on_top=True)
    elif event == '1st':
        sg.theme('DarkBlue6')
        sg.popup(Text_to_speech('YEAH ! UNDOUBTEDLY ')+'YEAH ! UNDOUBTEDLY ',font="_12", image=sg.EMOJI_BASE64_HAPPY_RELIEF, keep_on_top=True)
    elif event == '2nd':
        sg.theme('DarkBlue6')
        sg.popup(Text_to_speech('COOL ! THANK YOU')+'COOL ! THANK YOU',font="_12", image=sg.EMOJI_BASE64_HAPPY_HEARTS, keep_on_top=True)
    elif event=="yes":
        sg.theme('DarkBlue6')
        fortune_teller(event,values)
    elif event == 'No':
        sg.theme('DarkBlue6')
        sg.popup(Text_to_speech('OOPS ! you have missed this interesting part')+'OOPS ! you have missed this interesting part',font="_12", image=sg.EMOJI_BASE64_WEARY, keep_on_top=True)
window.close()
