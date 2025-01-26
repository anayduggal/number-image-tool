
import random

# modes:
# default (mode 0)
#   default colours
#   requires nothing
# primes (mode 1)
#   prime digits are set to one colour, composites are set to another colour
#   requires an array of only 2 colours [prime_colour, comp_colour]
# even or odd (mode 2)
#   evens are set to one colour, composites are set to another colour
#   requires an array of only 2 colours [even_colour, odd_colour]
# custom (mode 3)
#   digits are set custom colours
#   any unspecified digits are set to black
#   requires an array of tuples (digit, colour) of length 0-10
# random (mode 4)
#   digits are set completely random colours
#   requires nothing

def generateConfig(mode, input_config=[]):

    if mode == 0:
        config_list = [
            [255, 0, 0],
            [255, 127, 0],
            [255, 255, 0],
            [127, 255, 0],
            [0, 255, 0],
            [0, 255, 127],
            [0, 255, 255],
            [0, 127, 255],
            [0, 0, 255],
            [127, 0, 255]
        ]

    elif mode == 1:
        primes = [2, 3, 5, 7]
        config_list = [input_config[0] if i in primes else input_config[1] for i in range(10)]

    elif mode == 2:
        config_list = [input_config[0] if i % 2 == 0 else input_config[1] for i in range(10)]

    elif mode == 3:
        config_list = []
        step = -1

        if input_config[-1][0] != 9:
            input_config.append((9, [0, 0, 0]))

        for i in input_config:
            for _ in range(step + 1, i[0]):
                config_list.append([0, 0, 0])
            config_list.append(i[1])

    elif mode == 4:
        config_list = [random.sample(range(0, 255), 3) for _ in range(10)]

    with open("config.txt", "w") as f:
        for count, val in enumerate(config_list):
            color_string = ",".join(str(i) for i in val)
            f.write(f"{count},{color_string}\n")






