Defconfig Explainer
==================================================================================

Overview
----------------------------------------------------------------------------------

### Introduction

`defconfig-explainer` is a tool that analyzes the `defconfig` files used to build
the Linux kernel, etc., and provides **prompts and help** for each configuration
item to make it easier to understand.

### Features

  * Add **Kconfig description and help** included in the `defconfig` file
  * Use `Kconfiglib` to get information about Kconfig
  * Easily used as a command line tool

Installation
----------------------------------------------------------------------------------

### Install via `pip`


```sh
pip install git+https://github.com/ikwzm/defconfig_explainer.git
```

### Install Locally

You can also clone the repository and install it manually.

```sh
git clone https://github.com/ikwzm/defconfig_explainer.git
cd defconfig_explainer
pip install .
```

### Dependencies

This tool requires `Kconfiglib`.
It will be installed automatically with `pip install .`, but you can manually install it with:

```sh
pip install kconfiglib
```

Usage
----------------------------------------------------------------------------------

### Usage

```sh
defconfig-explainer [-h] [-m MERGE] [-p PRELOAD] [-k KCONFIG] [-o OUTPUT] [-a ARCH]
                     [--srcarch SRCARCH] [--srctree SRCTREE] [--cross-compile CROSS_COMPILE]
                     [--cc CC] [--ld LD] [-r] [-O OPTION] [--option-help] [-v]
                     [load_files [load_files ...]]
```

### Positional Arguments

| Argument                        | Description                                       |
|---------------------------------|---------------------------------------------------|
| `load_files`                    | Input defconfig files                             |

### Optional Arguments

| Option                          | Description                                       |
|---------------------------------|---------------------------------------------------|
| `-h, --help`                    | Show this help message and exit                   |
| `-m MERGE, --merge MERGE`       | Merge defconfig files                             |
| `-p PRELOAD, --preload PRELOAD` | Preload defconfig files                           |
| `-k KCONFIG, --kconfig KCONFIG` | Specify the Kconfig file (default: `Kconfig`)     |
| `-o OUTPUT, --output OUTPUT`    | Specify the output file (default: `stdout`)       |
| `-a ARCH, --arch ARCH`          | Set the target architecture (default: `None`)     |
| `--srcarch SRCARCH`             | Specify the source architecture                   |
| `--srctree SRCTREE`             | Set the source tree path (default: `.`)           |
| `--cross-compile CROSS_COMPILE` | Set the cross-compiler prefix (default: empty)    |
| `--cc CC`                       | Specify the C compiler command (default: `gcc`)   |
| `--ld LD`                       | Specify the linker command (default: `ld`)        |
| `-r, --recommended`             | Enable recommended print options                  |
| `-O OPTION, --option OPTION`    | Set an option in the format `KEY` or `kKEY=VALUE` |
| `--option-help`                 | Show help for `OPTION`                            |
| `-v, --verbose`                 | Enable verbose output                             |

### Example

```console
shell$ cd linux-6.1.108
shell$ defconfig-explainer --arch arm64 --cross-compile aarch64-linux-gnu- arch/arm64/configs/defconfig
```

License
----------------------------------------------------------------------------------

This project is licensed under the BSD 2-Clause License. See the [LICENSE](./LICENSE) file for details.

