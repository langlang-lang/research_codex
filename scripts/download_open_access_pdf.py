#!/usr/bin/env python3
import argparse
import pathlib
import sys
import urllib.request


def download_file(url: str, output: pathlib.Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    output.write_bytes(data)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Download an openly accessible PDF to a local path."
    )
    parser.add_argument("url", help="Direct PDF URL")
    parser.add_argument("output", help="Destination path")
    args = parser.parse_args()

    try:
        output = pathlib.Path(args.output)
        download_file(args.url, output)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
