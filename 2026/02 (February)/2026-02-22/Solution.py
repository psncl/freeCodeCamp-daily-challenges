class MedalTally:
    country_name: str
    gold_count: int = 0
    silver_count: int = 0
    bronze_count: int = 0

    def __init__(self, country: str) -> None:
        self.country_name = country

    @property
    def total_medal_count(self) -> int:
        return self.gold_count + self.silver_count + self.bronze_count

    def to_csv_row(self) -> str:
        return ",".join([
            self.country_name, 
            str(self.gold_count), 
            str(self.silver_count), 
            str(self.bronze_count), 
            str(self.total_medal_count)
            ])

def count_medals(winners: list[list[str]]) -> str:

    countries_medals: dict[str, MedalTally] = {}

    for event in winners:
        for i in range(len(event)):
            country_name = event[i]

            countries_medals.setdefault(country_name, MedalTally(country_name))

            country_medals = countries_medals[country_name]

            if i == 0:
                country_medals.gold_count += 1
            elif i == 1:
                country_medals.silver_count += 1
            elif i == 2:
                country_medals.bronze_count += 1

    # Negated gold_count in order to sort first by DESC, then by ASC.
    sorted_countries = sorted(countries_medals.values(), key=lambda c: (-c.gold_count, c.country_name))

    csv_header = "Country,Gold,Silver,Bronze,Total"
    csv_rows = "\n".join([c.to_csv_row() for c in sorted_countries])

    return "\n".join([csv_header, csv_rows])

## Tests

assert count_medals([["USA", "CAN", "NOR"], ["NOR", "USA", "CAN"], ["USA", "NOR", "SWE"]]) == "Country,Gold,Silver,Bronze,Total\nUSA,2,1,0,3\nNOR,1,1,1,3\nCAN,0,1,1,2\nSWE,0,0,1,1"
assert count_medals([["NOR","SWE","FIN"]]) == "Country,Gold,Silver,Bronze,Total\nNOR,1,0,0,1\nFIN,0,0,1,1\nSWE,0,1,0,1"
assert count_medals([["ITA", "CHN", "CHN"], ["JPN", "ITA", "JPN"]]) == "Country,Gold,Silver,Bronze,Total\nITA,1,1,0,2\nJPN,1,0,1,2\nCHN,0,1,1,2"
assert count_medals([["USA","CAN","NOR"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["SWE","FIN","NOR"], ["CAN","USA","SWE"], ["FRA","GER","ITA"]]) == "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nFRA,1,1,0,2\nGER,1,1,0,2\nJPN,1,0,0,1\nSWE,1,0,1,2\nUSA,1,1,0,2\nCHN,0,0,1,1\nFIN,0,1,0,1\nITA,0,0,2,2\nKOR,0,1,0,1\nNOR,0,0,2,2"
assert count_medals([["ESP","ITA","FRA"], ["ITA","ESP","GER"], ["NOR","SWE","FIN"], ["FIN","NOR","SWE"], ["USA","CAN","MEX"], ["CAN","USA","MEX"], ["JPN","KOR","CHN"], ["CHN","JPN","KOR"]]) == "Country,Gold,Silver,Bronze,Total\nCAN,1,1,0,2\nCHN,1,0,1,2\nESP,1,1,0,2\nFIN,1,0,1,2\nITA,1,1,0,2\nJPN,1,1,0,2\nNOR,1,1,0,2\nUSA,1,1,0,2\nFRA,0,0,1,1\nGER,0,0,1,1\nKOR,0,1,1,2\nMEX,0,0,2,2\nSWE,0,1,1,2"
assert count_medals([["USA","CAN","GER"], ["NOR","SWE","FIN"], ["USA","NOR","SWE"], ["GER","FRA","ITA"], ["JPN","KOR","CHN"], ["USA","GER","CAN"], ["SWE","NOR","FIN"], ["CAN","USA","NOR"], ["FRA","GER","ITA"], ["JPN","CHN","KOR"], ["SWE","FIN","NOR"], ["GER","ITA","FRA"]]) == "Country,Gold,Silver,Bronze,Total\nUSA,3,1,0,4\nGER,2,2,1,5\nJPN,2,0,0,2\nSWE,2,1,1,4\nCAN,1,1,1,3\nFRA,1,1,1,3\nNOR,1,2,2,5\nCHN,0,1,1,2\nFIN,0,1,2,3\nITA,0,1,2,3\nKOR,0,1,1,2"