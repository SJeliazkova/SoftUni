needed_experience = float(input())
battles = int(input())

battle_count = 0
collect_exper = 0

for battle in range(1, battles+1):
    exper_per_battle = float(input())

    battle_count += 1

    if  battle_count % 3 == 0:
        exper_per_battle = exper_per_battle * 1.15

    if battle_count % 5 == 0:
        exper_per_battle = exper_per_battle * 0.90

    if battle_count % 15 == 0:
        exper_per_battle = exper_per_battle * 1.05

    collect_exper += exper_per_battle

    if collect_exper >= needed_experience:
        print(f"Player successfully collected his needed "
              f"experience for {battle_count} battles.")
        break

if needed_experience > collect_exper:
    print(f"Player was not able to collect the needed experience, {(needed_experience - collect_exper):.2f} more needed.")


