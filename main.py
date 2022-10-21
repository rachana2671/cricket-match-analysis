
from random import*
from tkinter import*
from tkinter import ttk #for scrollbar


root=Tk()
root.title("Cricket Match Analysis")
#root.geometry("500x400")


#Create a main frame

main_frame=Frame(root)
main_frame.pack(fill=BOTH,expand=1)

#canvas
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

#scroll bar
my_sb=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_sb.pack(side=RIGHT,fill=Y)


#Configure the canvas
my_canvas.configure(yscrollcommand=my_sb.set)
my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#create another frame
sec_frame=Frame(my_canvas)

#add that new frame to a window in the canvas
my_canvas.create_window((0,0),window=sec_frame)






l1=Label(sec_frame,text="Cricket Match Analysis",font=("Helvetica",25))
l1.grid(column=1)
l2=Label(sec_frame,text="Match analysed:New Zealand vs South Africa",font=("Times New Roman",15)).grid(row=1, column=1)
l3=Label(sec_frame,text="Match type: T20\n Venue:New Wanderers Stadium,Johannesberg\n Toss:Won by New Zealand. Elected to bowl\n outcome:New Zealand won by 5 wickets",bd=1,relief="sunken").grid(row=2, column=1)
l4=Label(sec_frame,text="Choose one option from the drop down given below", font="Times 15 bold")
l4.grid(row=3,column=0)




def myclick():
       #reading from a file
      main_frame=Frame(root)
      main_frame.pack(fill=BOTH,expand=1)

#canvas
      my_canvas=Canvas(main_frame)
      my_canvas.pack(side=LEFT,fill=BOTH,expand=1)


      my_sb=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
      my_sb.pack(side=RIGHT,fill=Y)


#Configure the canvas
      my_canvas.configure(yscrollcommand=my_sb.set)
      my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#create another frame
      sec_frame=Frame(my_canvas)
 
#add that new frame to a window in the canvas
      my_canvas.create_window((0,0),window=sec_frame)

      f=open("matchdata1.txt","r")




      track=[]
      for t,l in enumerate(f):
          if "total" in l:
              rdln=l.strip()
              track.append(rdln[-1])
      l=[]
      for i in track:
          l.append(int(i))




      #storing when wickets fall

      runs=0
      wickets=[]
      for j in range(len(l)): 
          if l[j]!=7:
             runs=runs+l[j]
          else:     
         
             wickets.append(runs)
      #printing wickets fall 


      framew=Frame(sec_frame,width=100,height=100)
      framew.grid() 
      lab1 = Label(framew,text="Fall of wickets(by runs)",font="Times 15 bold")
      lab1.grid()
      lab2=Label(framew,text=wickets,font="Times 12",bd=1,relief="sunken").grid()


      #storing partnerships and max partnership 

      p=[]
      for k in range(len(wickets)):
          if k==0:
             p.append(wickets[0])
          else:
             p.append(wickets[k]-wickets[k-1])
      #printing partnerships 
      listp=[]
      lb=Label(framew,text="Partnerships ",font="Times 15 bold").grid()
      for i in range(len(p)):
          s="wicket "+str(i+1)+" partnership is "+str(p[i])
          listp.append(s)

      lb=Label(sec_frame,text="\n".join(listp)).grid()
   
    
    


      #printing highest partnership 
      var2=max(p)
      frame2 = Frame(sec_frame, width=100, height=100)
      frame2.grid()
      lab3 = Label(frame2,text="Highest Partnership is "+str(var2),font="Times 10 bold").grid()


      # balls 

      lab4=Label(frame2,text="Total number of balls bowled is 117",font="Times 15 bold").grid()
      dot=0
      for i in l:
          if i==0:
             dot=dot+1
      lab5=Label(frame2,text="Number of dot balls "+str(dot),font="Times 15 bold").grid()

      #no of 4s and sixes in partnership 
      f=[]
      s=[]
      four=0
      six=0
      for i in l:
    
          if i!=7:
             if i==4:
                four=four+1
             if i==6:
                six=six+1
          else:
             f.append(four)
             s.append(six)
          four=0
          six=0



 
      lab6=Label(frame2,text="Number of fours ",font="Times 15 bold").grid()

      for k in range(10):

    
           l=Label(frame2,text="in partnership "+str(k+1)+" ="+str(f[k])).grid()
  

      lab7=Label(frame2,text="Number of sixes ",font="Times 15 bold").grid()
      for k in range(10):
          l1=Label(frame2,text="in partnership "+str(k+1)+"= "+str(f[k])).grid()
    




      #reading from a file 
      f=open("matchdata1.txt","r")



      track1=[]
      for a,b in enumerate(f):
          if "player_out" in b:
              rdln1=b.strip()
              track1.append(rdln1[11:])
      lb3=Label(frame2,text="Fall of wickets(players)",font="Times 15 bold").grid()        
      lb4=Label(frame2,text=track1,bd=1,relief="sunken").grid()

      f=open("matchdata1.txt","r")
      lines=f.readlines()

      indi=[]
      for j in range(len(track1)):
          p1=[]
          for i in range(len(lines)):
        
              if "batsman" in lines[i].strip():
            
                   if track1[j] in lines[i].strip():
                      r=lines[i+4].strip()
                
                      p1.append(int(r[-1]))
          indi.append(p1)
#print(indi)

      listl=[]
      t=0
      for i in indi:
          t+=1
          c=s=0
          for j in i:
        
              if j==4:
                 c=c+1
              if j==6:
                 s=s+1
    #print("player "+str(j)+": "c," ",s)
          p="player "+str(t)+": "+str(c)+" four(s) "+str(s)+" six(es)"
          listl.append(p)

      lb=Label(frame2,text="\n".join(listl)).grid()
   
def myclick2():
    
      main_frame=Frame(root)
      main_frame.pack(fill=BOTH,expand=1)

#canvas
      my_canvas=Canvas(main_frame)
      my_canvas.pack(side=LEFT,fill=BOTH,expand=1)


      my_sb=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
      my_sb.pack(side=RIGHT,fill=Y)


#Configure the canvas
      my_canvas.configure(yscrollcommand=my_sb.set)
      my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#create another frame
      sec_frame=Frame(my_canvas)
 
#add that new frame to a window in the canvas
      my_canvas.create_window((0,0),window=sec_frame)

       #reading from a file 
      f=open("matchdata22.txt","r")




      track=[]
      for t,l in enumerate(f):
          if "total" in l:
              rdln=l.strip()
              track.append(rdln[-1])
      l=[]
      for i in track:
          l.append(int(i))




      #storing when wickets fall

      runs=0
      wickets=[]
      for j in range(len(l)): 
          if l[j]!=7:
             runs=runs+l[j]
          else:     
         
             wickets.append(runs)
      #printing wickets fall 


      framew=Frame(sec_frame,width=100,height=100)
      framew.grid() 
      lab1 = Label(framew,text="Fall of wickets(by runs)",font="Times 15 bold")
      lab1.grid()
      lab2=Label(framew,text=wickets,font="Times 12",bd=1,relief="sunken").grid()


      #storing partnerships and max partnership 

      p=[]
      for k in range(len(wickets)):
          if k==0:
             p.append(wickets[0])
          else:
             p.append(wickets[k]-wickets[k-1])
      #printing partnerships 
      listp=[]
      lb=Label(framew,text="Partnerships ",font="Times 15 bold").grid()
      for i in range(len(p)):
          s="wicket "+str(i+1)+" partnership is "+str(p[i])
          listp.append(s)

      lb=Label(sec_frame,text="\n".join(listp)).grid()
   
    
    


      #printing highest partnership 
      var2=max(p)
      frame2 = Frame(sec_frame, width=100, height=100)
      frame2.grid()
      lab3 = Label(frame2,text="Highest Partnership is "+str(var2),font="Times 10 bold").grid()


      # balls 

      lab4=Label(frame2,text="Total number of balls bowled is 106",font="Times 15 bold").grid()
      dot=0
      for i in l:
          if i==0:
             dot=dot+1
      lab5=Label(frame2,text="Number of dot balls "+str(dot),font="Times 15 bold").grid()

      #no of 4s and sixes in partnership 
      f=[]
      s=[]
      four=0
      six=0
      for i in l:
    
          if i!=7:
             if i==4:
                four=four+1
             if i==6:
                six=six+1
          else:
             f.append(four)
             s.append(six)
          four=0
          six=0



 
      lab6=Label(frame2,text="Number of fours ",font="Times 15 bold").grid()

      for k in range(len(wickets)):

    
           l=Label(frame2,text="in partnership "+str(k+1)+" ="+str(f[k])).grid()
  

      lab7=Label(frame2,text="Number of sixes ",font="Times 15 bold").grid()
      for k in range(len(wickets)):
          l1=Label(frame2,text="in partnership "+str(k+1)+"= "+str(f[k])).grid()
    




      #reading from a file 
      f=open("matchdata1.txt","r")



      track1=[]
      for a,b in enumerate(f):
          if "player_out" in b:
              rdln1=b.strip()
              track1.append(rdln1[11:])
      lb3=Label(frame2,text="Fall of wickets(players)",font="Times 15 bold").grid()        
      lb4=Label(frame2,text=track1,bd=1,relief="sunken").grid()

      f=open("matchdata1.txt","r")
      lines=f.readlines()

      indi=[]
      for j in range(len(track1)):
          p1=[]
          for i in range(len(lines)):
        
              if "batsman" in lines[i].strip():
            
                   if track1[j] in lines[i].strip():
                      r=lines[i+4].strip()
                
                      p1.append(int(r[-1]))
          indi.append(p1)
#print(indi)

      listl=[]
      t=0
      for i in indi:
          t+=1
          c=s=0
          for j in i:
        
              if j==4:
                 c=c+1
              if j==6:
                 s=s+1
    #print("player "+str(j)+": "c," ",s)
          p="player "+str(t)+": "+str(c)+" four(s) "+str(s)+" six(es)"
          listl.append(p)

      lb=Label(frame2,text="\n".join(listl)).grid()




check1=Button(sec_frame,text="innings 1 (SA BATTING)",command=myclick)
check1.grid(row=4,padx=50)
check2=Button(sec_frame,text="innings 2 (NEW ZEALAND)",command=myclick2).grid(row=5,padx=50)



    


    
        




  
    


    
        

    
 

    
        

    
        
