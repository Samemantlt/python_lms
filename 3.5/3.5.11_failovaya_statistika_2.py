import json


def avg(seq):
    return sum(seq) / len(seq)


def main():
    filename = input()

    with open(filename) as file:
        text = file.read()

    filename = input()

    nums = [int(i) for i in text.split()]

    result = {
        "count": len(nums),
        "positive_count": len([i for i in nums if i > 0]),
        "min": min(nums),
        "max": max(nums),
        "sum": sum(nums),
        "average": f"{avg(nums):.2f}"
    }

    with open(filename, 'w') as file:
        file.write(json.dumps(result))


if __name__ == "__main__":
    main()
