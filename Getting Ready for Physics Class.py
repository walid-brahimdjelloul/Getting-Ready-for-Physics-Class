train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3 * (10**8)

# Write your code below: 
      ## Turn up the Temperature
## Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
def f_to_c(f_temp):
  eq = (f_temp - 32) * (5/9)
  return eq

f100_in_celsius = f_to_c(100)

## Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit
def c_to_f(c_temp):
  eq = c_temp * (9/5) + 32
  return eq

c0_in_fahrenheit = c_to_f(0)

        ## Use the Force
        #1 get force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies "+str(train_force)+" Newtons of force.")
        ## 2 get energy
def get_energy(mass, c):
  return mass * c**2
bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies "+str(bomb_energy)+" Joules")

        ## Do the Work
def get_work(mass, acceleration, distance):
  eq = get_force(mass, acceleration) * distance
  return eq

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does "+str(train_work)+ " Joules of work over "+ str(train_distance)+ " train_distance")
