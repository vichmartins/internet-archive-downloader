
# Internet Archive Scraper (IAS)

A Python package to scrape and download files from the Internet Archive.


## Installation

You can install the package using `pip`:

```bash
pip install ias
```
## Usage

### Basic Usage

To download all files from an Internet Archive collection:
```
ias --url https://archive.org/details/some-collection --dest ./downloads
```
### Filter by File Type

You can filter files by specific types using the following arguments:

-   **Download only archive files**  (e.g.,  `.zip`,  `.rar`):
    ```
    ias --url https://archive.org/details/some-collection --dest ./downloads --archive
    ```
-   **Download only video files**  (e.g.,  `.mp4`,  `.avi`):
    ```
    ias --url https://archive.org/details/some-collection --dest ./downloads --video
    ```
-   **Download only audio files**  (e.g.,  `.mp3`,  `.flac`):
```
    ias --url https://archive.org/details/some-collection --dest ./downloads --audio
``` 

### Limit the Number of Files

To limit the number of files downloaded:
```
ias --url https://archive.org/details/some-collection --dest ./downloads --limit 5
```

### Show File Links

To display the direct file links of each file in the terminal:
```
ias --url https://archive.org/details/some-collection --dest ./downloads --show-links
```


### Combine Filters

You can combine multiple filters. For example, to download only video and audio files:
```
ias --url https://archive.org/details/some-collection --dest ./downloads --video --audio
```


### Simultaneous Downloads

To download multiple files at the same time through separate processes. Setting the number will determine how many files at any one given moment until its finished. ***Recommend 2-3, be nice to the servers.***
```
ias --url https://archive.org/details/some-collection --dest ./downloads --audio --concurrent 3
```


### Help

For a full list of options, use the  `--help`  flag:
```
ias --help
```

### Uninstall

If you wish to remove the dependencies ***(must be first otherwise*** `pip uninstall` ***will remove the uninstaller, IF YOU WANT THE DEPENDENCIES TO STAY, just skip this command.)***:
```bash
ias-cleanup
```

To remove the module:
```bash
pip uninstall ias
```

***IF*** you messed up and ran ```pip uninstall ias``` first, and still want the dependencies removed, no problem just reinstall the package again ```pip install ias``` and repeat the above 2 commands in order.