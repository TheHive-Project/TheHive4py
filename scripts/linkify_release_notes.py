#!/usr/bin/env python3
"""
This script can be run in two modes:
1.  Default mode: Reads the release notes file, applies the link
    replacements, and writes the changes back to the file.
2.  Check mode (`--check`): Reads the file and reports if any changes
    are needed without modifying the file. It exits with a non-zero status
    code if changes are pending, making it suitable for CI/CD pipelines.
"""

import argparse
import re
import sys
from typing import Dict, List, Union

# --- Configuration and Constants ---
# By defining constants here, we avoid hardcoding these values multiple times
# and make the script easier to configure if the repository details change.
REPO_OWNER = "TheHive-Project"
REPO_NAME = "TheHive4py"
GITHUB_BASE_URL = f"https://github.com/{REPO_OWNER}/{REPO_NAME}"
RELEASE_NOTES_PATH = "docs/release-notes.md"

# --- Refactored Core Logic: Configuration-Driven Linkification ---
# Each dictionary contains:
#   - 'name': A unique identifier for the named capture group in the regex.
#   - 'pattern': The regex pattern to find the reference. It MUST contain a
#                named capture group `(?P<name>...)` that matches the 'name' key.
#   - 'replacement': An f-string template for the new Markdown link. It uses
#                    the named groups from the pattern to build the URL.
LINK_CONFIG: List[Dict[str, str]] = [
    {
        "name": "issue",
        "pattern": r" #(?P<issue>\d+)",
        "replacement": f" [#{'{{issue}}'}]({GITHUB_BASE_URL}/issues/{'{{issue}}'})",
    },
    {
        "name": "pr",
        "pattern": r" (?P<pr_url>https://github\.com/{}/{}/pull/(?P<pr_number>\d+))".format(
            REPO_OWNER, REPO_NAME
        ),
        "replacement": f" [#{'{{pr_number}}'}]({{{{pr_url}}}})",
    },
    {
        "name": "contributor",
        "pattern": r" @(?P<contributor>\w+)",
        "replacement": f" [@{{'{{contributor}}'}}](https://github.com/{'{{contributor}}'})",
    },
    {
        "name": "changelog",
        "pattern": r" (?P<changelog_url>https://github\.com/{}/{}/compare/(?P<changelog_tags>.+\.\..+))".format(
            REPO_OWNER, REPO_NAME
        ),
        "replacement": f" [{ '{{changelog_tags}}'}]({{{{changelog_url}}}})",
    },
]


def unified_link_replacer(match: re.Match) -> str:
    """
    A single replacement function for re.sub that handles all link types.

    It identifies which pattern was matched by checking `match.lastgroup`
    and uses the corresponding configuration from LINK_CONFIG to generate
    the correct Markdown link.

    Args:
        match: The regex match object provided by re.sub.

    Returns:
        The formatted Markdown link as a string.
    """
    # `lastgroup` gives us the name of the last capturing group that was matched.
    # This tells us which of our patterns (issue, pr, etc.) was found.
    kind = match.lastgroup
    original_text = match.group(0)

    
    config = next((c for c in LINK_CONFIG if c["name"] == kind), None)

    if not config:
        # This should not happen if the regex is built correctly,
        # but it's good practice to handle it.
        return original_text

  
    replacement_link = config["replacement"].format(**match.groupdict())

    print(f"Replace `{original_text.strip()}` with `{replacement_link.strip()}`")
    return replacement_link


def linkify_all(release_notes: str) -> str:
    """
    Applies all configured link transformations to the release notes string
    in a single pass.

    This is more efficient than the original implementation which iterated
    over the string multiple times.

    Args:
        release_notes: The original content of the release notes file.

    Returns:
        The content with all references converted to Markdown links.
    """
    combined_pattern = "|".join(config["pattern"] for config in LINK_CONFIG)

    linkified_release_notes = re.sub(
        pattern=combined_pattern,
        repl=unified_link_replacer,
        string=release_notes,
    )
    return linkified_release_notes


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for the script.
    """
    parser = argparse.ArgumentParser(
        prog="linkify-release-notes",
        description="Enhance release notes with markdown links to GitHub.",
    )
    parser.add_argument(
        "-c",
        "--check",
        action="store_true",
        default=False,
        help="Check for needed link replacements without modifying the file. "
        "Exits with status 1 if changes are needed.",
    )
    return parser.parse_args()


def main() -> None:
    """
    Main execution function.
    """
    args = parse_arguments()

    try:
        with open(RELEASE_NOTES_PATH, "r", encoding="utf-8") as f:
            original_release_notes = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{RELEASE_NOTES_PATH}'", file=sys.stderr)
        sys.exit(1)

    print(f"Checking for linkification in '{RELEASE_NOTES_PATH}'...")
    linkified_release_notes = linkify_all(original_release_notes)

    if linkified_release_notes == original_release_notes:
        print("Nothing to do, release notes are already fully linkified!")
        return


    print("\nFound references that can be linkified.")

    if args.check:
        print("The `--check` flag is active. Exiting without writing changes.")
        
        sys.exit(1)

    try:
        with open(RELEASE_NOTES_PATH, "w", encoding="utf-8") as f:
            f.write(linkified_release_notes)
        print(f"Successfully linkified '{RELEASE_NOTES_PATH}'!")
    except IOError as e:
        print(f"Error writing to file '{RELEASE_NOTES_PATH}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
