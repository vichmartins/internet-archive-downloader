
# Internet Archive Downloader (iadl)

A Python package to scrape and download files from the Internet Archive.

## Installation

You can install the package using `pip`:

```bash
pip install iadl
```

## Usage

### Basic Usage

To download all files from an Internet Archive collection:

```bash
iadl --url https://archive.org/details/some-collection --dest ./downloads
```

### Filter by File Type

You can filter files by specific types using the following arguments:

- **Download only archive files**  (e.g.,  `.zip`,  `.rar`):

    ```bash
    iadl --url https://archive.org/details/some-collection --dest ./downloads --archive
    ```

- **Download only video files**  (e.g.,  `.mp4`,  `.avi`):

    ```bash
    iadl --url https://archive.org/details/some-collection --dest ./downloads --video
    ```

- **Download only audio files**  (e.g.,  `.mp3`,  `.flac`):

```bash
    iadl --url https://archive.org/details/some-collection --dest ./downloads --audio
```

### Limit the Number of Files

To limit the number of files downloaded:

```bash
iadl --url https://archive.org/details/some-collection --dest ./downloads --limit 5
```

### Show File Links

To display the direct file links of each file in the terminal:

```bash
iadl --url https://archive.org/details/some-collection --show-links
```

### Combine Filters

You can combine multiple filters. For example, to download only video and audio files:

```bash
iadl --url https://archive.org/details/some-collection --dest ./downloads --video --audio
```

### Simultaneous Downloads

To download multiple files at the same time through separate processes. Setting the number will determine how many files at any one given moment until its finished. ***Recommend 2-3, be nice to the servers.***

```bash
iadl --url https://archive.org/details/some-collection --dest ./downloads --audio --concurrent 3
```

### Help

For a full list of options, use the  `--help`  flag:

```bash
iadl --help
```

### Uninstall

If you wish to remove the dependencies ***(must be first otherwise*** `pip uninstall` ***will remove the uninstaller, IF YOU WANT THE DEPENDENCIES TO STAY, just skip this command.)***:

```bash
iadl-cleanup
```

To remove the module:

```bash
pip uninstall iadl
```

***IF*** you messed up and ran ```pip uninstall iadl``` first, and still want the dependencies removed, no problem just reinstall the package again ```pip install iadl``` and repeat the above 2 commands in order.

### Install in Virtual Enviroment

#### For Windows

```bash
python -m venv env
env\Scripts\Activate.ps1
pip install iadl
```

When done:

```bash
deactivate
```

#### For Linux

```bash
python3 -m venv env
source env/Scripts/activate
pip install iadl
```

When done:

```bash
deactivate
```
