# check for equilateral,scalene or isosclees triangle

len1= int(input("Enter lenght one of the triangle"))
len2= int(input("Enter lenght two on the triangle"))
len3= int(input("Enter lenght three on the triangle"))

if(len1==len2 and len2==len3 and len3==len1):
    {
    print("Traingle is equilateral triangle")

}
elif(len1==len2 or len2==len3 or len3==len1):
    {
        print("Traingle is isosceles triangle")
    }

else:
    print("Traingle is  scalene triangle")