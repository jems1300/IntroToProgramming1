def main():
   dist = 15
   mpg = 25
   gas_price = 3

   trips_per_day = int(input("Enter 1 for single way, enter 2 for a round-trip: "))

   if trips_per_day == 1:
       cost_single = dist / mpg * gas_price
       print("Single trip cost: ", cost_single)

   if trips_per_day == 1:
       cost_round = (dist / mpg * gas_price) * 2
       print("Single trip cost: ", cost_round)

   if trips_per_day < 1:
       print("You need to travel more!")


   cost_single = (dist / mpg * gas_price) * 2
   print("Single trip cost: ", cost_single)

   cost_round = (dist / mpg * gas_price) * 2
   print("Round trip cost: ", cost_round)

main()
