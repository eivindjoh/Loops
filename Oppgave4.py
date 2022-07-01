import math
import scipy.stats as stats
import matplotlib.pyplot as plt


def throw_distance(velocity, angle):
    throw_angle = math.radians(angle)
    throw_velocity = velocity / 3.6
    throw_velocity_y = throw_velocity * math.cos(throw_angle)
    throw_velocity_z = throw_velocity * math.sin(throw_angle)
    air_time = (throw_velocity_z + math.sqrt((throw_velocity_z ** 2) + (2 * 9.81 * 1.8))) / 9.81
    distance = throw_velocity_y * air_time
    return distance


def thorkildsen_throw():
    velocity = stats.weibull_max.rvs(2, loc=107, scale=4, size=1)[0]
    angle = stats.norm.rvs(48, 7, 1)[0]
    distance = throw_distance(velocity, angle)
    return distance


def pitkamaki_throw():
    velocity = stats.weibull_max.rvs(2, loc=106.5, scale=3, size=1)[0]
    angle = stats.norm.rvs(45.5, 4, 1)[0]
    distance = throw_distance(velocity, angle)
    return distance


def pitkamaki_competition_best(numb_throw=6):
    throws = []
    for i in range(numb_throw):
        throws.append(pitkamaki_throw())
    return max(throws)


def thorkildsen_competition_best(numb_throw=6):
    throws = []
    for i in range(numb_throw):
        throws.append(thorkildsen_throw())
    return max(throws)


def results_comp(numb_trow=6):
    print(f'Competition with {numb_trow} throws:\n')
    thorkildsen_results = []
    pitkamaki_results = []

    for i in range(1000):
        thorkildsen_results.append(thorkildsen_competition_best(numb_trow))
        pitkamaki_results.append(pitkamaki_competition_best(numb_trow))

    thorkildsen_wins = 0
    pitkamaki_wins = 0
    draws = 0

    for i in range(1000):
        if thorkildsen_results[i] > pitkamaki_results[i]:
            thorkildsen_wins += 1
        elif pitkamaki_results[i] > thorkildsen_results[i]:
            pitkamaki_wins += 1
        else:
            draws += 1

    print(f'Thorkildsen wins {thorkildsen_wins} times')
    print(f'Pitkamaki wins {pitkamaki_wins} times')
    print(f'Draws: {draws}')

    winning_throw = []
    for i in range(1000):
        if thorkildsen_results[i] > pitkamaki_results[i]:
            winning_throw.append(thorkildsen_results[i])
        elif pitkamaki_results[i] > thorkildsen_results[i]:
            winning_throw.append(pitkamaki_results[i])
        else:
            winning_throw.append(thorkildsen_results[i])

    values = winning_throw
    alpha = 0.05
    values.sort()
    lower_idx = round(len(values)*(alpha/2))
    upper_idx = round(len(values)*(1-(alpha/2))-1)
    print('\n95% confidence for their winning throw length:')
    print(f'lower_value: {round(values[lower_idx], 2)}m')
    print(f'upper_value: {round(values[upper_idx], 2)}m\n')

    num_bins = 50
    plt.hist(thorkildsen_results, num_bins, facecolor='blue', alpha=0.5)
    plt.hist(pitkamaki_results, num_bins, facecolor='red', alpha=0.5)
    plt.xlabel('Distance in meters')
    plt.ylabel('Number of throws')
    plt.title(f"Histogram of comp with {numb_trow} throws")
    plt.legend(['Thorkildsen', 'Pitkamaki'])
    plt.show()


results_comp()
results_comp(18)
