import os
import platform

try:
    import pyttsx3
except ModuleNotFoundError:
    os.system("pip install pyttsx3")
    import pyttsx3

print("WHAT DOES THIS PROGRAM DO: \n \n 1)  YOU CAN OPEN APPLICATIONS : TO add more application just make [] seperated via couma and first add orignal app name in string and than the what would you will type to open the app in another string all strings should seperated by couma")
print("\n YOU CAN GO TO FINDER by typing 'go to finder' : there are lots of thigs to do")
print("YOU CAN TURN ON OR OFF SPEAKING OF YOUR DEVICE BY TYPING NEGATIVE WORD LIKE 'not,never,etc'  and on by typing 'now speak, do speak'")







print("This specially made for mac users  \n You can open all apps which mac have. \n and programe is written in mac")
print("\n This Programme is optimise for all types of os (Mac ,Windows) ")
#pyttsx3.speak("this programme specially made for mac users . and .programme is written in mac .And This Programme is optimise for all types of Operating System .(Mac ,Windows). ")
pyttsx3.speak("User please Enter Your Name ")
name_user=input("Enter Your Name :- ")
pyttsx3.speak("Hello "+name_user +"! I am Darwin your virtual assistant How can I help you ")


speak_mode = 1

#about program

negative_comment_speach = "It's a negative comment so i can't proceed."
exit_speach = "you exited successfully"
negative_comment = ["dont",'not to','not',"don't",'never do this', 'never do' , "never" , "turn off"]
positive_comment= ["do","now","start"]


speak_turn_off= "speak voice"
speak_turn_off= speak_turn_off.split()




app_name=""


# FOR WINDOWS


if platform.system() == "Windows":
    print("you are operating this program on windows.....")
    pyttsx3.speak("you are operating this program on windows.....")
    
    pyttsx3.speak("This program is mainly made for Mac (OS)! but optimized also for windows! There are some chances that some function may not work in windows")

    x = [[""],["control","setting","settings","control","love to change things"],["Anaconda Navigator", "anaconda","Anaconda-Navigator","conda","Navigator"],["MsEdge", "Microsoft Edge","edge","edge browser","micrisoft browser"],["chrome","Google chrome","browser","net surfing in google "],["arcroRd32","acrobat","adobe acrobat"],["creative cloud","creative cloud","adobe cloud",],["illustrartor","Adobe illustrartor","illustrator","illustator","design","designing"," adobe logo maker"],["photoshop","photo shop","Photoeditor","editing"],["Excel","Microsoft Excel","excel","microsoft excel","excel data entry",],["chrome","Google chrome","net surfing in google"],["onenote","Microsoft OneNote","office","mf office",],["powerpnt","Power Point","Presentation","ppt presentation",],["winword","document","word","writing pad"]]


   
    
    
    def show_apps():
        print("\n \n")
        print("THE APPS THAT I CAN OPEN FOR YOU IF IT EXIST: \n")
        for i in range(1,len(x)):
            print(x[i][1])
        print("\n")

    
    def open_app():
        os.system('start ' +app_name)

    def file_creater():
        os.system("touch "+name+ext)
        os.system("dir")

    file_types=[[".txt",'Text File','textfile','text file','Text edit',"1"],[".pptx","Power Point Presentation","ppt","powerpoint","power point" ,"presentation"],[".docx","Microsoft Word","ms word","word","msword","microsoft word"],[".xlsx","Microsoft Excel","excel"]]

    def file_opener():
        df='"'+name+ext+'"'
        os.system("open "+df)
    def uni_f_op():
        z_1=inp_1[1]
        for i in inp_1[2:]:
              z_1+=" "+i
        os.system("open "+z_1)

    def folder_creater():
        folder_n='"'+inp_1[1]+'"'
        os.system("mkdir "+folder_n)

    def rename_file():
        z_1=inp_1[1]
        for i in inp_1[2:]:
              z_1+=" "+i

        if z_1 in os.listdir():
            if speak_mode==1:
                pyttsx3.speak("Enter your files new name: ")
            new_f=input("Enter your files new name: ")
            nnn =' "'+new_f+'"'


            os.system('ren "'+z_1+'"'+nnn)

            print("file renamed successfully.")
            if speak_mode==1:
                pyttsx3.speak("file renamed successfully.")




    def del_files():



        z_1=inp_1[1]
        for i in inp_1[2:]:
              z_1+=" "+i


        if z_1 in os.listdir():

             print(z_1)
             os.system('del f "'+z_1+'"')


             print(z_1+" file deleted successfully.")
             if speak_mode==1:
                pyttsx3.speak(z_1+" file deleted successfully.")
        else:
            print("there is no such file")
            if speak_mode==1:
                pyttsx3.speak("there is no such file.")






#qwertyuiopasdfghjklzxcvbnm






if platform.system() == "Darwin":
    print("you are operating this program on Mac.....")






#for mac

    x = [[""],["Photos","photos,photo"],["Preview","preview"],["Music","music","musics"],["Podcasts","podcasts"],["iMovie","imovie","video editing"],["KeyNote","keynote","presentation"],["Stocks","stocks","stock"],["Xcode","xcode"],["Notes","notes","note","notepad"],["FaceTime","facetime","face time"],["FindMy","find my","findmy"],["Photo Booth","photo booth","photobooth","photos booth","photosbooth"],["Mails","mails","emails"],["Contacts","contacts","contact"],["Whatsapp","whatsapp"],["Calender","calender","calanders"],["Reminders","reminders","reminder"],["Numbers","spreadsheet","numbers"],["Messages","messages","message"],["Maps","maps","navigate"],["TV","tv","apple tv","appletv"],["GarageBand","garageband","garage band","music mixer","music editor"],["Voice Memos","voice memos","sound secorder","recorder"],["Anac onda-Navigator", "anaconda","jupiter","Navigator","spyder"], ["App Store", "app store","applications","store","apps"], ["atom", "code in atom","coding in atom","lets code in atom","atom ide"],["Google chrome","chrome","net surfing in google","google","surf google"],["safari","net surfing","browser","default browser","sarfari browser"]]
    pyttsx3.speak("you are operating this program on Macintosh.....")




    def open_app():
        os.system('open -a "'+app_name+'".app')

    def file_creater():
        os.system("touch "+name+ext)
        os.system("ls")

    file_types=[[".txt",'Text File','textfile','text file','Text edit',"1"],[".txt",'Text File','textfile','text file','Text edit',"1"],[".pages","pages"],[".numbers","Spread Sheet","spread sheet","shhet","number"],[".pptx","Power Point Presentation","ppt","powerpoint","power point" ,"presentation"],[".docx","Microsoft Word","ms word","word","msword","microsoft word"],[".xlsx","Microsoft Excel","excel"]]
    
        
    def show_apps():
        print("\n \n")
        print("THE APPS THAT I CAN OPEN FOR YOU IF IT EXIST: \n")
        for i in range(1,len(x)):
            print(x[i][0])
        print("\n")

    def file_opener():
        df='"'+name+ext+'"'
        os.system("open "+df)
    def uni_f_op():
        z_1=inp_1[1]
        for i in inp_1[2:]:
              z_1+=" "+i
        os.system("open "+z_1)

    def folder_creater():
        folder_n='"'+inp_1[1]+'"'
        os.system("mkdir "+folder_n)

    def rename_file():
        z_1=inp_1[1]
        for i in inp_1[2:]:
              z_1+=" "+i




        if z_1 in os.listdir():
            if speak_mode==1:
                pyttsx3.speak("Enter your files new name: ")
            new_f=input("Enter your files new name: ")
            nnn =' "'+new_f+'"'


            os.system('mv "'+z_1+'"'+nnn)

            print("file renamed successfully.")
            if speak_mode==1:
                pyttsx3.speak("file renamed successfully.")




    def del_files():



        z_1=inp_1[1]
        for i in inp_1[2:]:
              z_1+=" "+i


        if z_1 in os.listdir():

             print(z_1)
             os.system('rm -Rf "'+z_1+'"')


             print(z_1+" file deleted successfully.")
             if speak_mode==1:
                pyttsx3.speak(z_1+" file deleted successfully.")
        else:
            print("there is no such file")
            if speak_mode==1:
                pyttsx3.speak("there is no such file.")







else:
    print("THIS PROGRAM IS NOT MADE FOR YOUR OPERATING SYSTEM")






print(len(x))


show_apps()




while True:

    to_control=1
    to_control_b=1


    requirements = input("enter your choice:- ")
    requirements=requirements.lower()
    req_1 = requirements

    if requirements=="exit()":

        print(exit_speach)
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
                        print("speaking mode turned off successfully")
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
                        print("speaking mode turned on successfully")
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
        print("you are now in finder")
        if speak_mode==1:
            pyttsx3.speak("welcome . , you are now in finder")
        while True :
              print("FOR EXIT : 'exit()' \n FOR OPENING FILE : 'open filename.extention' \n FOR OPENING FOLDER :  'open foldername' \n FOR MAKING FOLDER: make foldername \n FOR CREATING FILE :  create  \n FOR DELETING ANY FILE/FOLDER : 'delete filename/foldername' \n \n")

              if platform.system()=="Windows":
                    ls="ls"
              else:
                    ls = "dir"
              os.system(ls)


              inp_1 = input("what you want to do : ")



              if inp_1=="exit()":

                  print(exit_speach)
                  if speak_mode==1:
                      pyttsx3.speak(exit_speach)
                  break


              inp_1=inp_1.lower()
              inp_1 = inp_1.split()




                  #OPEN FILE/FOLDR
              if "open" in inp_1[0]:

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
                  print("folder made successfully")
                  if speak_mode==1:
                      pyttsx3.speak("folder made successfully")


              elif "show" in inp_1 and "file" in inp_1:
                   os.system("ls")

                #create files
              elif "create" in inp_1:

                    print("""    what type thing you want to create



                          """)


                    while True:
                        for i in range(0,len(file_types)):
                            print((i+1),end=")  "+file_types[i][1])
                        print('\n \n')
                        print("FOR GOING BACK PLEASE TYPE 'back()'")
                        Filenuser=input(""" Please enter which type of file you want if your choice not
    listed plss add extention with name to crate it
    or you can continue without extention: """)
                        if "back()" in Filenuser.lower():
                            break
                        for u in range(0,len(file_types)):
                            if Filenuser.lower() in file_types[u] :
                                ext=file_types[u][0]
                                name=input("Please enter file name:- ")
                                file_creater()
                                print("file crated successfully.")
                                if speak_mode==1:
                                    pyttsx3.speak("file crated successfully.")
                                open_file=input("want to open crated file (y/n) : ")


                                if open_file=="y":
                                    file_opener()
                                break




                        else:
                            name, ext = os.path.splitext(Filenuser)
                            if name=="":
                                print("no file name recorded... ")
                            elif ext=="":
                                while True:
                                    ext=input("extentiom: ")
                                    if "." in ext:
                                        break
                                    if ext=="back()":
                                        break
                                    else:
                                        print("incorrect extention")
                                        print("FOR GOING BACK PLEASE TYPE 'back()'")
                            elif name!="" and ext!="" and "." in ext:
                                file_creater()
                                print("file crated successfully.")
                                if speak_mode==1:
                                    pyttsx3.speak(print("file crated successfully."))
                            else:
                                print("Some Eroor Occurred Pls try one more")
                                if speak_mode==1:
                                    pyttsx3.speak(print("file crated successfully."))









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

                for r in range(0,len(x)):
                    for d in x[r]:
                        if d in req_1:
                            row=r

                            break

                        else:
                            pass

                if row ==0:
                    print("I cant understand")
                    if speak_mode==1:
                        pyttsx3.speak("I can't understand")
                else:
                    app_name=x[row][0]
                    open_app()
                    if platform.system()=="Windows":
                        app_name1=x[row][1]
                    else:
                        app_name1=x[row][0]
                    print("Command for opening "+app_name1+". given successfully")

                    if speak_mode==1:
                        pyttsx3.speak("Command for opening "+app_name1+". given successfully")



                break
