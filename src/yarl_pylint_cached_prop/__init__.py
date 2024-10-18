import yarl


def main() -> None:
    url = yarl.URL("https://example.com")
    if url.host == "foo":
        print("Host is foo")
    print("done.")
