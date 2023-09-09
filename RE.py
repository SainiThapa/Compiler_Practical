#Define a DFA {a,b} that accepts RE (ab*a)

transition_table={
    0:{'a':1,'b':3},
    1:{'a':2,'b':1},
    2:{'a':3,'b':3},
    3:{'a':3,'b':3}
}
#Function to simulate DFA
def is_accepted(inp_string):
    current_state=0

    for symbol in inp_string:
        if symbol not in transition_table[current_state]:
            return False
        current_state=transition_table[current_state][symbol]
    if(current_state==2):
        return True
    else:
        return False
#main Driver
if __name__ == "__main__":

    input_string=input("Enter a string {a,b} : " )
    a=is_accepted(input_string)
    if(a==True):
        print("Accepted")
    else:
        print("Rejected")