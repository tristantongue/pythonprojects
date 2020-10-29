
class Note:

    rank_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def __init__(self, rank = 0, nextnote = 0):
        rank_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        if isinstance(rank, int):
            self.rank = rank
            self.nextnote = int(rank + 1)
        else:
            rank = rank_names.index(rank.upper())
            self.rank = rank
            self.nextnote = int(rank +1)
            
    #default is C, notes are most basic form of information. the rank can be supplied as a string, if its a string, it gets searched for in rank_names and is converted into an integer


    def __str__(self):
        return '%s' % Note.rank_names[self.rank]

    def print_note(self):
        print('%s' % Note.rank_names[self.rank])

    def print_nextnote(self):
        print('%s' % Note.rank_names[self.rank+1])
    


class Octave:

    octavelist = [0,1,2,3,4,5,6,7,8,9,10,11]

    def __init__(self, root = 0):
        rank_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        if isinstance(root, int):
            self.notes = []
            self.root = root
            ournote = Note(root)
            i = root
            while i <= (root+11):
                self.notes.append(Note(Octave.octavelist[i % len(Octave.octavelist)]))
                i += 1
        else:
            self.notes = []
            root = rank_names.index(root.upper())
            self.root = root
            i = root
            while i <= (root+11):
                self.notes.append(Note(Octave.octavelist[i % len(Octave.octavelist)]))
                i += 1

    #default octave is C, otherwise octave will take the root and run through from new start point. can be string or interger, same as note.

    def __str__(self):
        res = []
        for note in self.notes:
            res.append(str(note))
            octave = '\n'.join(res)
        return octave

    def get_major_scale(self):
        root = getattr(self, 'root')
        return major_scale(root)

    def get_minor_scale(self):
        root = getattr(self, 'root')
        return minor_scale(root)

    def get_majorinterval_chords(self):
        root = getattr(self, 'root')
        print('Printing major chords:')
        return major_scale_chords(root)
    
    def get_minorinterval_chords(self):
        root = getattr(self, 'root')
        print('Printing minor chords:')
        return minor_scale_chords(root)





class major_scale(Octave):
# the major scale of the given root

    def __init__(self, root):
        self.root = root
        self.notes = []
        i = root
        self.notes.append('%s %s' % (Note(root), 'Major scale:'))
        self.notes.append(Note(Octave.octavelist[i % 12]))
        self.notes.append(Note(Octave.octavelist[(i+2)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+4)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+5)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+7)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+9)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+11)% 12]))


class minor_scale(Octave):
# the minor scale of the given root
    def __init__(self, root):
        self.root = root
        self.notes = []
        i = root
        self.notes.append('%s %s' % (Note(root),'Minor scale:'))
        self.notes.append(Note(Octave.octavelist[i % 12]))
        self.notes.append(Note(Octave.octavelist[(i+2)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+3)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+5)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+7)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+8)% 12]))
        self.notes.append(Note(Octave.octavelist[(i+10)% 12]))

class minor_scale_chords(Octave):

    def __init__(self, root = 0):
        self.notes = []
        i = root
        self.notes.append('%s %s' % (Note(Octave.octavelist[i % 12]), "Minor"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+2)% 12]), "Diminished"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+3)% 12]), "Major"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+5)% 12]), "Minor"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+7)% 12]), "Minor"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+8)% 12]), "Major"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+10)% 12]), "Major"))

class major_scale_chords(Octave):

    def __init__(self, root = 0):
        self.notes = []
        i = root
        self.notes.append('%s %s' % (Note(Octave.octavelist[i % 12]), "Major"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+2)% 12]), "Minor"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+4)% 12]), "Minor"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+5)% 12]), "Major"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+7)% 12]), "Major"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+9)% 12]), "Minor"))
        self.notes.append('%s %s' % (Note(Octave.octavelist[(i+11)% 12]), "Diminished"))

key = Octave(input("Enter a root note for octave: "))

print("what other musical information would you like? Request the major scale with chords, or minor scale with chords.")

choice = input("Enter 1 for Major interval or 2 for Minor interval: ")

if choice == "1":
    print(key.get_major_scale())
    print(key.get_majorinterval_chords())
if choice == "2":
    print(key.get_minor_scale())
    print(key.get_minorinterval_chords())
