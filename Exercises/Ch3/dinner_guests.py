"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41-42), use len() to print a message indicating the number
of people you're inviting to dinner.
"""

guests = ['Steve Jobs', 'APJ Abdul Kalam', 'Archimedes']
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')

print(f"\n{guests[2]} won't be attending the dinner.\n")

guests[2] = "Leonardo Da Vinci"
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')

print('\nI got reservation to a bigger table...!\n')
guests.insert(0, 'Joey')
guests.insert(2, 'Chandler')
guests.append('Phoebe')
print(f'Dear {guests[0]}, I cordially invite you to a dinner.')
print(f'Dear {guests[1]}, I cordially invite you to a dinner.')
print(f'Dear {guests[2]}, I cordially invite you to a dinner.')
print(f'Dear {guests[3]}, I cordially invite you to a dinner.')
print(f'Dear {guests[4]}, I cordially invite you to a dinner.')
print(f'Dear {guests[5]}, I cordially invite you to a dinner.')
print(f'\nI am inviting {len(guests)} people to the Dinner.')
