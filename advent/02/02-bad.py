# This was my supposed "non-naive" solution. This solution never actually
# worked and is long and messy and just no bueno. saving as evidence of me
# trying and trying and trying.... and then just saying, i'll iterate through
# my list so that this work actually gets completed.
# the non naive solution here did not work and got very messy. Why not just do
# things the naive way (try to delete each element if needed)?
def is_safe_pd(report):
    def is_safe_pair(level1, level2, descending: bool = None):
        # Check level difference
        if level1 == level2:
            return (False, descending, "Levels are equal")
        else:
            level_diff = abs(level1 - level2)
            if level_diff > 3:
                return (False, descending, "Level difference is greater than 3")
        # check level order
        if descending is None:
            descending = level1 > level2
        else:
            if descending:
                if level1 < level2:
                    return (
                        False,
                        descending,
                        "Descending order is not maintained",
                    )
            else:
                if level1 > level2:
                    return (
                        False,
                        descending,
                        "Ascending order is not maintained",
                    )
        return (True, descending, None)

    def tester(report):
        pd_activated = False
        for i in range(len(report) - 1):
            if i == 0:
                descending = None
            if pd_activated:
                level = report[i + 1]
                try:
                    next_level = report[i + 2]
                except IndexError:
                    return (
                        report,
                        True,
                        {
                            "i": i,
                            "pd_activated": pd_activated,
                            "reason": "end of report",
                        },
                    )
                safe, descending, reason = is_safe_pair(
                    level, next_level, descending
                )
                if not safe:
                    return (
                        report,
                        False,
                        {
                            "i": i,
                            "pd_activated": pd_activated,
                            "reason": reason,
                        },
                    )
            else:
                level = report[i]
                next_level = report[i + 1]
                safe, descending, reason = is_safe_pair(
                    level, next_level, descending
                )
                if not safe:
                    pd_activated = True
                    try:
                        next_level = report[i + 2]
                    except IndexError:
                        return (
                            report,
                            True,
                            {
                                "i": i,
                                "pd_activated": pd_activated,
                                "reason": "end of report",
                            },
                        )
                    safe, descending, reason = is_safe_pair(
                        level, next_level, descending
                    )
                    if not safe:
                        return (
                            report,
                            False,
                            {
                                "i": i,
                                "pd_activated": pd_activated,
                                "reason": reason,
                            },
                        )
        return (
            report,
            True,
            {
                "i": i,
                "pd_activated": pd_activated,
                "reason": "No issues found",
            },
        )

    report = [int(level) for level in report]
    result = tester(report)
    if (not result[1]) and (result[2]["i"] == 1):
        result = [result, tester(report[1:])]
    else:
        result = [result]
    return {"report": report, "results": result}


def print_safety_report(report):
    print(f"Report: {report['report']}")
    for result in report["results"]:
        print(f"\tIs safe: {result[1]}")
        if not result[1]:
            print(f"\t\tReason: {result[2]['reason']}")
            print(
                f"\t\tProblem Dampener Activated: {result[2]['pd_activated']}"
            )
            print(f"\t\tIndex: {result[2]['i']}")
    print("\n")


report_safety_with_pd = [is_safe_pd(report) for report in reports]

safe_report_count_with_pd = sum(
    i["results"][-1][1] for i in report_safety_with_pd
)
print(f"Safe reports with Problem Dampener: {safe_report_count_with_pd}")
