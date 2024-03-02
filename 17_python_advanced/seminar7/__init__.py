def rename_files(desired_name, num_digits, source_ext, target_ext):
    arr = []
    count = 1
    test_folder = Path("test_folder")
    for file in test_folder.iterdir():
        if file.is_file():
            file_name = file.name
            *_, file_ext = file_name.split(".")
            if file_ext == source_ext:
                num_str = f"{count}"
                while len(num_str) < num_digits:
                    num_str = "0" + num_str
                new_file_name = f"{desired_name}{num_str}.{target_ext}"
                file.rename(test_folder / new_file_name)
                arr.append(new_file_name)
                count += 1