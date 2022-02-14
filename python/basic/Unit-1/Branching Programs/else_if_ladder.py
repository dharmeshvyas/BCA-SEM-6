prefix="Machine : ";

while(1):
    msg = input("You : ");
    if(msg=="bye"):
        print(prefix,"Bye, have a good day.");
        break
    else:
        
        if(msg!=""):
            
            if(msg=="Hello" or msg=="hii"):
                print(prefix,"Hello there , how can i help you?");
            elif(msg=="how are you?"):
                print(prefix,"i'm good ,what about you?");
            elif(msg=="as"):
                print(prefix,"hihi");
            elif(msg=="jokes"):
                print(prefix,"LOL");
            elif(msg=="how are you?"):
                print(prefix,"i'm good ,what about you?");
            elif(msg=="how are you?"):
                print(prefix,"i'm good ,what about you?");
            else:
                print(prefix,"Invalid command for me.");
        else:
            print(prefix,"There no command for me. Please enter text.");
        
