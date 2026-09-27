from pathlib import Path
import shutil
import time
import sys


# ============================================================
# TERMINAL COLORS
# ============================================================

RESET = "\033[0m"
BOLD = "\033[1m"

WHITE = "\033[97m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"

# Disable colors when output is redirected
if not sys.stdout.isatty():
    RESET = BOLD = WHITE = CYAN = BLUE = GREEN = YELLOW = RED = MAGENTA = ""


# ============================================================
# TERMINAL SETTINGS
# ============================================================

WIDTH = 72

BAR_WIDTH = 20

# Fixed columns make every file row line up correctly
STATUS_WIDTH = 7
COUNT_WIDTH = 6
PERCENT_WIDTH = 4
FILENAME_WIDTH = 42
SIZE_WIDTH = 11


# ============================================================
# FILE CATEGORIES
# ============================================================

CATEGORIES = {
    "Images": (
        ".jpg", ".jpeg", ".png", ".gif", ".webp",
        ".bmp", ".svg", ".ico", ".tiff", ".tif"
    ),

    "Documents": (
        ".pdf", ".doc", ".docx", ".txt", ".rtf",
        ".odt", ".xls", ".xlsx", ".ppt", ".pptx",
        ".csv"
    ),

    "Archives": (
        ".zip", ".rar", ".7z", ".tar", ".gz",
        ".bz2", ".xz", ".iso"
    ),

    "Videos": (
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".m4v"
    ),

    "Audio": (
        ".mp3", ".wav", ".m4a", ".aac", ".flac",
        ".ogg", ".wma"
    ),
}


# ============================================================
# CATEGORY COLORS
# ============================================================

CATEGORY_COLORS = {
    "Images": MAGENTA,
    "Documents": BLUE,
    "Archives": YELLOW,
    "Videos": CYAN,
    "Audio": GREEN,
    "Others": WHITE,
}


# ============================================================
# SIZE FORMATTER
# ============================================================

def format_size(size_bytes):
    """
    Convert bytes to a readable size.
    """

    if size_bytes < 1024:
        return f"{size_bytes} B"

    if size_bytes < 1024 ** 2:
        return f"{size_bytes / 1024:.2f} KB"

    if size_bytes < 1024 ** 3:
        return f"{size_bytes / (1024 ** 2):.2f} MB"

    if size_bytes < 1024 ** 4:
        return f"{size_bytes / (1024 ** 3):.2f} GB"

    return f"{size_bytes / (1024 ** 4):.2f} TB"


# ============================================================
# TERMINAL HELPERS
# ============================================================

def line(char="=", width=WIDTH):
    print(f"{CYAN}{char * width}{RESET}")


def print_header():

    print()

    line("=")

    print(
        f"{CYAN}{BOLD}"
        f"{'DOWNLOAD ORGANIZER':^{WIDTH}}"
        f"{RESET}"
    )

    print(
        f"{WHITE}"
        f"{'Automatic File Organization':^{WIDTH}}"
        f"{RESET}"
    )
    print(
        f"{WHITE}"
        f"{'Author: PrimeRonin(skm-hpc)':^{WIDTH}}"
        f"{RESET}"
    )

    line("=")

    print()


def print_section(title):

    print()

    line("-")

    print(
        f"{CYAN}{BOLD}"
        f"{title:^{WIDTH}}"
        f"{RESET}"
    )

    line("-")


def get_category(extension):

    extension = extension.lower()

    for category, extensions in CATEGORIES.items():

        if extension in extensions:
            return category

    return "Others"


def format_filename(filename):

    """
    Keep filenames inside the fixed terminal column.
    """

    if len(filename) <= FILENAME_WIDTH:
        return filename

    return filename[:FILENAME_WIDTH - 3] + "..."


# ============================================================
# INLINE PROGRESS BAR
# ============================================================

def make_progress_bar(current, total):

    if total <= 0:
        return "-" * BAR_WIDTH

    filled = int(
        BAR_WIDTH * current / total
    )

    return (
        "#"
        * filled
        +
        "-"
        * (BAR_WIDTH - filled)
    )


# ============================================================
# FILE OUTPUT
# ============================================================

def print_file_result(
    index,
    total,
    status,
    filename,
    size,
    category
):

    percentage = int(
        (index / total) * 100
    )

    bar = make_progress_bar(
        index,
        total
    )

    # --------------------------------------------------------
    # Status color
    # --------------------------------------------------------

    if status == "OK":
        status_color = GREEN

    elif status == "SKIP":
        status_color = YELLOW

    else:
        status_color = RED

    # --------------------------------------------------------
    # Category color
    # --------------------------------------------------------

    category_color = CATEGORY_COLORS.get(
        category,
        WHITE
    )

    # --------------------------------------------------------
    # Format filename
    # --------------------------------------------------------

    display_name = format_filename(
        filename
    )

    # --------------------------------------------------------
    # Print ONE consistent row
    # --------------------------------------------------------

    print(
        f"{WHITE}[{bar}]{RESET} "
        f"{GREEN}{percentage:3d}%{RESET} "
        f"{WHITE}{index:>2}/{total:<2}{RESET} "
        f"{status_color}[{status:<4}]{RESET} "
        f"{display_name:<{FILENAME_WIDTH}} "
        f"{GREEN}{size:>{SIZE_WIDTH}}{RESET} "
        f"{CYAN}->{RESET} "
        f"{category_color}{category}/{RESET}"
    )


# ============================================================
# SUMMARY
# ============================================================

def print_summary(
    stats,
    total_files,
    total_size,
    elapsed
):

    print_section(
        "ORGANIZATION SUMMARY"
    )

    print()

    categories = (
        "Images",
        "Documents",
        "Videos",
        "Audio",
        "Archives",
        "Others",
    )

    for category in categories:

        count = stats[category]["count"]

        size = stats[category]["size"]

        if count == 0:
            continue

        color = CATEGORY_COLORS[
            category
        ]

        print(
            f"  {color}{category:<12}{RESET}"
            f" : {WHITE}{BOLD}{count:>4}{RESET}"
            f" file(s)"
            f"  {GREEN}{format_size(size):>11}{RESET}"
        )

    print()

    line("-")

    print(
        f"  {GREEN}[OK] Successfully moved : "
        f"{BOLD}{stats['moved']['count']}{RESET}"
        f"  {GREEN}{format_size(stats['moved']['size'])}{RESET}"
    )

    print(
        f"  {YELLOW}[--] Skipped             : "
        f"{BOLD}{stats['skipped']['count']}{RESET}"
        f"  {YELLOW}{format_size(stats['skipped']['size'])}{RESET}"
    )

    print(
        f"  {RED}[!!] Errors              : "
        f"{BOLD}{stats['errors']['count']}{RESET}"
        f"  {RED}{format_size(stats['errors']['size'])}{RESET}"
    )

    print()

    print(
        f"  {CYAN}{BOLD}"
        f"[##] Total files scanned : "
        f"{total_files}"
        f"{RESET}"
    )

    print(
        f"  {CYAN}{BOLD}"
        f"[MB] Total data scanned  : "
        f"{format_size(total_size)}"
        f"{RESET}"
    )

    print(
        f"  {WHITE}"
        f"[TIME] Processing time   : "
        f"{BOLD}{elapsed:.2f} seconds"
        f"{RESET}"
    )

    print()


# ============================================================
# ORGANIZE DOWNLOADS
# ============================================================

def organize_downloads(downloads_path):

    # --------------------------------------------------------
    # Validate Downloads folder
    # --------------------------------------------------------

    if not downloads_path.exists():

        print(
            f"{RED}[ERROR] Downloads folder not found:{RESET}"
        )

        print(
            f"        {WHITE}{downloads_path}{RESET}"
        )

        return

    if not downloads_path.is_dir():

        print(
            f"{RED}[ERROR] Path is not a directory:{RESET}"
        )

        print(
            f"        {WHITE}{downloads_path}{RESET}"
        )

        return

    # --------------------------------------------------------
    # Find files
    # --------------------------------------------------------

    files = [
        file
        for file in downloads_path.iterdir()
        if file.is_file()
    ]

    total_files = len(files)

    # --------------------------------------------------------
    # Calculate file sizes
    # --------------------------------------------------------

    file_sizes = {}

    total_size = 0

    for file in files:

        try:
            size = file.stat().st_size

        except OSError:
            size = 0

        file_sizes[file] = size

        total_size += size

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    stats = {

        "moved": {
            "count": 0,
            "size": 0,
        },

        "skipped": {
            "count": 0,
            "size": 0,
        },

        "errors": {
            "count": 0,
            "size": 0,
        },

        "Images": {
            "count": 0,
            "size": 0,
        },

        "Documents": {
            "count": 0,
            "size": 0,
        },

        "Archives": {
            "count": 0,
            "size": 0,
        },

        "Videos": {
            "count": 0,
            "size": 0,
        },

        "Audio": {
            "count": 0,
            "size": 0,
        },

        "Others": {
            "count": 0,
            "size": 0,
        },
    }

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    print_header()

    print(
        f"{CYAN}{BOLD}"
        "Downloads folder"
        f"{RESET}"
    )

    print(
        f"  {WHITE}{downloads_path}{RESET}"
    )

    print()

    print(
        f"{CYAN}{BOLD}"
        f"Files detected:{RESET} "
        f"{WHITE}{BOLD}{total_files}{RESET}"
    )

    print(
        f"{CYAN}{BOLD}"
        f"Total size:{RESET} "
        f"{WHITE}{BOLD}{format_size(total_size)}{RESET}"
    )

    # --------------------------------------------------------
    # Empty folder
    # --------------------------------------------------------

    if total_files == 0:

        print()

        print(
            f"{GREEN}{BOLD}"
            "[OK] Downloads folder is already organized."
            f"{RESET}"
        )

        print()

        return

    # --------------------------------------------------------
    # Start
    # --------------------------------------------------------

    print()

    print(
        f"{CYAN}{BOLD}"
        "Starting organization..."
        f"{RESET}"
    )

    print()

    start_time = time.time()

    # --------------------------------------------------------
    # Process files
    # --------------------------------------------------------

    for index, file in enumerate(
        files,
        start=1
    ):

        size_bytes = file_sizes[file]

        size_display = format_size(
            size_bytes
        )

        category = get_category(
            file.suffix
        )

        destination_folder = (
            downloads_path / category
        )

        destination_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        destination = (
            destination_folder / file.name
        )

        # ----------------------------------------------------
        # Already exists
        # ----------------------------------------------------

        if destination.exists():

            stats["skipped"]["count"] += 1

            stats["skipped"]["size"] += (
                size_bytes
            )

            print_file_result(
                index,
                total_files,
                "SKIP",
                file.name,
                size_display,
                category
            )

            continue

        # ----------------------------------------------------
        # Move
        # ----------------------------------------------------

        try:

            shutil.move(
                str(file),
                str(destination)
            )

            stats["moved"]["count"] += 1

            stats["moved"]["size"] += (
                size_bytes
            )

            stats[category]["count"] += 1

            stats[category]["size"] += (
                size_bytes
            )

            print_file_result(
                index,
                total_files,
                "OK",
                file.name,
                size_display,
                category
            )

        except OSError as error:

            stats["errors"]["count"] += 1

            stats["errors"]["size"] += (
                size_bytes
            )

            print_file_result(
                index,
                total_files,
                "ERR",
                file.name,
                size_display,
                category
            )

            print(
                f"        {RED}{error}{RESET}"
            )

    # --------------------------------------------------------
    # Finish
    # --------------------------------------------------------

    elapsed = (
        time.time() - start_time
    )

    print_summary(
        stats,
        total_files,
        total_size,
        elapsed
    )

    # --------------------------------------------------------
    # Final status
    # --------------------------------------------------------

    if stats["errors"]["count"] == 0:

        print(
            f"{GREEN}{BOLD}"
            "[SUCCESS] Download organization completed."
            f"{RESET}"
        )

    else:

        print(
            f"{YELLOW}{BOLD}"
            "[WARNING] Organization completed with errors."
            f"{RESET}"
        )

    print()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    # Automatically detect current user's Downloads folder.

    downloads_folder = (
        Path.home() / "Downloads"
    )

    organize_downloads(
        downloads_folder
    )
