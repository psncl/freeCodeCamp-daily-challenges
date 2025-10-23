from typing import TypedDict

class Song(TypedDict):
    title: str
    plays: int

def favorite_songs(playlist: list[Song]) -> list[str]:

    most_played = sorted(playlist, key=lambda song: song["plays"], reverse=True)
    return [song["title"] for song in most_played[0:2]]

## Tests

assert favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]) == ["Sync or Swim", "Earbud Blues"]
assert favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]) == ["Clickwheel Love", "99 Downloads"]
assert favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]) == ["Song B", "Song C"]