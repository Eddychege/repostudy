def calculate_final_speed(initial_speed, inclinations):
    speed=initial_speed

    for inclination in inclinations:
        if inclination>0:
            speed-=inclination
        elif inclination<0:
            speed+=abs(inclination)
    return speed

print(calculate_final_speed(100, [10, 50, -50]))