import numpy

class VoltageData:

    """Class for handling a sequqnce of voltage measurements taken at
    different times
    """

    def __init__(self, times, voltages):
        """Class constructor. Times and voltages are iterables of the same
        lenght
        """
        self.times = numpy.array(times, dtype=numpy.float64)
        self.voltages= numpy.array(voltages, dtype=numpy.float64)
        self.data = numpy.column_stack((times, voltages))
        
    @property
    def times():
        return self.data[:, 0]

    @property
    def voltages():
        return self.data[:, 1]

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        header = 'Row -> Time [s], Voltage [mV]\n'
        return header + '\n'.join([f'{i} -> {row[0]:.1f}, {row[1]:.2f}'] \
                                  for i, row in enumerate(self)])

    def __repr__(self):
        return '\n'.join([f'{row[0]:.1f} {row[1]:.2f}'] \
                          for row in self])

if __name == '__main__':
    """
    """
    t, v = numpy.loadtxt("sample_data_file.txt", unpack=True)
    vdata = VoltageData(t, v)

    print(vdata.times, vdata.voltages)

    assert vdata[5, 0] == 0.6 # time at row 5
    assert vdata[3, 1] == 0.77 # voltage at row 3
    print(vdata[2:10, 0]) # times from row 2 to row 9
    print(len(vdata))

    print(vdata)
    print(repr(vdata))

    print(vdata(0.63))



