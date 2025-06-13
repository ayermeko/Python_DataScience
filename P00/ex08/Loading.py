

def ft_tqdm(lst: range) -> None:  # type: ignore
    total = len(lst)
    for i, item in enumerate(lst, start=1):
        percent = int((i / total) * 100)
        bar_length = 50
        filled = int(bar_length * i // total)
        bar = '=' * (filled - 1) + '>' + ' ' * (bar_length - filled)
        print(f'\r{percent:3}%|[{bar}]| {i}/{total}', end='', flush=True)
        yield item
