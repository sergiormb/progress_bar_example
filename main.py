from progress_bar import ProgressBar


def main():
    progress_bar = ProgressBar("=")
    progress_bar.load(end=4)
    progress_bar = ProgressBar("/\\")
    progress_bar.load(end=5)
    progress_bar = ProgressBar(u"\u2588")
    progress_bar.load(end=3)


if __name__ == '__main__':
    main()