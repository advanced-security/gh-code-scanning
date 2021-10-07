# gh-code-scanning

A GitHub CLI extension to bulk-enable GitHub Code-Scanning!

### Install

```shell
gh extension install mario-campos/gh-code-scanning
```

### Usage

To enable Code-Scanning on one personal repository, "foo":

```shell
gh code-scanning --enable foo
```

To enable Code-Scanning on one organization repository, "foo/bar":

```shell
gh code-scanning --enable foo/bar
```

To bulk-enable Code-Scanning on all Python repositories (where Python is listed as the first or major language) in the organization "foo":

```shell
gh repo list --language python | cut -f 1 | xargs gh code-scanning --enable
```

To bulk-enable Code-Scanning on all Python repositories (where Python is listed as one of the languages) in the organization "foo":

```shell
gh repo list \
  --json nameWithOwner,languages \
  --jq '.[] | select(.languages.[].node.name == "Python") | .nameWithOwner' \
| xargs gh code-scanning --enable
```