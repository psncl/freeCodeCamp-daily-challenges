import json
from pathlib import Path

def count_solution_files(directory: str) -> int:
    py_files = list(Path(directory).rglob('*.py'))
    js_files = list(Path(directory).rglob('*.js'))
    return len(py_files) + len(js_files)

def latest_solution(directory: str, prefix: str) -> str:
    path = Path(directory)
    matching_folders: list[str] = []

    for item in path.rglob('*'):
        if item.is_dir() and item.name.startswith(prefix):
            matching_folders.append(item.name)

    return max(matching_folders)
    
def main():
    solutions_dir = '2025'
    count = count_solution_files(solutions_dir)
    latest = latest_solution(solutions_dir, prefix="2025")

    data = {
        'solution_count': count,
        'last_solution': latest
    }

    with open('solutions-count.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == '__main__':
    main()