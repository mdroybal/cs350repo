class Talker:

    def __init__(self,n,v):
        self.name = n
        self.vocab = v
 
    def getname(self):
        return self.name

    def getvocab(self,text):
        l = (hash(text) % len(self.vocab))
        return self.vocab[l]


responses = ["I want to build the wall", "People are going to pour into our country.", "People are going to come in from Syria.", "No puppet. You're the puppet.", "Let me tell you, Putin has outsmarted her and Obama at every single step of the way.", "Wrong.", "I have 200 generals and admirals, 21 endorsing me. 21 congressional medal of honor recipients.", " Her tax plan is a disaster.", " Such a nasty woman."]

responses1 = ["I find that just astonishing","We will have secure borders.", " He would rather believe Vladimir Putin than the military and civilian intelligence professionals who are sworn to protect us.", "I wonder when he thought America was great.", "You know, I've been privileged to see the presidency up close, and I know the awesome responsibility of protecting our country and the incredible opportunity of working to try to make life better for all of you.", "I hope you will give me a chance to serve as your president.", "I do not add a penny to the national debt.", "I take that very seriously because I do think it's one of the issues we've got to come to grips with.", "Well you should ask Bernie Sanders who he is supporting for President.", "And he said you are the most dangerous person to run for president in the modern history of America"]

while True:

    text = raw_input("Please ask a question: ")
    choose = int(raw_input("Please enter (1) for Trump to answer or (2) for Hillary to answer: "))
    
    if choose == 1:
         donald = Talker("Trump: ", responses)
         print donald.getname(), donald.getvocab(text)
     
    elif choose == 2:
         hillary = Talker("Clinton: ", responses1)
         print hillary.getname(), hillary.getvocab(text)

    else:
       print("Invalid number!!!") 
       break
        
   
    
   



    
    

    





    
