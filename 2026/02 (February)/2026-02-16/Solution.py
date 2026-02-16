from typing import TypedDict

class TeamInfo(TypedDict):
    name: str
    total_points: int

def get_semifinal_matchups(teams: list[str]) -> str:

    semis_teams: list[TeamInfo] = [get_team_and_points(team) for team in teams]
    semis_teams.sort(reverse=True, key=lambda team: team["total_points"])

    return f"The semi-final games will be {semis_teams[0]['name']} vs {semis_teams[3]['name']} and {semis_teams[1]['name']} vs {semis_teams[2]['name']}."

def get_team_and_points(team_record: str) -> TeamInfo:
    """
    Parse a team record of the format `TEAM: W-OTW-OTL-L`,
    e.g. `FIN: 2-2-1-0` and return the team name and number of points.
    """

    team, points_str = team_record.split(": ")
    wins, overtime_wins, overtime_losses, _losses = [int(pt) for pt in points_str.split("-")]

    total_points = (wins * 3) + (overtime_wins * 2) + overtime_losses

    return TeamInfo(name=team, total_points=total_points)

## Tests

assert get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]) == "The semi-final games will be FIN vs SWE and CAN vs USA."
assert get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]) == "The semi-final games will be USA vs CZE and CAN vs FIN."
assert get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]) == "The semi-final games will be CAN vs ITA and USA vs CZE."
assert get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]) == "The semi-final games will be JPN vs ITA and AUT vs KOR."