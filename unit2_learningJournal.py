from math import pi

# PART 1
def print_volume(r):
    volume_of_a_sphere = 4/3 * pi * r ** 3
    print(volume_of_a_sphere) 

print_volume(1)
# output 4.1887902047863905
print_volume(3)
# output 113.09733552923254
print_volume(5)
# output 523.5987755982989


# PART 2
def part_two_fun(a, b):
    make_more = a * 21
    sell_it_all = b / 2
    if make_more <= 63:
        print("Make More now!")
    elif make_more >= 250:
        print("We have too much!")
    else:
        print("Just right!")
    if sell_it_all <= 100:
        print("Sell it all!!")
    elif sell_it_all >= 3000:
        print("Very nice!")
    else:
        print("Doing OK!")

part_two_fun(2, 180)
part_two_fun(13, 6600)
part_two_fun(7, 3000)