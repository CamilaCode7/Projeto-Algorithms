def study_schedule(permanence_period, target_time):
    try:
        cont = 0
        for items in permanence_period:
            if items[0] <= target_time <= items[1]:
                cont += 1
        return cont
    except Exception:
        None
