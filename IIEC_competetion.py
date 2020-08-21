import os
import platform

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




line = " ___________________________________________________________________ "



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



speak_mode = 1

#about program

negative_comment_speach = "It's a negative comment so i can't proceed."
exit_speach = " - Good bye! "+name_user+"! hope we will meet soon"
negative_comment = ["dont",'not to','not',"don't",'never do this', 'never do' , "never" , "turn off"]
positive_comment= ["do","now","start"]


speak_turn_off= "speak voice"
speak_turn_off= speak_turn_off.split()

def nif():
    print("\n - No input found")
    if speak_mode==1:
            pyttsx3.speak("No input found.")


app_name=""


# FOR WINDOWS
print("\t\t\t\t what can I help you with ?")
print("\t\t\t\t-------------------------------- \n")
pyttsx3.speak("Hello "+name_user +"! I am Darwin your virtual assistant! What can I help you with!")

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
        os.system("dir")

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

    x = [[""],["System Preferences","stting","settings"],["Photos","photos","photo"],["Preview","preview"],["Music","music","musics"],["Podcasts","podcasts"],["iMovie","imovie","video editing"],["KeyNote","keynote","presentation"],["Stocks","stocks","stock"],["Xcode","xcode"],["Notes","notes","note","notepad"],["FaceTime","facetime","face time"],["FindMy","where is iphone","find iphone","find my","findmy"],["Photo Booth","photo booth","photobooth","photos booth","photosbooth"],["Mails","mails","emails"],["Contacts","contacts","contact"],["Whatsapp","whatsapp"],["Calender","calender","calanders"],["Reminders","reminders","reminder"],["Numbers","spreadsheet","numbers"],["Messages","messages","message"],["Maps","maps","navigate"],["TV","tv","apple tv","appletv"],["GarageBand","garageband","garage band","music mixer","music editor"],["Voice Memos","voice memos","sound secorder","recorder"],["Anac onda-Navigator", "anaconda","jupiter","Navigator","spyder"], ["App Store", "app store","applications","store","apps"], ["atom", "code in atom","coding in atom","lets code in atom","atom ide"],["Google chrome","chrome","net surfing in google","google","surf google"],["safari","net surfing","browser","default browser","sarfari browser"]]
    pyttsx3.speak("you are operating this program on Macintosh.....")




    def open_app():
        os.system('open -a "'+app_name+'".app')

    def file_creater():
        os.system("touch "+name+ext)
        os.system("ls")

    file_types=[[".txt",'Text File','textfile','text file','Text edit'],[".pages","pages"],[".numbers","Spread Sheet","spread sheet","shhet","number"],[".pptx","Power Point Presentation","ppt","powerpoint","power point" ,"presentation"],[".docx","Microsoft Word","ms word","word","msword","microsoft word"],[".xlsx","Microsoft Excel","excel"]]
    
        
    def show_apps():
        print("\n \n")
        print("THE APPS THAT I CAN OPEN FOR YOU IF IT EXIST: \n")
        for i in range(1,len(x)):
            q = str(i)
            print(q+") "+x[i][0])
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


while True:
    print("\n "+line+" \n")
    to_control=1
    to_control_b=1

    show_apps()
    print(line+" \n \n")
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
    if speak_mode==1:
        for h in speak_turn_off:
            if h in requirements:
                for k in negative_comment:
                    if k in requirements:
                        speak_mode=0
                        to_control=0
                        to_control_b=0
                        print("\n - speaking mode turned off successfully")
                        break
                    else:
                        pass
            else:
                pass

    elif speak_mode==0:

        for h in speak_turn_off:
            if h in requirements:
                for k in positive_comment:
                    if k in requirements:
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
                if speak_mode==1:
                    to_control=0
                    pyttsx3.speak(negative_comment_speach)

                break
            if (h in negative_comment) and (h in speak_turn_off):
                break




            # file creater

    if "show" in requirements and "app" in requirements:
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


              inp_1=inp_1.lower()
              inp_1 = inp_1.split()


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
                    print("\n "+line)
                    print("""  \n \n  what type thing you want to create

                          """)


                    while True:
                        for i in range(0,len(file_types)):
                            print((i+1),end=")  "+file_types[i][1]+"\n")
                        print("\n \n "+line)
                        print('\n \n')
                        print("FOR GOING BACK PLEASE TYPE 'back()'")
                        print(""" Please enter which type of file you want if your choice not \n listed plss add extention with name to crate it \n or you can continue without extention. """)
                        print("\n "+line+" \n")
                        Filenuser = input("Your choice please :- ")
                        print("\n "+line+" \n")
                        
                        if "back()" in Filenuser.lower():
                            break
                        
                        
                        
                        
                        #For CREATING files
                        
                        if Filenuser.isnumeric():
                            Filenuser=int(Filenuser)
                            u = Filenuser - 1
                            if u in range(0,len(file_types)):
                                
                                ext=file_types[u][0]
                                name=input("Please enter file name:- ")
                                name='"'+name
                                ext=ext+'"'
                                file_creater()
                                print("\n "+line+" \n" )
                                print(" - file crated successfully.")
                                if speak_mode==1:
                                    pyttsx3.speak("file crated successfully.")
                                    
                                print("\n")
                                open_file=input("want to open crated file (y/n) : ")
                                if open_file=="y":
                                    file_opener()
                                break
                                    
                                    
                        
                        else:
                           
                            for u in range(0,len(file_types)):
                            
                                if Filenuser.lower() in file_types[u] :
                                    ext=file_types[u][0]
                                    name=input("Please enter file name:- ")
                                    name='"'+name
                                    ext=ext+'"'
                                    file_creater()
                                    print(" - file crated successfully.")
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
                                            if "."==ext:
                                                print(" - wrong input recorded")
                                            elif "." in ext:
                                                file_creater()
                                                print(" - file created successfully.")
                                                if speak_mode==1:
                                                    pyttsx3.speak(print("file created successfully."))
                                               
                                                break
                                            if ext=='back()':
                                                break
                                             
                                            else:
                                                
                                                print(" - Incorrect extention \n")
                                                print("FOR GOING BACK PLEASE TYPE 'back()'")
                                    elif name!="" and ext!="" and "." in ext:
                                        file_creater()
                                        print(" - file created successfully.")
                                        if speak_mode==1:
                                            pyttsx3.speak(print("file created successfully."))
                                        break
                                    else:
                                        print(" - Some Eroor Occurred Pls try onece more")
                                        if speak_mode==1:
                                            pyttsx3.speak(print("Some Eroor Occurred Pls try onece more"))
                                        break
                                    break
        
    


    elif to_control==1:

        for h in sentece_postm:
            if (h in negative_comment) and h not in speak_turn_off :
                print(negative_comment_speach)
                if speak_mode==1:
                    pyttsx3.speak(negative_comment_speach)
                break
            if (h in negative_comment) and (h in speak_turn_off):
                break



            else:
                
                
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

                if row ==0:
                    print("Unable to understand")
                    if speak_mode==1:
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



                break
