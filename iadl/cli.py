import argparse
import sys
from urllib.parse import urlparse
from iadl.scraper import InternetArchiveScraper
from iadl.downloader import FileDownloader
from iadl.extensions import (
    ARCHIVE_EXTENSIONS, VIDEO_EXTENSIONS, AUDIO_EXTENSIONS, STREAMING_EXTENSIONS,
    AUDIOBOOK_EXTENSIONS, DISK_IMAGE_EXTENSIONS, DOCUMENT_EXTENSIONS, EXECUTABLE_EXTENSIONS,
    DATA_EXTENSIONS, WEB_EXTENSIONS, COMIC_EXTENSIONS, EBOOK_EXTENSIONS, PICTURE_EXTENSIONS, 
    CONTAINER_EXTENSIONS, TORRENT_EXTENSIONS, ALL_EXTENSIONS
)

def extract_item_id(url):
    """
    Extract the item ID from an Internet Archive URL.
    Example: https://archive.org/details/rr-sega-mega-cd → rr-sega-mega-cd
    """
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    if path.startswith('details/'):
        # Extract the item ID from the path
        return path.split('/')[1]
    else:
        # Assume the path is the item ID
        return path

def get_file_extensions(args):
    """
    Get the list of file extensions based on the provided arguments.
    If no specific category is selected, return None to indicate all files should be downloaded.
    """
    file_extensions = []
    
    if args.archive:
        file_extensions.extend(ARCHIVE_EXTENSIONS)
    if args.video:
        file_extensions.extend(VIDEO_EXTENSIONS)
    if args.audio:
        file_extensions.extend(AUDIO_EXTENSIONS)
    if args.streaming:
        file_extensions.extend(STREAMING_EXTENSIONS)
    if args.audiobooks:
        file_extensions.extend(AUDIOBOOK_EXTENSIONS)
    if args.disk_images:
        file_extensions.extend(DISK_IMAGE_EXTENSIONS)
    if args.documents:
        file_extensions.extend(DOCUMENT_EXTENSIONS)
    if args.executables:
        file_extensions.extend(EXECUTABLE_EXTENSIONS)
    if args.data:
        file_extensions.extend(DATA_EXTENSIONS)
    if args.web:
        file_extensions.extend(WEB_EXTENSIONS)
    if args.comics:
        file_extensions.extend(COMIC_EXTENSIONS)
    if args.ebooks:
        file_extensions.extend(EBOOK_EXTENSIONS)
    if args.pictures:
        file_extensions.extend(PICTURE_EXTENSIONS)
    if args.containers:
        file_extensions.extend(CONTAINER_EXTENSIONS)
    if args.torrent:
        file_extensions.extend(TORRENT_EXTENSIONS)
    
    # If no specific category is selected, return None to indicate all files should be downloaded
    if not any([args.archive, args.video, args.audio, args.streaming, args.audiobooks, 
                args.disk_images, args.documents, args.executables, args.data, args.web, 
                args.comics, args.ebooks, args.pictures, args.containers, args.torrent]):
        return None
    
    return file_extensions

def main():
    """Main function to parse arguments and run the scraper"""
    try:
        parser = argparse.ArgumentParser(description='Download files from Internet Archive.')
        
        # Primary arguments with both short and long forms
        parser.add_argument('-u', '--url', required=True, help='Full URL of the Internet Archive collection')
        parser.add_argument('-d', '--dest', required='--show-links' not in sys.argv, 
                          help='Destination folder for downloaded files (not required if only showing links)')
        parser.add_argument('-l', '--limit', type=int, default=0, help='Limit number of files to download (0 for all)')
        parser.add_argument('-s', '--show-links', action='store_true', help='Display file links without downloading')
        parser.add_argument('-c', '--concurrent', type=int, default=1, help='Maximum concurrent downloads (default: 1)')
        
        # Category filters with short options
        parser.add_argument('-a', '--archive', action='store_true', help='Download only archive formats')
        parser.add_argument('-v', '--video', action='store_true', help='Download only video formats')
        parser.add_argument('-m', '--audio', action='store_true', help='Download only audio formats (m for music)')
        parser.add_argument('-t', '--streaming', action='store_true', help='Download only streaming formats')
        parser.add_argument('-b', '--audiobooks', action='store_true', help='Download only audiobook formats')
        parser.add_argument('-i', '--disk_images', action='store_true', help='Download only disk image formats')
        parser.add_argument('-o', '--documents', action='store_true', help='Download only document formats')
        parser.add_argument('-e', '--executables', action='store_true', help='Download only executable formats')
        parser.add_argument('-f', '--data', action='store_true', help='Download only data formats')
        parser.add_argument('-w', '--web', action='store_true', help='Download only web formats')
        parser.add_argument('-x', '--comics', action='store_true', help='Download only comic formats')
        parser.add_argument('-k', '--ebooks', action='store_true', help='Download only eBook formats')
        parser.add_argument('-p', '--pictures', action='store_true', help='Download only picture formats')
        parser.add_argument('-n', '--containers', action='store_true', help='Download only container formats')
        parser.add_argument('-r', '--torrent', action='store_true', help='Download only torrent files')
        
        args = parser.parse_args()
        
        # Extract the item ID from the URL
        item_id = extract_item_id(args.url)
        print(f"Extracted item ID: {item_id}")
        
        # Get the list of file extensions based on the provided arguments
        file_extensions = get_file_extensions(args)
        if file_extensions is not None:
            print(f"Filtering files with extensions: {file_extensions}")
        else:
            print("Showing all files (no filters applied).")
        
        # Create scraper object
        scraper = InternetArchiveScraper(url="https://archive.org", item_id=item_id)
        
        # Get list of file URLs
        file_urls = scraper.get_file_links(file_extensions=file_extensions, show_links=args.show_links)
        
        if not file_urls:
            print("No files found. Exiting.")
            return
        
        # Apply limit if specified
        if args.limit > 0:
            file_urls = file_urls[:args.limit]
            print(f"Limiting to {args.limit} files")
        
        # If only showing links, exit here
        if args.show_links:
            print("\nFinished displaying links. No files were downloaded.")
            return
        
        # Only proceed with downloads if destination is specified
        if not args.dest:
            print("\nError: Destination folder is required for downloads.")
            return
        
        # Create downloader object and download files
        downloader = FileDownloader(args.dest, args.concurrent)
        downloader.download_files(file_urls)
    
    except KeyboardInterrupt:
        print("\nExecution canceled by user. Exiting gracefully.")