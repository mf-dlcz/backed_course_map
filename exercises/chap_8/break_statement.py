"""
Break Statement

Fix the check_defense function.

It checks each defensive enchantment against the attack.

If an enchantment is strong enough, it prints that the attack is blocked.

In that case, the loop should stop instead of checking further... make sure that it does!
"""

def check_defense(attack_strength, min_enchantment, max_enchantment):
    for enchantment_strength in range(min_enchantment, max_enchantment + 1):
        print(
            f"Comparing attack strength {attack_strength} to enchantment strength {enchantment_strength}."
        )

        if enchantment_strength >= attack_strength:
            print("Attack blocked!")
            break