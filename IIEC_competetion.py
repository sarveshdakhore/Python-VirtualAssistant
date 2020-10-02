import os
import platform
import prat
import imp
import speech_recognition as sr

try:
    import time
except ModuleNotFoundError:
    os.system("pip install time")
    import time

try:
    import pyttsx3
except ModuleNotFoundError:
    os.system("pip install pyttsx3")
    import pyttsx3

name_user="Prathmesh"

line = " ___________________________________________________________________ "


'''
print("\n \n \n "+line+" \n \n \n")

print("WHAT DOES THIS PROGRAM DO: \n \n 1)  YOU CAN OPEN APPLICATIONS : TO add more application just make [] seperated via couma and first \n add orignal app name in string and than the what would you will type to open the app in \n another string all strings should seperated by couma. \n")
print("\t\t\t\t-----------------------------------")
print("\n 2) YOU CAN GO TO FINDER by typing 'go to finder' : there are lots of thigs to do \n")
print("\t\t\t\t-----------------------------------")
print("\n 3) YOU CAN TURN ON OR OFF SPEAKING OF YOUR DEVICE BY TYPING NEGATIVE WORD LIKE 'not,never,etc'  and on by typing 'now speak, do speak' \n \n ")




print(line+" \n")
print(" This specially made for mac users  \n You can open all apps which mac have. \n and programe is written in mac")
print("\n "+line+" \n \n")
pyttsx3.speak("User please Enter Your Name ")
name_user=input("Enter Your Name :- ")
print("\n \n"+line+" \n")

'''

speak_mode = 0

#about program

negative_comment_speach = "It's a negative comment so i can't proceed."
exit_speach = " - Good bye! "+name_user+"! hope we will meet soon"
negative_comment = ["dont",'not to','not',"don't",'never do this', 'never do' , "never" , "turn off","stop"]
positive_comment= ["do","now","start"]

voice_off=["voice"]
speak_turn_off= "speak"
speak_turn_off= speak_turn_off.split()

def nif():
    print("\n - No input found")
    if speak_mode==1:
            pyttsx3.speak("No input found.")


app_name=""


# FOR WINDOWS
print("\t\t\t\t what can I help you with ?")
print("\t\t\t\t-------------------------------- \n")
'''
pyttsx3.speak("Hello "+name_user +"! I am Darwin your virtual assistant! What can I help you with!")
'''
if platform.system() == "Windows":
    print("you are operating this program on windows.....")
    pyttsx3.speak("you are operating this program on windows.....")
    
    pyttsx3.speak("This program is mainly made for Mac (OS)! but optimized also for windows! There are some chances that some function may not work in windows")

    x = [[""],["wmplayer","Windows Media Player","windows media player","windowsmediaplayer","wmp","video player"],["control","setting","settings","control","love to change things"],["Anaconda Navigator", "anaconda","Anaconda-Navigator","conda","Navigator"],["MsEdge", "Microsoft Edge","edge","edge browser","micrisoft browser"],["chrome","Google chrome","browser","net surfing in google "],["arcroRd32","acrobat","adobe acrobat"],["creative cloud","creative cloud","adobe cloud",],["illustrartor","Adobe illustrartor","illustrator","illustator","design","designing"," adobe logo maker"],["photoshop","photo shop","Photoeditor","editing"],["Excel","Microsoft Excel","excel","microsoft excel","excel data entry",],["chrome","Google chrome","net surfing in google"],["onenote","Microsoft OneNote","office","mf office",],["powerpnt","Power Point","powerpoint","power point","Presentation","ppt presentation",],["winword","document","word","writing pad"]]


   
    
    
    def show_apps():
        print("\n \n")
        print("THE APPS THAT I CAN OPEN FOR YOU IF IT EXIST: \n")
        for i in range(1,len(x)):
            q=str(i)
            print(q+") "+x[i][1])
        print("\n")

    
    def open_app():
        os.system('start ' +app_name)

    def file_creater():
        os.system("Type "+name+ext)
        print("\n "+line+" \n")
        os.system("dir")
        time.sleep(0.1)
        print("\n "+line+" \n")
        

    file_types=[[".txt",'Text File','textfile','text file','Text edit'],[".pptx","Power Point Presentation","ppt","powerpoint","power point" ,"presentation"],[".docx","Microsoft Word","ms word","word","msword","microsoft word"],[".xlsx","Microsoft Excel","excel"]]

    def file_opener():
        df='"'+name+ext+'"'
        os.system(df)
    def uni_f_op():
        if len(inp_1)!=1:
            z_1=inp_1[1]
            for i in inp_1[2:]:
                  z_1+=" "+i
            os.system("open "+z_1)
        else:
            nif()

    def folder_creater():
        if len(inp_1)!=1:
            
            folder_n=inp_1[1]
            for i in inp_1[2:]:
                  folder_n+=" "+i
            folder_n=folder_n+'"'
            os.system('mkdir "'+folder_n)
            print(" - folder made successfully")
            if speak_mode==1:
                pyttsx3.speak("folder made successfully")
        else:
            nif()

    def rename_file():
        if len(inp_1)!=1:
            z_1=inp_1[1]
            for i in inp_1[2:]:
                z_1+=" "+i

            if z_1 in os.listdir():
                if speak_mode==1:
                    pyttsx3.speak("Enter your files new name: ")
                new_f=input("Enter your files new name: ")
                nnn =' "'+new_f+'"'


                os.system('ren "'+z_1+'"'+nnn)

                print(" - file renamed successfully.")
                if speak_mode==1:
                    pyttsx3.speak("file renamed successfully.")
            else:
                print("\n - there is no such file")
                if speak_mode==1:
                    pyttsx3.speak("there is no such file.")
        else:
            nif()


    def del_files():


        if len(inp_1)!=1:
            z_1=inp_1[1]
            for i in inp_1[2:]:
                  z_1+=" "+i


        if z_1 in os.listdir():

             print(z_1)
             os.system('rmdir "'+z_1+'"')


             print(z_1+" - file deleted successfully.")
             if speak_mode==1:
                pyttsx3.speak(z_1+" file deleted successfully.")
        else:
            nif()






#qwertyuiopasdfghjklzxcvbnm





# MAC START HERE
if platform.system() == "Darwin":
    print("you are operating this program on Mac.....")






#for mac
    x=prat.apps_list_fin




    def open_app():
        os.system('open -a "'+app_name+'".app')

        
        
    def file_creater():
        os.system("touch "+name+ext)
        print("\n "+line+" \n")
        os.system("ls")
        time.sleep(0.1)
        print("\n "+line+" \n")
        
        

    
        
    def show_apps():
        print("\n \n")
        print("THE APPS THAT I CAN OPEN FOR YOU IF IT EXIST: \n")
        for i in range(1,len(x)):
            q = str(i)
            print(q+") "+x[i][1])
        print("\n")

    def file_opener():
        df=name+ext
        os.system("open "+df)
    def uni_f_op():
        if len(inp_1)!=1:
            z_1=inp_1[1]
            for i in inp_1[2:]:
                  z_1+=" "+i
            z_1=z_1+'"'
            os.system('open "'+z_1)
        else:
            nif()

    def folder_creater():
        if len(inp_1)!=1:
            
            folder_n=inp_1[1]
            for i in inp_1[2:]:
                  folder_n+=" "+i
            folder_n=folder_n+'"'
            os.system('mkdir "'+folder_n)
            print(" - folder made successfully")
            if speak_mode==1:
                pyttsx3.speak("folder made successfully")
        else:
            nif()

    def rename_file():
        if len(inp_1)!=1:
            z_1=inp_1[1]
            for i in inp_1[2:]:
                  z_1+=" "+i
    
            if z_1 in os.listdir():
                if speak_mode==1:
                    pyttsx3.speak("Enter your files new name: ")
                new_f=input("Enter your files new name: ")
                nnn =' "'+new_f+'"'
    
    
                os.system('mv "'+z_1+'"'+nnn)
    
                print(" - file renamed successfully.")
                if speak_mode==1:
                    pyttsx3.speak("file renamed successfully.")
    
            else:
                print("\n - there is no such file")
                if speak_mode==1:
                    pyttsx3.speak("there is no such file.")
        else:
            nif()

    def del_files():

        if len(inp_1)!=1:

            z_1=inp_1[1]
            for i in inp_1[2:]:
                  z_1+=" "+i
    
    
            if z_1 in os.listdir():
    
                 
                 os.system('rm -Rf "'+z_1+'"')
    
    
                 print(z_1+" - file deleted successfully.")
                 if speak_mode==1:
                    pyttsx3.speak(z_1+" file deleted successfully.")
            else:
                print("\n - there is no such file")
                if speak_mode==1:
                    pyttsx3.speak("there is no such file.")


        else:
            nif()




else:
    print("THIS PROGRAM IS NOT MADE FOR YOUR OPERATING SYSTEM")

voice_control=0
pyttsx3.speak("How Can I help You with .")
show_apps()






while True:       
                             # Start from here
    to_control_app_opening=1
    imp.reload(prat)
    to_control_understanding=1
    
    
    file_types=prat.file_list_fin 
    x = prat.apps_list_fin  
    
    
    
    app_list_n=[]
    print("\n"+line+" \n")
    to_control=1
    to_control_b=1
    
    
    print(line +" \n \n")
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

        print("\n "+exit_speach+" \n \n"+line+"\n \n")
        if speak_mode==1:
            pyttsx3.speak(exit_speach)
        break


    column = 0        #column
    row = 0        #row


    
    
    sentece_postm = requirements.split()
    
    if voice_control==1:
        for h in voice_off:
            if h in requirements:
                for k in sentece_postm:
                    if k in negative_comment:
                        voice_control=0
                        to_control=0
                        to_control_b=0
                        print("\n - Voice control turned off successfully")
                        
                        pyttsx3.speak("Voice control turned off successfully")
                       
                        break
                    else:
                        pass
            else:
                pass

            
            
    elif voice_control==0:

        for h in voice_off:
            if h in requirements:
                for k in sentece_postm:
                    if k in positive_comment:
                        voice_control=1
                        to_control=0
                        to_control_b=0
                        print("\n - Voice control turned on successfully")
                        pyttsx3.speak("Voice control turned on successfully")
                        break
            else:
                pass
    
    
    
    
    
    
    
    
    if speak_mode==1:
        for h in speak_turn_off:
            if h in requirements:
                for k in sentece_postm:
                    if k in negative_comment:
                        speak_mode=0
                        to_control=0
                        to_control_b=0
                        print("\n - speaking mode turned off successfully")
                        break
                    else:
                        pass
            else:
                pass

            
            
            
            
    if speak_mode==0:

        for h in speak_turn_off:
            if h in requirements:
                for k in sentece_postm:
                    if k in positive_comment:
                        speak_mode=1
                        to_control_b=0
                        to_control=0
                        print("\n - speaking mode turned on successfully")
                        pyttsx3.speak("speaking mode turned on successfully")
                        break
            else:
                pass









    if to_control==1:
           # IN SEARCH OF NEGATIVE COMMENT
        for h in sentece_postm:
            if (h in negative_comment) and h not in speak_turn_off :
                print(negative_comment_speach)
                to_control=0
                if speak_mode==1:
                    
                    pyttsx3.speak(negative_comment_speach)

                break
            if (h in negative_comment) and (h in speak_turn_off):
                break

                
                
                
                
                
                
                
#ADD REMOVE APPS

    if ("remove" in requirements or "delete" in requirements) and ("app" in requirements or "apps" in requirements) and to_control==1:
        to_control_app_opening=0
        t=len(x)+1
        show_apps()
        print(line)
        while True:
            rm_app=""
            try:
                rm_app=int(input("Enter number :- "))
            except ValueError:
                pass
            
            
            
            if rm_app==0:
                print("Exited!!")
                if speak_mode==1:
                    pyttsx3.speak("Exited")
            
            
            
            if rm_app in range(1,t):
                with open("prat.py","a+") as file_O:
                    rm=str(rm_app)
                    file_O.write("\n")
                    print(x[rm_app][1]+" Removed successfully !!")
                    to_control_app_opening=0
                    print("\n"+line)
                    if speak_mode==1:
                        print("\n")
                        pyttsx3.speak(x[rm_app][1]+" Removed successfully")
                    file_O.write("apps_list_fin.remove(apps_list_fin["+rm+"])")
                    imp.reload(prat)
                    break
            
            
            
            else:
                print("\n Wrong Input!!")
                print(line)
                if speak_mode==1:
                    pyttsx3.speak("Wrong Input")
                    
                
                
                

                
    if ("add" in requirements) and ("app" in requirements or "apps" in requirements) and to_control==1:
        to_control_app_opening=0
        while True:
            n_app=input("Display Name :-  ")
            if len(n_app.split()) == 0:
                print("\n No Input")
                print(line)
                if speak_mode==1:
                    pyttsx3.speak("No Input")
                else:
                    pass
            elif n_app=="exit":
                break
            else:#bnvsd
                n_app_act=input("Actual Name :-  ")
                if len(n_app_act.split()) == 0:
                    print("\n No Input")
                    print(line)
                    if speak_mode==1:
                        pyttsx3.speak("No Input")
                    else:
                        pass
                elif n_app_act=="exit":
                    break
                else:
                    
                    nic_name_app=[]
                    
                    n_app_nic=""
                    while True:
                        n_app_nic=input("Nick Name :-  ")
                        n_app_nic=n_app_nic.lower()
                        if len(n_app_nic.split()) == 0:
                            print("\n No Input")
                            print(line)
                            if speak_mode==1:
                                pyttsx3.speak("No Input")
                            else:
                                pass
                        elif n_app_nic=="exit":
                            break
                        else:
                            nic_name_app.append(n_app_nic)
                    app_list_n.append(n_app_act)
                    app_list_n.append(n_app)
                    for i in range(len(nic_name_app)):
                        app_list_n.append(nic_name_app[i])
                    
                        
                          
                            
                    with open("prat.py","a+") as file_O:
                        file_O.seek(0)
                        
                        
                        app_list="'"+"','".join(app_list_n)+"'"       
                                                                       #bvcahgddjvkcvhdvsachkjshavdjc 
                        file_O.write("\n")
                        file_O.write("x_0 = ["+app_list+"]")
                        file_O.write("\n")
                        file_O.write("apps_list_fin.append(x_0)")
                        file_O.write("\n")
                        imp.reload(prat)
                        imp.reload(prat)
                        to_control_understanding=0
                        print("\n"+line+"\n")
                        print(n_app+" Added successfully !!")
                        print(line)
                        if speak_mode==1:
                            pyttsx3.speak(n_app+" Added successfully")
                        break
                        
                        
                        
#----------  







            # file creater

    if "show" in requirements and "app" in requirements and to_control==1:
        show_apps()
    elif "go" in req_1 and "finder" in req_1:
        print("\n \n"+line+"\n \n")
        print(" - You are now in finder. \n")
        
        if speak_mode==1:
            pyttsx3.speak("welcome . , you are now in finder.")
        while True :
              print("\n \n"+line+"\n"+ line+"\n \n")
             
              if platform.system()=="Windows":
                    ls='"dir"'
                    print("hello")
              else:
                    ls = "ls"
              print("Files in directory:- \n ------------ \n")
              os.system(ls)
              time.sleep(0.1)
              print("\n "+line+"\n \n ")
              print(" PLEASE FOLLOW THE INSTRUCTION GIVEN BELOW :-    \n \n FOR EXIT : 'exit()' \n FOR OPENING FILE : 'open filename.extention' \n FOR RENAMING FILE/FOLDER :  'rename foldername or file name.extention' \n FOR OPENING FOLDER :  'open foldername' \n FOR MAKING FOLDER: make foldername \n FOR CREATING FILE :  create  \n FOR DELETING ANY FILE/FOLDER : 'delete filename/foldername' \n \n")
              print(line+" \n \n")
             

              inp_1 = input("what you want to do : ")

              

              if inp_1=="exit()" or inp_1=="exit" or inp_1=="back":

                  print(" - you exited successfully.")
                  if speak_mode==1:
                      pyttsx3.speak("you exited successfully.")
                  break
              inp_1 = inp_1.split()

              inp_1[0]=inp_1[0].lower()
              


              if inp_1==[]:
                  pass

                  #OPEN FILE/FOLDR
              elif "open" in inp_1[0]:

                  uni_f_op()


                  # DELETE FILE
              elif   "delete" in inp_1[0]:

                  del_files()



                # renaming file
              elif "rename" in inp_1[0]:

                  rename_file()


                    # make FOLDER
              elif "make" in inp_1[0]:
                  folder_creater()
                  


              elif "show" in inp_1 and "file" in inp_1:
                   os.system(ls)

                    
                    
                #create files
              elif "create" in inp_1:
                    


                    while True:
                        
                        print("\n "+line)
                        print("""  \n \n  what type thing you want to create

                          """)
                        def show_files():
                            for i in range(0,len(file_types)):
                                print((i+1),end=")  "+file_types[i][1]+"\n")
                    
                        imp.reload(prat)
                        file_types=prat.file_list_fin 
                        show_files()
                        
                        print("\n \n "+line)
                        print('\n \n')
                        print(" FOR GOING BACK PLEASE TYPE 'back()'")
                        print(""" Please enter which type of file you want if your choice not \n listed plss add extention with name to create it \n or you can continue without extention. """)
                        
                        
                        print("\n "+line+" \n")
                        Filenuser = input("Your choice please :- ")
                        print("\n "+line+" \n")
                        
                            
                        if "back()" in Filenuser.lower():
                            break
                        
                       
                        #FILE REMOVER
                        if Filenuser.lower()=="remove file" or Filenuser=="delete file":
                            to_control_app_opening=0
                            t_1=len(file_types)+1
                            show_files()
                            print(line)
                            while True:
                                rm_file=""
                                try:
                                    print("\n \nTo Exit --> '0'")
                                    rm_file=int(input("Enter number :- "))
                                except ValueError:
                                    pass
                                if rm_file==0:
                                    print("Exited!!")
                                    if speak_mode==1:
                                        pyttsx3.speak("Exited")
                                    break
                                elif rm_file in range(1,t_1):
                                    with open("prat.py","a+") as file_O:
                                        rm_file=rm_file-1
                                        rmm=str(rm_file)
                                        file_O.write("\n")
                                        print(file_types[rm_file][1]+" Removed successfully !!")
                                        to_control_app_opening=0
                                        print("\n"+line)
                                        if speak_mode==1:
                                            print("\n")
                                            pyttsx3.speak(file_types[rm_file][1]+" Removed successfully")
                                        file_O.write("file_list_fin.remove(file_list_fin["+rmm+"])")
                                        imp.reload(prat)
                                        break
                                else:
                                    print("\n Wrong Input!!")
                                    print(line)
                                    if speak_mode==1:
                                        pyttsx3.speak("Wrong Input")                    
                       
                      
                        
                        
                        
                        
                        
                        
                        
                        #File ADDER
                        
                        elif Filenuser.lower()=="add file":
                            file_list_n=[]
                            to_control_app_opening=0
                            while True:
                                n_file=input("Display Name :-  ")
                                if len(n_file.split()) == 0:
                                    print("\n No Input")
                                    print(line)
                                    if speak_mode==1:
                                        pyttsx3.speak("No Input")
                                    else:
                                        pass
                                elif n_file=="exit":
                                    break
                                else:
                                    n_file_ext=input("File extention(use '.') :-  ")
                                    
                                    if n_file_ext=="exit":
                                        break
                                    elif len(n_file_ext.split()) == 0 or n_file_ext[0]!=".":
                                        print("\n No Input")
                                        print(line)
                                        if speak_mode==1:
                                            pyttsx3.speak("No Input")
                                    
                                        else:
                                            pass
                                    else:
                                        nic_name_file=[]
                                        n_file_nic=""
                                        while True:
                                            n_file_nic=input("Nick Name :-  ")
                                            n_file_nic=n_file_nic.lower()
                                            if len(n_file_nic.split()) == 0:
                                                print("\n No Input")
                                                print(line)
                                                if speak_mode==1:
                                                    pyttsx3.speak("No Input")
                                                else:
                                                    pass
                                            elif n_file_nic=="exit":
                                                break
                                            else:
                                                nic_name_file.append(n_file_nic)
                                        file_list_n.append(n_file_ext)
                                        file_list_n.append(n_file)
                                        for i in range(len(nic_name_file)):
                                            app_list_n.append(nic_name_file[i])
                                            
                                        with open("prat.py","a+") as file_O:
                                            file_O.seek(0)
                                            file_list="'"+"','".join(file_list_n)+"'"       
                                                                       #bvcahgddjvkcvhdvsachkjshavdjc 
                                            file_O.write("\n")
                                            file_O.write("x_1 = ["+file_list+"]")
                                            file_O.write("\n")
                                            file_O.write("file_list_fin.append(x_1)")
                                            file_O.write("\n")
                                            imp.reload(prat)
                                            to_control_understanding=0
                                            print("\n"+line+"\n")
                                            print(n_file+" Added successfully !!")
                                            print(line)
                                            if speak_mode==1:
                                                pyttsx3.speak(n_file+" Added successfully")
                                            break                  
              
            
            
            
            
                        
                        #For CREATING files
                        
                        elif Filenuser.isnumeric():
                            Filenuser=int(Filenuser)
                            u = Filenuser - 1
                            if u in range(0,len(file_types)):
                                
                                ext=file_types[u][0]
                                name=input("Please enter file name:- ")
                                name='"'+name
                                ext=ext+'"'
                                file_creater()
                                print("\n "+line+" \n" )
                                print(" - file created successfully.")
                                if speak_mode==1:
                                    pyttsx3.speak("file created successfully.")
                                    
                                print("\n")
                                open_file=input("want to open created file (y/n) : ")
                                if open_file=="y":
                                    file_opener()
                                    
                                    
           
        
        
        
                        
                        else :
                           
                            for u in range(0,len(file_types)):
                            
                                if Filenuser.lower() in file_types[u] :
                                    ext=file_types[u][0]
                                    name=input("Please enter file name:- ")
                                    name='"'+name
                                    ext=ext+'"'
                                    file_creater()
                                    print(" - file created successfully.")
                                    if speak_mode==1:
                                        pyttsx3.speak("file created successfully.")
                                    
                                    print("\n")
                                    open_file=input("want to open created file (y/n) : ")
                                    if open_file=="y":
                                        file_opener()
                                    break
    
    

                            else:
                                    name, ext = os.path.splitext(Filenuser)
                                    if name=="":
                                        print(" - no file name recorded... ")
                                    elif ext=="":
                                        while True:
                                            ext=input("extentiom: ")
                                            
                                            if "." in ext:
                                                file_creater()
                                                time.sleep(0.2)
                                                print(" - file created successfully.")
                                                if speak_mode==1:
                                                    pyttsx3.speak("file created successfully.")
                                               
                                                break
                                            if ext=='back()':
                                                break
                                             
                                            else:
                                                
                                                print(" - Incorrect extention \n")
                                                print("FOR GOING BACK PLEASE TYPE 'back()'")
                                                
                                    elif name!="" and ext!="" and "." in ext:
                                        file_creater()
                                        time.sleep(0.2)
                                        print(" - file created successfully.")
                                        if speak_mode==1:
                                            pyttsx3.speak("file created successfully.")
                                            
                                        
                                    else:
                                        print(" - Some Eror Occurred Pls try onece more")
                                        if speak_mode==1:
                                            pyttsx3.speak(print("Some Eror Occurred Pls try onece more"))
                                        break
                                    
        
    


    elif to_control==1 and to_control_app_opening==1:

        for h in sentece_postm:
            if (h in negative_comment) and h not in speak_turn_off :
                print(negative_comment_speach)
                if speak_mode==1:
                    pyttsx3.speak(negative_comment_speach)
                break
            if (h in negative_comment) and (h in speak_turn_off):
                break



        if to_control==1 and to_control_understanding==1:
                
                
                if req_2.isnumeric():
                    req_2=int(req_2)
                   
                if req_2 in range(0,len(x)):
                    row=req_2
                    
                    
                else:
                    for r in range(0,len(x)):
                        for d in x[r]:
                            if d in req_1:
                                row=r
    
                                break
    
    
    
    
    
                            else:
                                pass

                if row ==0 and to_control_understanding==1:
                    print("Unable to understand")
                    if speak_mode==1 and voice_control==0:
                        pyttsx3.speak("Unable to understand")
                else:
                    app_name=x[row][0]
                    open_app()
                    if platform.system()=="Windows":
                        app_name1=x[row][1]
                    else:
                        app_name1=x[row][0]
                    print(" - Command for opening "+app_name1+". given successfully")

                    if speak_mode==1:
                        pyttsx3.speak("Command for opening "+app_name1+". given successfully")



                

