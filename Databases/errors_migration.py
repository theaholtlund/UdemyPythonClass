# Importing ducks
import errors_ducks

flock = errors_ducks.Flock()
donald = errors_ducks.Duck()
daisy = errors_ducks.Duck()
duck3 = errors_ducks.Duck()
duck4 = errors_ducks.Duck()
duck5 = errors_ducks.Duck()
duck6 = errors_ducks.Duck()
duck7 = errors_ducks.Duck()

# Adding a penguin to the flock will raise an error, because the class does not have a fly method
percy = errors_ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

# This will raise an error, because the add_duck method only accepts ducks as arguments
flock.add_duck(percy)

flock.migrate()
