actor_name = input()
actor_score = float(input())
jury = int(input())

for i in range (1, jury + 1):
    jury_name = input()
    jury_score = float(input())

    jury_lenght = len(jury_name)
    actor_score += jury_lenght * jury_score / 2

    if actor_score >= 1250.5:
        break

if actor_score >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_score:.1f}!")

else:
    needed_score = 1250.5 - actor_score
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")
