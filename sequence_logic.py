import random
from typing import List, Dict


def _is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def _prime_digits(length: int) -> List[int]:
    digits: List[int] = []
    n = 2
    while len(digits) < length:
        if _is_prime(n):
            for ch in str(n):
                digits.append(int(ch))
                if len(digits) == length:
                    break
        n += 1
    return digits


def _fibonacci_digits(length: int) -> List[int]:
    digits: List[int] = []
    a, b = 1, 1
    while len(digits) < length:
        a, b = b, a + b
        for ch in str(b):
            digits.append(int(ch))
            if len(digits) == length:
                break
    return digits


def _mirror_pattern(length: int, max_digit: int) -> List[int]:
    half = (length + 1) // 2
    base = [random.randint(0, max_digit) for _ in range(half)]
    mirror_part = list(reversed(base[: length - half]))
    return base + mirror_part


def _random_digits(length: int, max_digit: int) -> List[int]:
    return [random.randint(0, max_digit) for _ in range(length)]


def generate_sequence(length: int, max_digit: int = 9, mode: str = "random") -> List[int]:
    if mode == "primes":
        return _prime_digits(length)
    if mode == "fibonacci":
        return _fibonacci_digits(length)
    if mode == "mirror":
        return _mirror_pattern(length, max_digit)
    return _random_digits(length, max_digit)


def _get_perf_value(perf, key: str, default: int = 0) -> int:
    if perf is None:
        return default
    try:
        return int(perf.get(key, default))  # type: ignore[attr-defined]
    except Exception:
        try:
            return int(perf[key])  # type: ignore[index]
        except Exception:
            return default


def round_config(level: int, performance=None) -> Dict[str, int]:
    streak = _get_perf_value(performance, "streak", 0)
    failures = _get_perf_value(performance, "failures", 0)
    last_time_left = _get_perf_value(performance, "lastTimeLeft", 0)

    base_length = min(3 + level, 18)
    length_adjust = 0
    if streak >= 5:
        length_adjust += 2
    elif streak >= 3:
        length_adjust += 1
    if failures >= 2:
        length_adjust -= 1
    seq_length = max(3, min(18, base_length + length_adjust))

    time_allowance = max(6 + int(seq_length * 1.2), 6 + level)
    if last_time_left >= 6:
        time_allowance -= 2
    elif last_time_left >= 3:
        time_allowance -= 1
    if failures >= 1:
        time_allowance += 2
    if failures >= 2:
        time_allowance += 1
    time_allowance = max(6, min(40, time_allowance))

    return {"length": seq_length, "time": time_allowance}


def score_for_round(seq_len: int, performance=None) -> int:
    streak = _get_perf_value(performance, "streak", 0)
    last_time_left = _get_perf_value(performance, "lastTimeLeft", 0)
    failures = _get_perf_value(performance, "failures", 0)
    base = seq_len * 12
    streak_bonus = min(30, streak * 6)
    speed_bonus = min(24, max(last_time_left - 2, 0) * 2)
    failure_penalty = min(30, failures * 5)
    return max(seq_len * 5, base + streak_bonus + speed_bonus - failure_penalty)


def check_sequence(player: List[int], correct: List[int]) -> bool:
    return list(player) == list(correct)


def get_result_message(success: bool, sequence: List[int]) -> str:
    if success:
        return "Correct — next round!"
    return f"Wrong order. Correct digits: {' '.join(str(n) for n in sequence)}"


def get_high_scores() -> List[Dict[str, int]]:
    # High scores are managed in JS/localStorage; return empty for Python mode.
    return []


if __name__ == "__main__":
    print("Random:", generate_sequence(8))
    print("Primes:", generate_sequence(8, mode="primes"))
    print("Fibonacci:", generate_sequence(8, mode="fibonacci"))
    print("Mirror:", generate_sequence(8, mode="mirror"))


