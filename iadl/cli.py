# iad/cli.py
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
    """Extract the item ID from an Internet Archive URL."""
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    if path.startswith('details/'):
        return path.split('/')[1]
    return path

def get_file_extensions(args):
    """Get file extensions based on provided arguments."""
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
    
    if not any([args.archive, args.video, args.audio, args.streaming, args.audiobooks,
                args.disk_images, args.documents, args.executables, args.data, args.web,
                args.comics, args.ebooks, args.pictures, args.containers, args.torrent]):
        return None
    
    return file_extensions

def main():
    """Main function to parse arguments and run the scraper"""
    try:
        parser = argparse.ArgumentParser(description='Download files from Internet Archive.')
        
        # Check if show-links is present in any form (-s or --show-links)
        show_links_present = any(arg in sys.argv for arg in ['-s', '--show-links'])
        
        # Primary arguments
        parser.add_argument('-u', '--url', required=True, help='Internet Archive URL')
        parser.add_argument('-d', '--dest', required=not show_links_present,
                          help='Destination folder (not required with -s/--show-links)')
        parser.add_argument('-l', '--limit', type=int, default=0, help='Limit files to download')
        parser.add_argument('-s', '--show-links', action='store_true', 
                          help='Display links without downloading')
        parser.add_argument('-c', '--concurrent', type=int, default=1,
                          help='Max concurrent downloads')
        
        # Category filters (using more distinct single letters)
        parser.add_argument('-z', '--archive', action='store_true', help='Archive formats')
        parser.add_argument('-v', '--video', action='store_true', help='Video formats')
        parser.add_argument('-m', '--audio', action='store_true', help='Audio formats')
        parser.add_argument('-t', '--streaming', action='store_true', help='Streaming formats')
        parser.add_argument('-b', '--audiobooks', action='store_true', help='Audiobook formats')
        parser.add_argument('-i', '--disk_images', action='store_true', help='Disk images')
        parser.add_argument('-o', '--documents', action='store_true', help='Documents')
        parser.add_argument('-x', '--executables', action='store_true', help='Executables')
        parser.add_argument('-f', '--data', action='store_true', help='Data files')
        parser.add_argument('-w', '--web', action='store_true', help='Web files')
        parser.add_argument('-k', '--comics', action='store_true', help='Comics')
        parser.add_argument('-e', '--ebooks', action='store_true', help='eBooks')
        parser.add_argument('-p', '--pictures', action='store_true', help='Pictures')
        parser.add_argument('-n', '--containers', action='store_true', help='Containers')
        parser.add_argument('-r', '--torrent', action='store_true', help='Torrents')
        
        args = parser.parse_args()
        
        # Extract item ID
        item_id = extract_item_id(args.url)
        print(f"Extracted item ID: {item_id}")
        
        # Get file extensions
        file_extensions = get_file_extensions(args)
        if file_extensions:
            print(f"Filtering files with extensions: {file_extensions}")
        else:
            print("Showing all files (no filters applied).")
        
        # Create scraper
        scraper = InternetArchiveScraper(url="https://archive.org", item_id=item_id)
        file_urls = scraper.get_file_links(file_extensions=file_extensions, 
                                         show_links=args.show_links)
        
        if not file_urls:
            print("No files found. Exiting.")
            return
        
        if args.limit > 0:
            file_urls = file_urls[:args.limit]
            print(f"Limiting to {args.limit} files")
        
        if args.show_links:
            print("\nFinished displaying links. No files were downloaded.")
            return
        
        if not args.dest:
            print("\nError: Destination folder is required for downloads.")
            return
        
        downloader = FileDownloader(args.dest, args.concurrent)
        downloader.download_files(file_urls)
    
    except KeyboardInterrupt:
        print("\nExecution canceled by user. Exiting gracefully.")