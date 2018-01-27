# frontmatter-cli

This is a very early WIP project. My goal is to make working with Frontmatter a little nicer from the command line. The API is going to change, and I plan on adding some other features to make editing Frontmatter easier too.

## Install

```bash
$ pipenv install
```

## Usage

```bash
$ python frontmatter_cli --help
Usage: frontmatter-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  main*

## Echo'ing text as Frontmatter
$ echo "Hello World!" | frontmatter-cli --title="My New Blog Post" - -
---
title: My New Blog Post
---

Hello World!
```

## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue.

[![](https://jefftriplett.com/assets/images/social/github.png)](https://github.com/jefftriplett)
[![](https://jefftriplett.com/assets/images/social/globe.png)](https://jefftriplett.com/)
[![](https://jefftriplett.com/assets/images/social/twitter.png)](https://twitter.com/webology)
[![](https://jefftriplett.com/assets/images/social/docker.png)](https://hub.docker.com/u/jefftriplett/)
