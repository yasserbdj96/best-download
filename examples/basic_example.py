from best_download import download_file

tests = []
tests.append(("http://speedcheck.cdn.on.net/100meg.test", "100meg.test",
    "b89222456931da603c4c601208b6bf9d1a0d7cad3bde957163612074b04e6154"))
tests.append(("http://speedcheck.cdn.on.net/1000meg.test", "1000meg.test",
    "cfab8f3761126268a6715f90796a68074c3f57c3af48e0101776d211e7b5139e"))

# Github example doesn't support resuming
tests.append(("https://github.com/Nealcly/MuTual/archive/master.zip", "master.zip", None))

# Testing Accept-Encoding: identity (no gzip)
tests.append(("https://raw.githubusercontent.com/openai/gpt-3/master/data/two_digit_addition.jsonl",
             "two_digit_addition.jsonl", "75a54b7a3db3b23369df74fe440c23025f3d3c51f664300bd3d56632b2617b3d"))

def main():
    url, local_file_path, checksum = tests[0]

    print(f"Testing download of file {url} to {local_file_path}")
    print("Please cancel half way through and re-run this example to test resuming")
    download_file(url, local_file_path, checksum)

if __name__ == '__main__':
    main()

