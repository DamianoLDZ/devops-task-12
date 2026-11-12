import shutil


def calculate_usage_percent(used, total):
    return round((used / total) * 100, 2)


def check_disk_usage(path="/"):
    try:
        total, used, free = shutil.disk_usage(path)
    except OSError as error:
        raise ValueError(f"Cannot check disk usage for path: {path}") from error

    usage_percent = calculate_usage_percent(used, total)

    return {
        "total": total,
        "used": used,
        "free": free,
        "usage_percent": usage_percent
    }


if __name__ == "__main__":
    try:
        result = check_disk_usage()

        print(f"Disk usage: {result['usage_percent']}%")
        print(f"Free space: {result['free']} bytes")
    except ValueError as error:
        print(f"Error: {error}")
