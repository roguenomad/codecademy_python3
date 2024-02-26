# Use the Force

# Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.

train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def get_force(mass, acceleration):
  return mass * acceleration

# Test get_force by calling it with the variables train_mass and train_acceleration.

train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force.

print("The GE train supplies " + str(train_force) + " Newtons of force")

# Define a function called get_energy that takes in mass and c.

# c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

# get_energy should return mass multiplied by c squared.

def get_energy(mass, c=3*10**8):
  return mass * (c**2)

# Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.

bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

# Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")


# Define a final function called get_work that takes in mass, acceleration, and distance.

# Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.

def get_work(mass, acceleration, distance):
  get_force = mass * acceleration
  return get_force * distance


# Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.

train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

# Print the string "The GE train does X Joules of work over Y meters.", with X replaced with train_work and Y replaced with train_distance.

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")

# Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.

# It should then return c_temp.

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)


# Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.

# It should then return f_temp.

def c_to_f(c_temp):
  return c_temp * (9/5) + 32

c0_in_fehrenheit = c_to_f(0)
print(c0_in_fehrenheit)