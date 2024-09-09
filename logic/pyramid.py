def draw_pyramid(number): 
  for i in range(0, number):
    num_of_stars = 2 * i + 1        # the formula to caculate number of stars
    num_of_spaces = number - i      # the formula to caculate number of spaces in each side
    print(' ' * num_of_spaces, end = "")
    print('*' * num_of_stars)

draw_pyramid(3)
