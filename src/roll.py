import random

def roll_stats():
    stats = []
    for x in range(0, 6):
        stats.append(roll_stat())
    return stats

def roll_stat():
    stat = []
    for x in range(0, 4):
        stat.append(random.randint(1,6))
    stat = sorted(stat, reverse=True)
    return sum(stat[:3])


if __name__=='__main__':
    print(roll_stats())