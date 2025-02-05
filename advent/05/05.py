from math import floor

with open("test_input", "r", encoding="utf8") as f:
    lines = f.readlines()

lines = [line.strip().replace("\n", "") for line in lines]


def parse_input(lines):
    rules = {}
    pages = []
    IS_RULE = True
    for line in lines:
        if IS_RULE:
            if line == "":
                IS_RULE = False
                continue
            rule = line.split("|")
            try:

                rules[rule[0]].append(rule[1])
            except KeyError:
                rules[rule[0]] = [rule[1]]
            except Exception as e:
                print(e)
                print(rule)
                print(line)
        else:
            page_list = line.split(",")
            pages.append(page_list)
    return rules, pages


def check_page_order(page_list, rules):
    for idx, page in enumerate(page_list):
        try:
            page_rules = rules[page]
        except KeyError:
            # print(f"Skipping page because it has no rules. Page: {page}")
            continue
        if idx != 0:
            # Skip checking pages before b/c there are none for the first entry
            works = all(
                [
                    before_page not in page_rules
                    for before_page in page_list[:idx]
                ]
            )
            if not works:
                return False
        if idx != len(page_list):
            # Skip checking pages after b/c there are none for the last entry
            works = all(
                [
                    after_page in page_rules
                    for after_page in page_list[idx + 1 :]
                ]
            )
            if not works:
                return False
    return True


def reorder_pages(page_list, rules):
    for idx, page in enumerate(page_list):
        try:
            page_rules = rules[page]
        except KeyError:
            # print(f"Skipping page because it has no rules. Page: {page}")
            continue
        relevant_rules = [rule for rule in page_rules if rule in page_list]
        if idx == 0:
            new_list = [page] + relevant_rules
    # spots = len(page_list)
    # new_list = []
    # remaining_pages = page_list
    # for page in page_list:
    #     if new_list == []:
    #         new_list.append(page)
    #         continue
    #     try:
    #         page_rules = rules[page]
    #     except KeyError:
    #         # print(f"Skipping page because it has no rules. Page: {page}")
    #         continue
    #     relevant_rules = [rule for rule in page_rules if rule in page_list]
    #     for new_list_page in new_list:
    #         if new_list_page in relevant_rules:
    #             new_list.insert(new_list.index(new_list_page), page)
    #             break


rules, pages = parse_input(lines)
page_centers = []
for page_list in pages:
    meets_criteria = check_page_order(page_list, rules)
    if meets_criteria:
        n_pages = len(page_list)
        middle_idx = floor(n_pages / 2)  # use floor b/c py is 0 indexed
        page_centers.append(int(page_list[middle_idx]))

center_sums = sum(page_centers)
print(
    f"The sum of the middle numbers of the correctly ordered pages is: {center_sums}"
)

breakpoint()
