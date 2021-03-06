# ezi72ulx

By [Allison Parrish](http://www.decontextualize.com/)

This is a script that reads in an Inform 7 source file from standard input and
spits out a `.ulx` file on standard output. In order to function properly, it
requires you to have the [Inform 7 IDE for macOS](http://inform7.com/download/)
installed in the default location. You may be able to use the code in the
library to easily adapt the functionality for other platforms and purposes.

Usage:

```bash
    python -m ezi72ulx.build <source.ni >output.ulx
```

You can load the resulting `.ulx` up in any
[Glulx](https://www.eblong.com/zarf/glulx/) interpreter of your choice,
including [Quixe](https://github.com/erkyrath/quixe/).

If there's a compilation error, the program exits with a non-zero return code
and displays the error to `stderr`.

## Installation

With `pip` right from GitHub:

    pip install https://github.com/aparrish/ezi72ulx/archive/master.zip

As noted above, if you want the `build` module to work as an executable, you'll
need to be running macOS and have the Inform 7 IDE installed in the expected
location (`/Applications/Inform.app`).

The code makes use of one or two of Python 3.7+ features, so you'll need to be
running that.

## How it works and why

Here's what the program does:

1. Reads in standard input and creates a Inform 7 project in a temporary directory
2. Uses the `ni` and `inform6` executables to compile the source to `.ulx`
3. Reads in the `.ulx` and prints it to standard output
4. Deletes the temporary directory

I made this so I could work the Inform 7 compilation process into my existing
workflows for programming and building tutorials.

## Limitations

This is a quick hack, so it probably doesn't... actually work for anything but
the simplest cases. I don't think it will work with extensions, for example.

## License

    Copyright 2018 Allison Parrish

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do
    so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

