weather = input("What's the weather like today? (sunny/rainy/cold):")


if weather == "sunny":
    weather_advice = print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    weather_advice = print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    weather_advice = print("Make sure to wear a warm coat and a scarf.")
else:
    weather_advice = print("Sorry, I don't have recommendations for this weather.")

print(weather_advice)
