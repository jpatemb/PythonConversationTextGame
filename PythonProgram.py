import random
from datetime import datetime
import os
import requests


print("Hello, and welcome to my program! This is a test of various python features")
print("First, I will print a list of integers:")

a = [4,5,6,7]
b = {1,2,3}
c = ("bird", 100, False)
c = ("red", 101, True)
print(c)


for(x) in a:
    print(x)

for(y) in b:
    print(b)



def func():
    print("This is a test function to print 'Hello World'")

func()

def game():
    n = random.randint(1, 10)
    count = 1
    guess = int(input("I'm thinking of a number between 1 an 10. Can you guess what number it is? Please note that I will crash and exit if you respond with any letters:"))
    while n != "guess":
        if guess < n:
            print ("Too low")
            count += 1
            guess = int(input("Guess again:"))
        elif guess > n:
            print("Too high")
            count += 1
            guess = int(input("Guess again:"))
        elif guess == n:
            print("Correct! You guessed the number in " + str(count) + " try/tries!")
            response = input("Want to play again? (y for yes, n for no)")
            if response in ('y'):
                print("Ok! Then let's play again!")
                game()
            elif response in ('n'):
                print("Alright, on to something else then.\n")
                break
            else:
                guess = int(input("That's not a number.(Please enter y for yes, or n for no"))
                continue
            break
        else:
            print("Invalid input!")
            guess = int(input("Please enter an integer number betwen 1 and 10:"))

answer = input("Now I would like to play a game. How about you? (y for yes, n for no)")
while answer != ('y', 'n'):
    if answer in ('y'):
        print("Wonderful! Then let's play!\n")
        game()
    elif answer in ('n'):
        print("Alright.\n")
        break
    else:
        print("Come again?")
        answer = input("Please enter y for yes, or n for no")
        continue
    break

name = input(str("So, what is your name?"))
print("Hello there " + name + "! Sorry I never introduced myself earlier. I am Reggie!\n")

mood = input(str("How are you today? (type 'g' for good or 'b' for bad):"))
while mood != ('g', 'b'):
    if mood in ('g'):
        print("That's nice to know " + name + "! I'm doing good myself.\n")
        break
    elif mood in ('b'):
        print("Sorry to know that " + name + ". I hope you feel better.\n")
        break
    else:
        print("Come again?")
        mood = input(str("(type 'g' for good or 'b' for bad):"))

date_time = input(str("Would you like to know the date and time? (y for yes, n for no):"))
while date_time != ('y', 'n'):
    if date_time in ('y'):
        now = datetime.now()
        print("Ok then!")
        print("The current date is:")
        print(now.strftime("%m-%d-%Y"))
        print("The current time is:")
        print(now.strftime("%H:%M:%S\n"))
        break
    elif date_time in ('n'):
        print("Okie dokie.\n")
        break
    else:
        print("Come again?")
        date_time = input(str("(y for yes, n for no):"))


#pasted from OpenWeather website: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
      
weather = input(str("Would you like to know the weather? (y for yes, n for no):"))
while weather!= ('y', 'n'):
    if weather in ('y'):
        user_api = os.environ['current_weather_data']
        location = input(str("Enter a City name: "))
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        if api_data['cod'] == '404':
            print("Hmm, never heard of that City, and believe me, I've been around. Maybe another City? (Invalid City: '{}'. Please check your City name):".format(location))
            continue
        else:
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            w_date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        #print(api_data)
        print("----------------------------------------------------------------------")
        print("Ok then! Here is the current weather for {} || {}:".format(location.upper(), w_date_time))
        print("----------------------------------------------------------------------")

        print("Temperature: {:.2f} deg C".format(temp_city))
        print("Description: ", weather_desc)
        print("Humidity: ", hmdt, '%')
        print("Wind Speed: ", wind_spd, 'kmph')
        break
    elif weather in ('n'):
        print("Alright then, nevermind.\n")
        break
    else:
        print("Come again?")
        weather = input(str("(y for yes, n for no):"))
        continue
        
print("Well, it was a pleasure speaking with you ", name, ". Have a great day!")