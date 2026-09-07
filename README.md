# Smaji Rime Zheng Generator

This project is a generator for creating Rime input method configuration files (schema and dictionary) for **Smaji Zheng (鄭碼)**. It automates the process of transforming structured glyph data into the YAML format required by the Rime input method engine.

## Features

- **Automatic Dictionary Generation**: Parses a directory of glyphs and generates a `.dict.yaml` file including input method code mappings, word lists, and composition data.
- **Schema Generation**: Creates a `.schema.yaml` file with predefined engine configurations, switches, and metadata.
- **Block Support**: Supports specific Unicode blocks (e.g., Version 13) as defined in the project configuration.
- **Customizable Output**: Allows users to specify the output name, version, description via command-line arguments.

## Prerequisites

- Python 3.x
- Rime based input method (for using the generated files)

## Usage

Run the generator using `generator.py`. You need to provide the input directory containing the glyph data and specify the version.

### Basic Command
```bash
python3 generator.py --version "1.0.0" --input /path/to/input_data --output /path/to/output_dir
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--cjkv_info` | Path of the cjkv\_info file | `.` |
| `--name` | Name of the generated code table | `smaji_zheng` |
| `--region` | Region to select characters from (comma-separated) | `China, Hong Kong, Japan, ...` |
| `--description` | Description of this zhengma input method | (Default description) |
| `--version` | **Required.** The version of the code table | |
| `--comment` | Comment for this version | |
| `--datetime` | Datetime of this version | (Current UTC) |
| `--input` | Directory of the input method collection | `.` |
| `--output` | Directory containing the new code table | `.` |
| `--verbose` | Generate verbose info during processing | `False` |

## Input Directory Structure

The generator expects the `--input` directory to be structured as follows:

```text
input_dir/
├── [core_hex]/
│   ├── [variation_hex]/
│   │   └── zhengma
│   └── ...
└── ...
```

- `core_hex`: The hexadecimal representation of the character's Unicode core (e.g., `4e00`).
- `variation_hex`: The hexadecimal representation of the variation (e.g., `0000`).
- `zhengma`: A file containing the ZhengMa code for that specific character/variation.

## Output

The generator will create a directory structure in the `--output` path:

- `description`: The input method description.
- `version`: The version string.
- `comment`: The version comment.
- `datetime`: The generation timestamp.
- `data/`:
    - `[name].dict.yaml`: The Rime dictionary file.
    - `[name].schema.yaml`: The Rime schema file.

## License

This project is licensed under the GPL2 license.
