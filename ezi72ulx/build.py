from ezi72ulx import build_ulx_from_source_macos

if __name__ == '__main__':
    import sys
    story = sys.stdin.read()
    raw_ulx = build_ulx_from_source_macos(story)
    sys.stdout.buffer.write(raw_ulx)

