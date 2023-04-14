from contextlib import contextmanager

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('start')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        print('exit')
        return True

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


if __name__ == "__main__":

    with ManagedFile('notes.txt') as file:
        file.write('todooooo...')

    with open_managed_file('2notes.txt') as file:
        file.write('written from decorator+generator!')


