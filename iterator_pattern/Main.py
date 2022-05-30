from BrowseHistory import BrowserHistory

if __name__ == '__main__':
    history = BrowserHistory()
    history.push('a')
    history.push('b')
    history.push('c')

    for url in history.get_urls:
        print(url)