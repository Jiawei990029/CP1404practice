"""
wimbledon
Estimate: 10 minutes
Actual:   116:( minutes
"""

def main():
    all_lists = make_list_of_champions()
    calculate_times_champions_won(all_lists)
    count_countries_won(all_lists)

def count_countries_won(all_lists):
    champion_to_country = {}
    for line_list in all_lists:
        champion_to_country[line_list[2]] = line_list[1]
    countries = list(set(champion_to_country.values()))
    countries.sort()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(','.join(countries))

def calculate_times_champions_won(all_lists):
    champion_to_times = {}
    for line_list in all_lists:
        try:
            champion_to_times[line_list[2]] += 1
        except KeyError:
            champion_to_times[line_list[2]] = 1
    print("Wimbledon Champions: ")
    for name, times in champion_to_times.items():
        print(f"{name} {times}")

def make_list_of_champions():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        all_lists = [line.strip().split(',') for line in in_file]
        all_lists.remove(all_lists[0])
    return all_lists

main()