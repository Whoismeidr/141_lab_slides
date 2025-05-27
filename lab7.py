# Name: Mark Luu
# Created for the Testing lab for CMPT 141.

def oj_oneshot_rate(atk_mod, def_mod, def_health):
    """Function to find the odds of any attacker one-shotting a defender
    in 100% Orange Juice.
    atk_mod: Bonus to attack roll for attacker.
    def_mod: Bonus to defend roll for defender.
    def_health: Health of defender.
    Returns: A string representation of the fraction of events
    where the defender gets one-shot from full health."""

    # TODO: The minimum attack and defend roll is 1.
    # There should be no scenario where a -1 attacker kills a 5 health character,
    # regardless of their defense modifier.
    # Fix the error in logic that is causing the output of (-1, -1, 5)
    # to return something other than 0/36.

    loss_count = 0
    fight_count = 0
    dice_size = range(1, 6 + 1)

    for attack in dice_size:
        for defend in dice_size:
            if (attack + atk_mod) >= (defend + def_mod + def_health):
                loss_count += 1
            fight_count += 1

    return str(loss_count) + "/" + str(fight_count)

print(oj_oneshot_rate(-1, -1, 5))