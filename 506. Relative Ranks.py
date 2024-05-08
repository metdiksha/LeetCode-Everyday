def findRelativeRanks(score):
    if len(score) == 0:
        return []
    temp = list(score)
    temp.sort(reverse=True)
    print(temp)
    rank = []
    for i in score:
        rank.append(str(temp.index(i) + 1))

    rank[rank.index("1")] = "Gold Medal"
    if len(score) == 1:
        return rank
    rank[rank.index("2")] = "Silver Medal"
    if len(score) == 2:
        return rank
    rank[rank.index("3")] = "Bronze Medal"
    return rank


def main():
    score = [10, 3, 8, 9, 4]
    ret = findRelativeRanks(score)
    print(ret)


if __name__ == "__main__":
    main()
