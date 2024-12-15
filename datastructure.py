# yoruba_dictionary = {wa= 'come',
#                     lo= go
#                     }
# print(yoruba_dictionary)


#
# height = float(input("Enter your height: "))
# age = int(input("Enter your age: "))
#
# if(height > 170):
#     print('welcome')
# elif(age>17):
#     print('welcome')
# else:
#     print('you are not qualified')



# for i in range(3,9,20):
#     print(i)
#
# names = []
# names.append("jonathan")
# names.append("isaac")
# names.append("daniel")
# names.append("laolu")
# names[2] = "laylo"
#
# print(names)
#
# for name in names:
#     if( name == "laylo"):
#         print("i've been looking for you")
#         break;
#     else:
#         print("i'm looking for laylo")

# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# numbers.append(8)
# numbers.pop(6)
#
# sum = 0
#
# for val in numbers:
#     print(val, " + ", sum)
#     sum = sum + val
#
# print("The sum is", sum)
#
# names=["tobi,james,laolu,laylo"]
#
# yoruba_dictionary={"come":"wa",
#                    "go":"lo"}


print("What's your BODY MASS INDEX(BMI)? ")
def calculate_bodymassindex( w,h ):
    print(w/(h*h))
w=float(input("enter your weight:"))
h=float(input("enter your height:"))

calculate_bodymassindex( w,h )

body_mass_index=float(input("enter calcuated body mass index "))


if(float(body_mass_index > 14 and body_mass_index<16)):
    print("you're stunting")

elif(float(body_mass_index > 16 and body_mass_index < 17)):
    print("you're underweight")

elif(float(body_mass_index > 18 and body_mass_index < 25)):
    print("your weight is normal")

elif(float(body_mass_index > 25 and body_mass_index <30)):
    print("you're overweight")

elif(float(body_mass_index > 30 and body_mass_index <35)):
    print("you're obesity grade1")

elif(float(body_mass_index > 35 and body_mass_index<40)):
    print("you're obesity grade2")

else :
    print("your level of obesity is grade3")

