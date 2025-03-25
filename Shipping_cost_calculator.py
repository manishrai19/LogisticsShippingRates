#Shipping cost calculator

#Input Package weight and Shipping rate

weight= float(input("Enter the weight in kgs: "))
rate =  float(input("Enter the rate per KGs in USD : "))

shipping_cost = weight * rate

print(f"The shipping cost for the item is {shipping_cost} USD")
