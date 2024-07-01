# Copy My Writing

Copy My Writing is a command-line tool for generating content based on your personal writing style.

## Installation

1. Clone this repository.
2. Run `pip install -e .` in the project directory.
3. Set up your `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   WRITING_SAMPLES_PATH=path/to/your/writing_samples.json
   ```

## Usage

Generate content:
```
copy_my_writing generate "Your topic here"
```

Analyze current style:
```
copy_my_writing analyze-style
```

For more information, use the `--help` flag:
```
copy_my_writing --help
```

## Data License

All data contained within the `data` folder, including but not limited to files within `data/Keep` and `data/KeepProcessed`, is considered private and confidential. This data is not covered by the MIT License that applies to the source code of this project. Any use, distribution, reproduction, or sharing of this data, in whole or in part, is strictly prohibited without explicit written permission from the copyright holder.

## Configuration

The configuration for Copy My Writing is stored in the `.env` file. It contains the OpenAI API key and the path to the writing samples JSON file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.