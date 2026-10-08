def getsteer(desired,actual):
    if actual<0:
        return -getsteer(-desired,-actual)
    return (actual+desired)/2
