#  > - <  I P O R T S  > - <  #


import random as rdm 


#  > - <  F O N C T I O N S  > - <  #


def basic_roll(max : int):
    '''Dice roll / probabilities equals for each values
    > Return a number upper than 0 and lower or equal than the "max"'''
    nbr = rdm.randint(0, max)
    return nbr

def Katsu_roll(cmd : str):
    '''100 roll with bonus and malus
    > Return a number upper than 0 and lower or equal than 100 with malus or bonus'''
    command = []
    cmd_size = len(cmd) - 1
    
    # cmd spliting in command
    for elt in cmd:
        if elt.isdigit():
            command.append(int(elt))
            
        else:
            if elt in ["d", "+", "-"]:
                if elt != "d":
                    if "d" not in command:
                        return f'CommandError : "{elt}"'
                    
                    else:
                        command.append(elt)
                    
                else:
                    if "d" not in command:
                        command.append(elt)
                    
                    else:
                        return f'CommandError : "{elt}"'
                
            elif elt == " ":
                break
            
            else:
                return f'CommandError : "{elt}"'
            
    # split assembling
    if "d" not in command:
        return f'CommandError : "d" is required tu use this roll'
    
    else:
        i = command.index("d")
        
        # first assembling (rolls number)
        if i > 0:
            first = ""
            for elt in command[0 : i - 1]:
                first += str(elt)
                
            first = int(first)
            
        else:
            first = 1
        
        # roll check (if number after "d" is 100)
        size = ""
        if cmd_size >= i + 3:
            for elt in command[i + 1 : i + 3]:
                if type(elt) is int:
                    size += str(elt)
                    
                else:
                    return f'CommandError : invalide dice size, size must be "100"'
              
            if int(size) != 100:
                return f'CommandError : invalide dice size, size must be "100"'
            
        elif cmd_size > i + 3:
                if type(command[i + 4]) is int:
                    return f'CommandError : invalide dice size, size must be "100"'
                 
        else:
            return f'CommandError : invalide dice size, size must be "100"'
            
        # bonus assembling (with "+" and "-")
        def bonus_check(bns : list, i : int): # return the bonus value (without use "+" or "-")
            bonus = ""
            for elt in command[i + 1 : len(command) - 1]:
                if type(elt) is int:
                    bonus += str(elt)
                
            return int(bonus)
                
        bonus = 0        
        if len(command) - 1 > i + 4:
            i += 4
            bonus_index = []
            for i in range(len(command)):
                if command[i] in ["+", "-"] and type(command[i + 1]) is int:
                    bonus_index.append(i)
            
            for idx in bonus_index:
                if command[idx] == "+":
                    bonus += bonus_check(command, idx)
                    
            else:
                if command[idx] == "-":
                    bonus -= bonus_check(command, idx)
        
        # final command (assembled)
        command = [first, "d", 100, bonus]
        return command
   
# tests     
print(Katsu_roll("d100"))