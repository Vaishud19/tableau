'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
nominee1= input("enter the name of 1st nominee here:")
nominee2= input("enter the name of 2nd nominee here:")
#initially vote count for both nominee must be 0
nm1_votes=0
nm2_votes=0

voter_id=[1,2,3,4,5,6,7,8,9,10]
w= len(voter_id)

while True:
    if voter_id==[]:
        print("voting session is over!!")
        if nm1_votes> nm2_votes:
            percent=(nm1_votes/w)*100
            print(nominee1, "has won the election with", percent, "% of votes")
            break
        elif nm2_votes> nm1_votes:
            percent=(nm2_votes/w)*100
            print(nominee2, "has won the election with", percent, "% of votes")
            break    
        else:
            print("both have equal no. of votes!! goverment will decide who will rule")
            break
    voter=int(input("enter your voter id:"))
    if voter in voter_id:
        print("you are a voter")
        #we will remove so that again same voter can't vote)
        voter_id.remove (voter)
        print("-------------------")
        print("to give vote to", nominee1, "press1")
        print("to give vote to", nominee2, "press2")
        print("-------------------")
        vote= int(input("enter your pecious vote:"))
        if vote==1:
            nm1_votes+=1
            print(nominee1, "thanks for vote!!")
        elif vote==2:
            nm2_votes+=1
            print(nominee2, "thanks for vote!!")
        elif vote>2:
            print("check your press key!!")
        else:
            print("you are not a voter or you have already voted")
                
        