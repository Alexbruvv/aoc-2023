def get_input(day: int) -> list[str]:
    return [line.strip() for line in open(f"input/{day}.txt").readlines()]