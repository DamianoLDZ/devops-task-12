import shutil


def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    usage_percent = (used / total) * 100

    return {
        "total": total,
        "used": used,
        "free": free,
        "usage_percent": round(usage_percent, 2)
    }


if __name__ == "__main__":
    result = check_disk_usage()

    print(f"Disk usage: {result['usage_percent']}%")
    print(f"Free space: {result['free']} bytes")
