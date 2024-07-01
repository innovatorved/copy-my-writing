import asyncio
import aiofiles
import os
import json

processed_files_dir = "data/KeepProcessed"
target_json_path = "data/writing_samples.json"


async def read_json_file(file_path):
    async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
        content = await file.read()
        return json.loads(content)


async def write_json_file(file_path, data):
    async with aiofiles.open(file_path, "w", encoding="utf-8") as file:
        await file.write(json.dumps(data, ensure_ascii=False, indent=4))


async def combine_json_files(processed_files_dir, target_json_path):
    combined_data = []

    for filename in os.listdir(processed_files_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(processed_files_dir, filename)
            data = await read_json_file(file_path)
            data["textContent"] = " ".join(data["textContent"].split())
            data["textContent"] = data["textContent"].replace("#its_ved", "")
            combined_data.append(data)

    target_data = {"writing_samples": []}
    target_data["writing_samples"].extend(combined_data)

    await write_json_file(target_json_path, target_data)


w
asyncio.run(combine_json_files(processed_files_dir, target_json_path))
