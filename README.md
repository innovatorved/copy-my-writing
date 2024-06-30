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

## Configuration

The configuration for Copy My Writing is stored in the `.env` file. It contains the OpenAI API key and the path to the writing samples JSON file.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Please let me know if there is anything else I can help you with.