# filter to point
def filter_threshold(point):
    if point.index > 800 and point.index < 810:
        return True
    return False

# filter to trajectory
def filter_length(trajectory):
    if len(trajectory) < 30:
        return True
    return False