from math import ceil

class SGSResult():

    def __init__(self, round_actuals:bool = True, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __iter__(self) -> dict:
        for key, value in vars(self).items():
            yield (key, value)

    def __repr__(self) -> str:
        return str(dict(self))

    def pretty_print(self) -> None:

        def round_up(x, base):
            return base * ceil(x/base)
        
        _print_dict = {}
        _spacing = 2
        _tab = 8

        _max = round_up(
            max([len(k.replace("_", " ") + ":") for k in (vars(self).keys())]) + 1,
            _tab
        )

        for k, v in vars(self).items():
            _k = k.replace("_", " ") + ":"
            diff = _max + (_spacing * _tab) - len(_k)
            tabs = int(round_up(diff, _tab) / _tab)
            _k = _k + ('\t' * tabs)
            _print_dict[_k] = v

        print('\n\n')

        for k, v in _print_dict.items():
            print(f'{k}{v}\n\n', sep='')