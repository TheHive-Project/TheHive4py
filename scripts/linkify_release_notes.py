#!/usr/bin/env python
import argparse
import re


def replace_issue_reference(match: re.Match) -> str:
    issue_number = match.groups()[0]
    issue_link = (
        f" [#{issue_number}]"
        f"(https://github.com/TheHive-Project/TheHive4py/issues/{issue_number})"
    )
    print(f"Replace `{match.group()}` by `{issue_link}`")
    return issue_link


def linkify_issue_references(release_notes: str) -> str:
    issue_ref_pattern = r" #(\d+)"
    linkified_release_notes = re.sub(
        pattern=issue_ref_pattern,
        repl=replace_issue_reference,
        string=release_notes,
    )
    return linkified_release_notes


def replace_pr_url(match: re.Match) -> str:
    pr_url, pr_number = match.groups()
    pr_link = f" [#{pr_number}]({pr_url})"
    print(f"Replace `{match.group()}` by `{pr_link}`")
    return pr_link


def linkify_pr_urls(release_notes: str) -> str:
    pr_url_pattern = (
        r" (https:\/\/github\.com\/TheHive-Project\/TheHive4py\/pull\/(\d+))"
    )

    linkified_release_notes = re.sub(
        pattern=pr_url_pattern,
        repl=replace_pr_url,
        string=release_notes,
    )
    return linkified_release_notes


def replace_contributor_reference(match: re.Match) -> str:
    contributor = match.groups()[0]
    contributor_link = f" [@{contributor}](https://github.com/{contributor})"
    print(f"Replace `{match.group()}` by `{contributor_link}`")
    return contributor_link


def linkify_contributor_references(release_notes: str) -> str:
    contributor_ref_pattern = r" @(\w+)"

    linkified_release_notes = re.sub(
        pattern=contributor_ref_pattern,
        repl=replace_contributor_reference,
        string=release_notes,
    )
    return linkified_release_notes


def replace_full_changelog_url(match: re.Match) -> str:
    changelog_url, changelog_tags = match.groups()
    full_changelog_link = f" [{changelog_tags}]({changelog_url})"
    print(f"Replace `{match.group()}` by `{full_changelog_link}`")
    return full_changelog_link


def linkify_full_changelog_urls(release_notes: str) -> str:
    full_changelog_url_pattern = (
        r" (https:\/\/github\.com/TheHive-Project\/TheHive4py\/compare\/(.+\.\.\..+))"
    )

    linkified_release_notes = re.sub(
        pattern=full_changelog_url_pattern,
        repl=replace_full_changelog_url,
        string=release_notes,
    )
    return linkified_release_notes


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="linkify-release-notes",
        description=("enhance release notes with markdown links"),
    )
    parser.add_argument(
        "-c",
        "--check",
        action="store_true",
        default=False,
        help="just check for link replacements",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    release_notes_path = "docs/release-notes.md"
    with open(release_notes_path) as release_notes_fp:
        release_notes = release_notes_fp.read()

    print(f"Checking linkification in '{release_notes_path}'")
    linkified_release_notes = release_notes
    linkified_release_notes = linkify_issue_references(
        release_notes=linkified_release_notes
    )
    linkified_release_notes = linkify_pr_urls(release_notes=linkified_release_notes)
    linkified_release_notes = linkify_contributor_references(
        release_notes=linkified_release_notes
    )
    linkified_release_notes = linkify_full_changelog_urls(
        release_notes=linkified_release_notes
    )

    if linkified_release_notes == release_notes:
        print("Nothing to do, release notes are already linkified!")
        return

    if args.check:
        print("The `--check` flag is active, exiting without replacing!")
        exit(1)

    with open(release_notes_path, "w") as linkified_release_notes_fp:
        linkified_release_notes_fp.write(linkified_release_notes)

    print(f"Successfully linkified '{release_notes_path}'!")


if __name__ == "__main__":
    main()
