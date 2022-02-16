def avg(marks):
    assert len(marks) != 0
    return sum(marks) / len(marks)


marks = [45,45,23]
print("Averager of mark1 :", avg(marks))


def avg(marks):
    assert len(marks) != 0,"list is empty."
    return sum(marks) / len(marks)


marks = []
print("Averager of mark1 :", avg(marks))
