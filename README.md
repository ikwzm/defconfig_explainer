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

#### Example 1

```console
shell$ cd linux-6.1.108
shell$ defconfig-explainer --arch arm64 --cross-compile aarch64-linux-gnu- arch/arm64/configs/defconfig -o new_defconfig
```

#### Example 2

```console
shell$ cd linux-6.1.108
shell$ cat <<EOT >> add_config
CONFIG_DMABUF_HEAPS=y
CONFIG_DMABUF_HEAPS_SYSTEM=y
CONFIG_DMABUF_HEAPS_CMA=y
EOT
shell$ defconfig-explainer --arch arm64 --cross-compile aarch64-linux-gnu- -r -O print-help -O print-location -p arch/arm64/configs/defconfig -m add_defconfig
## =============================================================================
## Device Drivers
## =============================================================================
## drivers/Kconfig : 2
##

### ----------------------------------------------------------------------------
### DMABUF options
### ----------------------------------------------------------------------------
### drivers/dma-buf/Kconfig : 2
###

#### 
#### DMA-BUF Userland Memory Heaps
#### 
#### help
####     Choose this option to enable the DMA-BUF userland memory heaps.
####     This options creates per heap chardevs in /dev/dma_heap/ which
####     allows userspace to allocate dma-bufs that can be shared
####     between drivers.
####
#### drivers/dma-buf/Kconfig : 68
####
CONFIG_DMABUF_HEAPS=y

#### end of DMA-BUF Userland Memory Heaps

#### 
#### DMA-BUF System Heap
#### 
#### help
####     Choose this option to enable the system dmabuf heap. The system heap
####     is backed by pages from the buddy allocator. If in doubt, say Y.
####
#### drivers/dma-buf/heaps/Kconfig : 1
####
CONFIG_DMABUF_HEAPS_SYSTEM=y

#### 
#### DMA-BUF CMA Heap
#### 
#### help
####     Choose this option to enable dma-buf CMA heap. This heap is backed
####     by the Contiguous Memory Allocator (CMA). If your system has these
####     regions, you should say Y here.
####
#### drivers/dma-buf/heaps/Kconfig : 8
####
CONFIG_DMABUF_HEAPS_CMA=y

### end of DMABUF options

## end of Device Drivers
```

License
----------------------------------------------------------------------------------

This project is licensed under the BSD 2-Clause License. See the [LICENSE](./LICENSE) file for details.

