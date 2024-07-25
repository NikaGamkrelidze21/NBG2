from settings import URL


def main():
    from components.http.http_main import http_main
    http_main(URL)


if __name__ == "__main__":
    main()
