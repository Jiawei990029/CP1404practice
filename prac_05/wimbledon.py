"""
wimbledon
Estimate: 10 minutes
Actual:    minutes
"""

def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        all_lists = [line.strip().split(',') for line in in_file]
        all_lists.remove(all_lists[0])
    champion_to_country = {}
    for line_list in all_lists:
        try:
            champion_to_country[line_list[2]] += 1
        except KeyError:
            champion_to_country[line_list[2]] = 1
    print(champion_to_country)



main()