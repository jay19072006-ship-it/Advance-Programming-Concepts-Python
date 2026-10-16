def cal_result(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"
