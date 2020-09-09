# Getting Ready for Physics Class
You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.

## Tasks

### Turn up the Temperature

1. Write a function called ```f_to_c``` that takes an input ```f_temp```, a temperature in Fahrenheit, and converts it to ```c_temp```, that temperature in Celsius.<br />
<br />It should then return ```c_temp```.<br />
<br />The equation you should use is: ```Temp (C) = (Temp (F) - 32) * 5/9```

2. Let’s test your function with a value of 100 Fahrenheit.
<br />Define a variable ```f100_in_celsius``` and set it equal to the value of ```f_to_c``` with ```100``` as an input.<br />

3. Write a function called ```c_to_f``` that takes an input ```c_temp```, a temperature in Celsius, and converts it to ```f_temp```, that temperature in Fahrenheit.
<br />It should then return ```f_temp```.<br />
<br />The equation you should use is:<br />
<br />```Temp (F) = Temp (C) * (9/5) + 32```<br />

4. Let’s test your function with a value of 0 Celsius.
<br />Define a variable ```c0_in_fahrenheit``` and set it equal to the value of ```c_to_f``` with ```0``` as an input.<br />

### Use the Force

5. Define a function called ```get_force``` that takes in ```mass``` and ```acceleration```. It should return ```mass``` multiplied by ```acceleration```.

6. Test ```get_force``` by calling it with the variables ```train_mass``` and ```train_acceleration```.
<br />Save the result to a variable called ```train_force``` and print it out.<br />

7. Print the string “The GE train supplies ```X``` Newtons of force.”, with X replaced by ```train_force```.

8. Define a function called ```get_energy``` that takes in ```mass``` and ```c```.
<br />```c``` is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set ```c``` to have a default value of ```3*10**8```.<br />
<br />```get_energy``` should return ```mass``` multiplied by ```c``` squared.<br />

9. Test ```get_energy``` by using it on ```bomb_mass```, with the default value of ```c```. Save the result to a variable called ```bomb_energy```.

10. Print the string “A 1kg bomb supplies X Joules.”, with ```X``` replaced by ```bomb_energy```.

### Do the Work

11. Define a final function called ```get_work``` that takes in ```mass, ```acceleration```, and ```distance```.
<br />Work is defined as force multiplied by distance. First, get the ```force``` using ```get_force```, then multiply that by ```distance```. Return the result.<br />

12. Test ```get_work``` by using it on ```train_mass```, ````train_acceleration```, and ```train_distance```. Save the result to a variable called ```train_work```.

13. Print the string ```"The GE train does X Joules of work over Y meters."```, with ```X``` replaced with ```train_work``` and ```Y``` replaced with ```train_distance```.
