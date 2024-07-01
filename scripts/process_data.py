import os
import json
import asyncio

source_dir = "data/Keep"
destination_dir = "data/KeepProcessed"

os.makedirs(destination_dir, exist_ok=True)


async def process_file(filename, index):
    file_path = os.path.join(source_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        new_data = {
            "textContent": data.get("textContent", ""),
            "title": data.get("title", ""),
        }

        destination_filename = f"{index}.json"
        destination_file_path = os.path.join(destination_dir, destination_filename)

        with open(destination_file_path, "w", encoding="utf-8") as new_file:
            json.dump(new_data, new_file, ensure_ascii=False, indent=4)


async def process_files():
    tasks = []
    index = 1
    for filename in os.listdir(source_dir):
        if filename.endswith(".json"):
            task = asyncio.create_task(process_file(filename, index))
            tasks.append(task)
            index += 1
    await asyncio.gather(*tasks)


asyncio.run(process_files())
