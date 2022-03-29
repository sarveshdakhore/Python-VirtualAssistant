import os, platform, database
try:
    import pyttsx3
except:
    os.system("pip install pyttsx3")
    import pyttsx3
try:
    import pyaudio
except:
    try:
        os.system("pip install pyaudio")
        import pyaudio
    except:
        os.system("conda install pyaudio")
        import pyaudio
    
try:
    import speech_recognition as sr
except:
    os.system("pip install speechrecognition")
    import speech_recognition as sr
    
line = " ___________________________________________________________ "
speak_mode = 0
negative_comment_speach, exit_speach = "It's a negative comment so i can't proceed.", " - Good bye!!  ,Hope we will meet soon"
negative_comment, positive_comment = ["dont",'not to','not',"don't",'never do this', 'never do' , "never" , "turn off","stop"], ["do","now","start","turn on","turnon"]
voice_off=["voice","voice control"]
speak_turn_off= "speak speaking"
speak_turn_off= speak_turn_off.split()

def nif():
    print("\n - No input found")
    if speak_mode==1:
            pyttsx3.speak("No input found.")

if platform.system() == "Windows" or platform.system()=="Darwin":
    if platform.system()=="Darwin":
        err_app = 256
        def wero(n_app_act):
            os.system("osascript -e 'quit app "+'"'+n_app_act+'"'+"'")
            
        def open_app(app_name):
            return os.system('open -a "'+app_name+'".app')
            
    else:
        err_app = 1
        def wero(n_app_act):
            os.system("taskkill /im "+n_app_act+".exe /t /f")
        def open_app(app_name):
            return os.system('start ' +app_name)
        
    x=database.retrive_app_data()
    def speech_or_text(text_to_process):
        print(text_to_process)
        if speak_mode==1:
            pyttsx3.speak(str(text_to_process))
    
    def show_apps():
        x=database.retrive_app_data()
        print("\n \n")
        print("THE APPS THAT I CAN OPEN FOR YOU : \n")
        for i in range(1,len(x)):
            q=str(i)
            print(q+") "+x[i][1])
        print("\n")
    
    
else:
    exit
    
to_clear_screen=[]
app_name=""
print("\n\t\t\t\t-------------------------------- \n\n\t\t\t\t what can I help you with ?\n\n\t\t\t\t-------------------------------- \n")
voice_control=0
pyttsx3.speak("What Can I help You with")
show_apps()

while True:                  # Start from here
    opo=1
    to_clear_screen.append("1")
    requirements=""
    to_control_switch=1
    to_control_app_opening=1
    to_control_understanding=1
    
    if len(to_clear_screen)>20:
        show_apps()
        to_clear_screen.clear()
        
        if platform.system()=="Windows":
            os.system("cls")
        else:
            os.system("clear")
    
    app_list_n=[]
    to_control=1
    to_control_b=1
    print(line +" \n ")
    
    if voice_control==1:    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say what you want? \n")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source,phrase_time_limit=3)
            try:
                requirements = r.recognize_google(audio)
            except sr.UnknownValueError or LookupError:
                    print("No Input")
                    requirements=""
            print(requirements)
            print("\n Speech done.....")
            print(line+"\n \n")
    
    else:
        requirements = input("enter your choice:- ")
    req_2=requirements
    requirements=requirements.lower()
    req_1 = requirements

    if "exit" in requirements or "exit()" in requirements or "good bye" in requirements or "bye" in requirements:
        database.close_s()
        print("\n "+exit_speach+" \n \n"+line+"\n \n")
        if speak_mode==1:
            pyttsx3.speak(exit_speach)
        break
    
    row = 0        #row
    sentece_postm = requirements.split()

    for h in negative_comment:             # IN SEARCH OF NEGATIVE COMMENT
        if h in requirements:
            to_control_switch=0

    if voice_control==1 and to_control_switch==0:
        for h in voice_off:
            if h in requirements:
                if voice_control==0:
                    break
                else:
                    for k in negative_comment:
                        if k in requirements:
                            voice_control=0
                            to_control=0
                            print("\n - Voice control turned off successfully")
                            pyttsx3.speak("Voice control turned off successfully")
                            break
            elif voice_control==0:
                break

    elif voice_control==0 and to_control_switch==1:
        for h in voice_off:
            if h in requirements:
                if voice_control==1:
                    break
                else:
                    for k in positive_comment:
                        if k in requirements:
                            voice_control=1
                            to_control=0
                            print("\n - Voice control turned on successfully")
                            pyttsx3.speak("Voice control turned on successfully")
                            break
            elif voice_control==1:
                break

    if speak_mode==1 and to_control_switch==0:
        for h in speak_turn_off:
            if h in requirements:
                if speak_mode==0:
                    break
                else:
                    for k in negative_comment:
                        if k in requirements:
                            speak_mode=0
                            to_control=0
                            print("\n - speaking mode turned off successfully")
                            break  
            elif speak_mode==0:
                break

    elif speak_mode==0 and to_control_switch==1:
        for h in speak_turn_off:
            if h in requirements:
                if speak_mode==1:
                    break
                else:
                    for k in positive_comment:
                        if k in requirements:
                            speak_mode=1
                            to_control=0
                            print("\n - speaking mode turned on successfully")
                            pyttsx3.speak("speaking mode turned on successfully")
                            break
            elif speak_mode==1: 
                break
    
    if to_control==1:                   # IN SEARCH OF NEGATIVE COMMENT
            for h in sentece_postm:
                if (h in negative_comment) and h not in speak_turn_off :
                    speech_or_text(negative_comment_speach)
                    to_control=0
                    break
                if (h in negative_comment) and (h in speak_turn_off):
                    break

    if ("remove" in requirements or "delete" in requirements) and ("app" in requirements or "apps" in requirements) and to_control==1:
        to_control_app_opening=0
        show_apps()
        print(line)
        while True:
            rm_app=""
            print()
            try:
                rm_app=int(input("Enter number/to exit '0' :- "))
            except ValueError:
                pass
            if rm_app==0:
                speech_or_text("Exited!!")
                break
                
            elif rm_app in range(1,len(x)+1):
                x=database.retrive_app_data()
                speech_or_text(x[rm_app][1]+" Removed successfully !!")
                database.remove_app_sql(rm_app)
                show_apps()
                to_control_app_opening=0
                print("\n"+line)
                break
            else:
                speech_or_text("\n Wrong Input!!")
                print(line)

    if ("add" in requirements) and ("app" in requirements or "apps" in requirements) and (to_control==1):
        to_control_app_opening=0
        while True:
            pop_1=1
            n_app=input("Display Name :-  ")
            if len(n_app.split()) == 0 or n_app.isnumeric():
                speech_or_text("\n Wrong Input")
                print(line)
            elif n_app=="exit":
                break
            else:
                n_app_act=input("Actual Name :-  ")
                
                if len(n_app_act.split()) == 0:
                    speech_or_text("\n No Input")
                    print(line)
                elif n_app_act=="exit":
                    break
                
                if open_app(n_app_act) == err_app:
                    print("App does not exist.")
                    print(line+"\n")
                    pop_1=0
                
                elif pop_1!=0:
                    print("\nTrying to opening app .....")
                    wero(n_app_act)
                    print("-------- app was opened for confirmation...... \n"+"Confirmation done... \n"+line+"\n")

                    nic_name_app=[]
                    n_app_nic=""
                    while True:
                        n_app_nic=input("Nick Name/exit->0 :-  ").lower()
                        n_app_nic=n_app_nic.lower()
                        if len(n_app_nic.split()) == 0:
                            speech_or_text("\n No Input")
                            print(line)
                        elif n_app_nic=="exit" or "0" in n_app_nic:
                            break                     
                        else:
                            nic_name_app.append(n_app_nic)
                    app_list_n.append(n_app_act)
                    app_list_n.append(n_app)
                    
                    for i in range(len(nic_name_app)):
                        app_list_n.append(nic_name_app[i])
                        
                    database.add_app_sql(app_list_n)
                    to_control_understanding=0
                    print("\n"+line+"\n")
                    speech_or_text(n_app+" Added successfully !!")
                    x=database.retrive_app_data()
                    show_apps()
                    break

    if "show" in requirements and "app" in requirements and to_control==1:
        show_apps()
        
    elif to_control==1 and to_control_app_opening==1:
        x=database.retrive_app_data()
        for h in sentece_postm:
            if (h in negative_comment) and h not in speak_turn_off :
                speech_or_text(negative_comment_speach)
                break
            if (h in negative_comment) and (h in speak_turn_off):
                break

        if to_control==1 and to_control_understanding==1:                               
                if req_2.isnumeric():
                    req_2=int(req_2)
                    if req_2 in range(0,len(x)):
                        row=req_2
                                            
                else:
                    for r in range(1,len(x)):
                        for d in x[r]:
                            if d.lower() in req_1:
                                row=r    
                                break   
                            
                if row ==0 and to_control_understanding==1:
                    speech_or_text("Unable to understand")
                    
                else:
                    app_name=x[row][0]
                    
                    if "quit" in sentece_postm:
                        wero(app_name)   
                    elif open_app(app_name) == err_app:
                        opo=0
                        print("App does not exist. \n It has been removed as its not existed \n")
                        print(line+"\n")
                        database.remove_app_sql(row)
                    else:
                        app_name1=x[row][1]
                        speech_or_text(" - Command for opening "+app_name1+". given successfully")
                            
                            
                            
                            
                            
                            
