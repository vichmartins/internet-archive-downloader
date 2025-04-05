# Archive formats
ARCHIVE_EXTENSIONS = ['.7z', '.zip', '.rar', '.tar', '.gz', '.xz',
                      '.lz', '.lzma', '.zst', '.tgz', '.tbz', '.tb2', '.tbz2'
                      '.tar.gz', '.tar.bz2', '.tar.xz', '.tar.lzma', '.tar.zst',
                      '.tar.lz', '.tar.lzma', '.tar.zst', '.tar.xz', '.tar.bzip2',
                      '.tar.lzip', '.tar.lzop', '.tar.zlib', 'cab', 'arj', 'ace',
                      'zoo', 'zipx', 'war', 'ear', 'tar.lzo', 'lzh',
                      'lha', 'pax', 'cpio', 'bzip', 'bzip2', 'tbz', 'tb2', 'tbz2',
                      'tbz2', 'tar.lzop', 'tar.lzip', 'tar.zlib', 'tar.bzip2', 'uue'
                    ]

# Video formats
VIDEO_EXTENSIONS = ['.avi', '.mov', '.wmv', '.mpg', '.mpeg', '.mp4',
                    '.mkv', '.webm', '.flv', '.3gp', '.m4v', '.vob', '.ogv'
                    '.gifv', '.mng', '.mts', '.m2ts', '.ts', '.divx', '.dv', '.f4v',
                    '.f4p', '.f4a', '.f4b', '.h264', '.h265', '.hevc', '.vp8', '.vp9', '.av1', '.xvid',
                    '.qt', '.3gp', '.svi', '.rm', '.rmvb', '.asf', '.drc', '.mjpeg', '.mjpg', '.mp2v', '.mp4v',
                    '.mpv', '.nsv', '.ogm', '.roq', '.srt', '.sub', '.idx', '.vtt']

# Audio formats
AUDIO_EXTENSIONS = ['.mp3', '.flac', 'alac', '.wav', '.aac', '.ogg', '.wma', '.opus', '.m4p', '.aiff']

# Streaming formats
STREAMING_EXTENSIONS = ['.m3u8', '.m3u', '.ts', '.m4s', '.mpd']

# Audiobook formats
AUDIOBOOK_EXTENSIONS = ['.m4b', 'm4p', '.m4a', 'm4b', '.aa', '.aax']

# Disk image formats
DISK_IMAGE_EXTENSIONS = ['.iso', '.img', '.bin', '.cue', '.dmg','.nrg', '.toast', 'raw', 
                         'qcow', 'qcow2', '.vmdk', '.vdi', '.vhd', '.vhdx', 'hdd', 'hdi']

# Document formats
DOCUMENT_EXTENSIONS = ['.txt', '.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx']

# Executable formats
EXECUTABLE_EXTENSIONS = ['.exe', '.msi', '.apk', '.deb', '.rpm', 'jar',]

# Data formats
DATA_EXTENSIONS = ['.txt', '.csv', '.json', '.xml', '.sqlite']

# Web formats
WEB_EXTENSIONS = ['.html', '.css', '.js']

# Comic formats
COMIC_EXTENSIONS = ['cbr', 'cbz', 'cb7', 'cbt', 'cba']

# eBook formats
EBOOK_EXTENSIONS = ['epub', '.mobi', 'lrf', 'lrx', 'pkg', 'opf', 'lit', 'ps',
                    'djvu', '.azw', '.azw3', 'ibooks', 'kf8', 'kfx', 'opf', '.prc',
                    'pdb', '.prc', '.fb2', 'fbz', '.fb2.zip', 'xeb', '.xhtml', 'ceb'
]

# Help formats
HELP_EXTENSIONS = ['chm', '.hlp']

# Picture formats
PICTURE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webm', '.jpeg2000', '.webp', '.hdr', '.heif', 
                      '.avif', '.jpegxl', '.tiff', '.bmp', '.ppm', '.pgm', '.pbm', '.pnm'
]

# Container formats for raster graphics
CONTAINER_EXTENSIONS = ['.afphoto', '.cd5', '.clip', '.cpt', '.kra', '.mdp', '.pdn', '.pld', '.psd', '.psp', '.sai', '.xcf'
]

# Torrent formats
TORRENT_EXTENSIONS = ['.torrent']

# All extensions
ALL_EXTENSIONS = (
    ARCHIVE_EXTENSIONS +
    VIDEO_EXTENSIONS +
    AUDIO_EXTENSIONS +
    STREAMING_EXTENSIONS +
    AUDIOBOOK_EXTENSIONS +
    DISK_IMAGE_EXTENSIONS +
    DOCUMENT_EXTENSIONS +
    EXECUTABLE_EXTENSIONS +
    DATA_EXTENSIONS +
    WEB_EXTENSIONS +
    COMIC_EXTENSIONS +
    EBOOK_EXTENSIONS +
    HELP_EXTENSIONS +
    PICTURE_EXTENSIONS +
    CONTAINER_EXTENSIONS +
    TORRENT_EXTENSIONS
)