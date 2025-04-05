import os
import requests
import time
from tqdm import tqdm
from urllib.parse import unquote
from concurrent.futures import ThreadPoolExecutor, as_completed, CancelledError

def human_readable_size(size_in_bytes):
    """
    Convert a file size in bytes to a human-readable format (e.g., B, KB, MB, GB, TB, PB, EB).
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} EB"  # Exabytes (just in case!)

class FileDownloader:
    def __init__(self, destination_folder, max_concurrent_downloads=1):
        """Initialize the downloader with a destination folder and maximum concurrent downloads"""
        self.destination_folder = os.path.abspath(destination_folder)
        self.max_concurrent_downloads = max_concurrent_downloads
        
        os.makedirs(self.destination_folder, exist_ok=True)
        print(f"Destination folder: {self.destination_folder}\n")
    
    def download_file(self, url, retries=3):
        """Download a file from URL to the destination folder with a progress bar"""

        file_name = unquote(os.path.basename(url))
        file_path = os.path.join(self.destination_folder, file_name)
        
        if os.path.exists(file_path):
            print(f"File '{file_name}' already exists. Skipping.")
            return
        
        for attempt in range(retries):
            try:
                # Make the request with a timeout
                print(f"Starting download (attempt {attempt + 1}): {file_name}")
                response = requests.get(url, stream=True, timeout=30)
                response.raise_for_status()  # Raise exception for bad responses
                
                # Get file size for progress reporting
                total_size_in_bytes = int(response.headers.get('content-length', 0))
                file_size = human_readable_size(total_size_in_bytes)
                print(f"File size: {file_size}")
                
                block_size = 8192  # 8 Kibibytes
                
                # Create a tqdm progress bar
                print(f"Downloading {file_name}...")
                progress_bar = tqdm(
                    total=total_size_in_bytes,
                    unit='iB',
                    unit_scale=True,
                    desc=file_name,
                    bar_format='{l_bar}{bar:30}{r_bar}',
                    ascii=False  # Use Unicode for the progress bar
                )
                
                # Open file for writing in binary mode
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=block_size):
                        if chunk:
                            progress_bar.update(len(chunk))
                            f.write(chunk)
                
                progress_bar.close()
                
                # Check if the download completed successfully
                if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                    print(f"ERROR: Downloaded file size does not match expected size for '{file_name}'")
                else:
                    print(f"Successfully downloaded '{file_name}'!")
                    break  # Exit the retry loop if successful
                
            except Exception as e:
                print(f"Error downloading '{file_name}' (attempt {attempt + 1}): {str(e)}")
                if attempt == retries - 1:
                    print(f"Failed to download '{file_name}' after {retries} attempts.")
                else:
                    print("Retrying...")
                    time.sleep(2)  # Wait before retrying
        
        # Add a slight delay between downloads to be nice to the server
        time.sleep(1)
    
    def download_files(self, file_urls):
        """Download multiple files from the provided list of URLs"""
        try:
            print(f"Found {len(file_urls)} files to download.\n")
            with ThreadPoolExecutor(max_workers=self.max_concurrent_downloads) as executor:
                futures = {executor.submit(self.download_file, url): url for url in file_urls}
                try:
                    for i, future in enumerate(as_completed(futures), 1):
                        url = futures[future]
                        try:
                            print(f"\nFile {i} of {len(file_urls)}")
                            future.result()
                        except Exception as e:
                            print(f"Error downloading {url}: {str(e)}")
                except KeyboardInterrupt:
                    print("\nCTRL + C detected. Cancelling all downloads...")
                    # Cancel all pending futures
                    for future in futures:
                        future.cancel()
                    # Wait for all futures to complete (cancelled or otherwise)
                    for future in futures:
                        try:
                            future.result()
                        except CancelledError:
                            pass  # Ignore cancellation errors
                    print("All downloads cancelled. Exiting gracefully.")
                    return  # Exit the function immediately
                
            print("\nAll downloads completed!")
        
        except KeyboardInterrupt:
            print("\nDownload canceled by user. Exiting gracefully.")