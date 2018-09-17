from ezi72ulx import build_ulx_from_source_macos
import sys, subprocess

if __name__ == '__main__':
    import sys
    story = sys.stdin.read()
    try:
        raw_ulx = build_ulx_from_source_macos(story)
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(-1)
    sys.stdout.buffer.write(raw_ulx)

