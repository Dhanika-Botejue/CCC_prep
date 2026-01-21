import sys

data = sys.stdin.read()
lines = data.splitlines()

note_amount, max_amount, good_amount = lines[0].split()

note_amount = int(note_amount)
max_amount = int(max_amount)
good_amount = int(good_amount)

notes = []
good_remaining = good_amount
phase_0 = True
final_note = None

# edge cases check
if note_amount > good_amount:
    print(-1)

else:
    for i in range(note_amount):        
        remaining_notes = note_amount - i - 1
        cur_contribution = min((i + 1), max_amount)

        if phase_0 == False:
            # forced
            notes.append(final_note)

        elif (cur_contribution + remaining_notes) > good_remaining:
            needed_contrib = good_remaining - remaining_notes
            needed_index = -1 * needed_contrib
            cur_note = notes[needed_index]
            notes.append(cur_note)
            good_remaining = 0 # always print final list because now its possible
            final_note = cur_note
            phase_0 = False
        
        else:
            cur_note = (i % max_amount) + 1
            good_remaining -= cur_contribution
            notes.append(cur_note)

        
        
    if good_remaining != 0:
        print(-1)
    else:
        result = " ".join(map(str, notes))
        print(result)



