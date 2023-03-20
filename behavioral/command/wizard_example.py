
class Wizard:

    def __init__(self, src, root_dir):
        self.choices = []
        self.root_dir = root_dir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print('Copying binaries --', self.src, 'to', self.root_dir)
            else:
                print('No operation')


if __name__ == '__main__':
    # client code
    wizard = Wizard('pyhton3.10.gzip', '/usr/bin/')

    # Users choices to install python only
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
