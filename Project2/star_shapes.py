shapenum = 1
while( shapenum != 0 ):
    shapenum = int(input("This program can \n 1) Draw a rectangle. \n 2) Draw an isosceles triangle. \n 3) Draw an octagon. \n Please select a number or 0 to exit: "))
    star = "*"
    
    if(shapenum == 0): #exiting the program option
        print("\nShutting down program. Thank you for using my program.")
        
    elif(shapenum == 1):#wanting to draw a rectangle -- obtain the dimensions
        rect_wid = int(input("How wide should the rectangle be? " ))
        rect_height = int(input("How high should the rectangle be? " ))
        height = 0
        
        while( height < rect_height):
            height += 1
            print(rect_wid * star)
        #Code to create a rectangle with specified dimensions
    
    elif(shapenum == 2):#wanting to draw a triangle
        tri_row_num = int(input("How many levels should there be in the triangle? \n Enter an odd number: "))#FIX THE ODD NUMBER SITUATION
        
        while( tri_row_num % 2 == 0 ):
            tri_row_num = int(input(" Enter an odd number: "))
    
        tri_direc = int(input("Where would you like the triangle to point? \n 1) down \n 2) up \n 3) left \n 4) right \n Please select a number: ")) #choose which side you want the triangle points
        space = " "
        spacenum = 0
        
        if ( tri_direc == 1 ):#Triangle pointing downward
            while( tri_row_num >= 1 ):
                rows = tri_row_num * 2 - 1
                print( spacenum * space , rows * star)
                spacenum += 1
                tri_row_num -= 1

        elif ( tri_direc == 2 ):#Triangle pointing upward
            rows = 1
            
            while( tri_row_num >= 1 ):
                spacenum = tri_row_num - 1
                print( spacenum * space , rows * star)
                rows += 2
                tri_row_num -= 1
                
        elif ( tri_direc == 3 ):#triangle pointing left
            
            rows = 1
            #incorporate the spaces needed
            
            while( tri_row_num > 1):#top half of the triangle
                spacenum = tri_row_num 
                print( spacenum * space , rows * star )
                rows += 1
                tri_row_num -= 1
                
            rows2 = rows
            
            while( tri_row_num <= rows2 ):#bottom half of the triangle
                spacenum = tri_row_num
                print( spacenum * space , rows *star )
                rows -= 1
                tri_row_num += 1
                
        elif( tri_direc == 4 ):#triangle pointing right
            
            rows = 1
                #incorporate the spaces needed
            while(rows <= tri_row_num ): #top half of the triangle
                print( rows * star )
                rows += 1
                
            rows2 = rows - 1
            
            while( rows2 >= 1 ): #bottom half of the triangle
                rows2 -= 1
                print( rows2 *star )
            
    elif(shapenum == 3):#wanting to draw an octogon
        oct_side_length = int(input("How long should each side of the octogon be? ")) #same length on each side
        length = oct_side_length
        row = 1
        spacenum = oct_side_length - 2
        space = " "
        #split octogon drawing into three parts 
        
        while( row < oct_side_length ):#top part othe octogon
            row += 1
            print( (space * spacenum) , length * star )
            spacenum -= 1
            length += 2
            
        row1 = 0#middle part of the octogonil
        while( row1 < oct_side_length ):
            row1 += 1
            print( length * star )
            
        row2 = length - 1 #bottom part of the octogon
        spacenum1 = 0
        
        while( length > oct_side_length ):
            row2 -= 1
            length -= 2
            print( spacenum1 * space , length * star )
            spacenum1 += 1
        #Code to create a octogon with specified side lengths
        
    else:#any number other than one of the options
        print("Not a valid option, please select an appropriate option....")
    
    print()