def main():
    S = input()
    weeks = list(reversed(['SUN','MON','TUE','WED','THU','FRI','SAT']))
    print(weeks.index(S)+1)

if __name__ == "__main__":
    main()
