import json
from pathlib import Path

def count_solution_files(directory: str) -> int:
    py_files = list(Path(directory).rglob('*.py'))
    js_files = list(Path(directory).rglob('*.js'))
    return len(py_files) + len(js_files)

def latest_solution(directory: str) -> str:
    """
    Find the newest folder in folders of this pattern: 20XX/20XX-MM-DD
    """
    path = Path(directory)
    matching_folders: list[str] = []

    for item in path.rglob('*'):
        if item.is_dir() and item.name.startswith(directory):
            matching_folders.append(item.name)

    return max(matching_folders)
    
def main():
    solutions_dirs = ['2025', '2026']
    count: int = sum(count_solution_files(solutions_dir) for solutions_dir in solutions_dirs)
    latest: str = latest_solution(solutions_dirs[-1])

    data = {
        'solution_count': count,
        'last_solution': latest
    }

    with open('solutions-count.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == '__main__':
    main()