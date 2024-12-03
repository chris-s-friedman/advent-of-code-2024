with open("input", "r") as f:
    reports = f.readlines()

f.close()

reports = [report.strip().split(" ") for report in reports]


# part 1 solution
def is_safe(report):
    report = [int(level) for level in report]
    for i in range(len(report) - 1):
        level = report[i]
        next_level = report[i + 1]
        # Check level difference
        if level == next_level:
            return False
        else:
            level_diff = abs(level - next_level)
            if level_diff > 3:
                return False
        # Check report order
        if i == 0:
            # skip report order check for the first level
            descending = level > next_level
        else:
            if descending:
                if level < next_level:
                    return False
            else:
                if level > next_level:
                    return False
    return True


report_safety = [is_safe(report) for report in reports]

safe_report_count = sum(report_safety)
print(f"Safe reports: {safe_report_count}")

# Part 2 Solution


def is_safe_pd(report):
    # first check if the report is safe without problem dampener
    result = is_safe(report)
    if result:
        return True
    else:
        for i in range(len(report)):
            # remove the i-th element and check if the report is safe
            new_report = report[:i] + report[i + 1 :]
            result = is_safe(new_report)
            if result:
                return True
    return False


report_safety_with_pd = [is_safe_pd(report) for report in reports]

safe_report_count_with_pd = sum(report_safety_with_pd)
print(f"Safe reports with Problem Dampener: {safe_report_count_with_pd}")
