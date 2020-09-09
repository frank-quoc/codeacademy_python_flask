def grd_ship_cost(weight, premium=False):
  flat_charge = 20.00
  premium_grd = 125.00

  if premium == True:
    return premium_grd
  if weight <= 2:
    price_lb = weight * 1.50 
  elif weight <= 6:
    price_lb = weight * 3.00
  elif weight <= 10:
    price_lb = weight * 4.00
  else:
    price_lb = weight * 4.75
  return flat_charge + price_lb

print(grd_ship_cost(8.4))

def drone_ship(weight):
  if weight <= 2:
    price_lb = weight * 4.50 
  elif weight <= 6:
    price_lb = weight * 9.00
  elif weight <= 10:
    price_lb = weight * 12.00
  else:
    price_lb = weight * 14.25
  return price_lb

print(drone_ship(1.5))

def cheapest_ship(weight):
  prem = grd_ship_cost(weight, premium=True)
  stand = grd_ship_cost(weight)
  drone = drone_ship(weight)

  min_val = min(prem, stand, drone)

  if min_val == prem:
    print("Premium:", prem)
  elif min_val == stand:
    print("Standard:", stand)
  elif min_val == drone:
    print("Drone:", drone)

cheapest_ship(4.8)
cheapest_ship(41.5)
