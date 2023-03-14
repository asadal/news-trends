from newstrends import utils


def main():
    keyword = '코로나'
    df = utils.search_keywords_as_dataframe(keyword, num_days=7, ignore_time=True)

    counts = [
        (date, df_.shape[0]) for date, df_ in df.groupby(by='date', sort=True)
    ]
    for date, count in counts:
        print(f"{date.strftime('%Y/%m/%d')}: {count}")


if __name__ == '__main__':
    main()
