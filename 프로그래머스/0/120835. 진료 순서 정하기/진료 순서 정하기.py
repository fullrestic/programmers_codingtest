def solution(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    rank_dict = {num : i + 1 for i, num in enumerate(sorted_emergency)}
    return [rank_dict[num] for num in emergency]