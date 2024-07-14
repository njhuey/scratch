import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-k",
        "--key-file",
        default=None,
        help="Specify where your Benchling API key is stored. Default of None will try to use '~/.secrets/benchling.$USER.api_key'.",  # NOQA: E501
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = main()
    print(args.key_file)
