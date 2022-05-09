def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    mytime = pontoon_distance / you_speed
    if dolphin == True:
        shark_speed = shark_speed / 2
    sharktime = shark_distance / shark_speed
    if mytime >= sharktime:
        return "Shark Bait!"
    else:
        return "Alive!"

if __name__ == "__main__":

    assert(shark(12, 50, 4, 8, True) == "Alive!");
    assert(shark(7, 55, 4, 16, True) == "Alive!");
    assert(shark(24, 0, 4, 8, True) == "Shark Bait!");