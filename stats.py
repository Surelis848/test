from collections import defaultdict


class StatsList(list):

    ########### MEAN ###########
    def mean(self):
        return sum(self) / len(self)

    # END mean

    ########### MEDIAN ###########
    def median(self):
        if len(self) % 2:
            return self[int(len(self) / 2)]
        else:
            idx = int(len(self) / 2)
            return (self[idx] + self[idx - 1]) / 2
        # ENDIF

    # END median

    ########### MODE ###########
    def mode(self):
        freqs = defaultdict(int)
        for item in self:
            freqs[item] += 1
        # ENDFOR

        mode_freq = max(freqs.values())
        modes = []
        for item, value in freqs.items():
            if value == mode_freq:
                modes.append(item)
            # ENDIF
        # ENDFOR

        return modes
    def smallest(self):
        self.sort()
        return self[:1]
    # END mode

# END CLASS StatsList