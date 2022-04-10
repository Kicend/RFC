import argparse
import os


def prepare_convert_process(source_path: str, destination_path: str):
    files_list = []
    for dir_name, dir_names, filenames in os.walk(source_path):
        for filename in filenames:
            files_list.append(os.path.join(dir_name, filename))

    for path in files_list:
        if path.count(".smf") != 1:
            del files_list[files_list.index(path)]

    converter(files_list, destination_path)


def converter(files_list: list, destination_path: str):
    for path in files_list:
        filename = path[path.rfind("\\") + 1:path.index(".smf")]
        with open(path, "rb") as f:
            content = f.read()
            converted_content = content[16:]

        with open(f"{destination_path}/{filename}.wav", "wb") as f:
            f.write(converted_content)


def parser():
    rfc_parser = argparse.ArgumentParser(prog="RFC",
                                         usage="%(prog)s SOURCE_DIR DESTINATION_DIR",
                                         description="Program do konwertowania plików smf na wav")
    rfc_parser.add_argument("SOURCE_DIR", type=str)
    rfc_parser.add_argument("DESTINATION_DIR", type=str)
    args = rfc_parser.parse_args()

    if args.SOURCE_DIR is not None and args.DESTINATION_DIR is not None:
        prepare_convert_process(args.SOURCE_DIR, args.DESTINATION_DIR)


if __name__ == "__main__":
    parser()
