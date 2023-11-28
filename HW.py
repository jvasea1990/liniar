SCALE  = 15

hX =6
hY = 5


map = "" 
for y in range(1,SCALE+1):
    map += str(y) + ". "
    for x in range(1, SCALE+1):

        if x == 1 or x == SCALE or y == 1 or y == SCALE:
            map += "# "

        elif x == hX and y == hY:
            map += "H "  
        elif y==hY and hX+2>=x>=hX-2:
            map+="X "
        elif y==hY+1 and hX+1>=x>=hX-1:
            map+="X "
        elif y==hY-1 and hX+1>=x>=hX-1:
            map+="X "  
        else:
            map += "  "

    map += "\n"                

print(map)